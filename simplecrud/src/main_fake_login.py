from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

from config import Settings, get_settings
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

settings: Settings = get_settings()


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "2309809d0325e7de3a5f234a44a5ed37e11988aa87f07b6216853d9f4176ac54"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$peLtpSEy.hErsmjJ6B7Jf.3UGU5ZrBPyW16kjyZhKsCA2hWM5VbJm",
        # "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    # "alice": {
    #     "username": "alice",
    #     "full_name": "Alice Wonderson",
    #     "email": "alice@example.com",
    #     "hashed_password": "fakehashedsecret2",
    #     "disabled": True,
    # },
}

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Here tokenUrl="token" refers to a relative URL token that we haven't created yet. As it's a relative URL, it's equivalent to ./token.

"""
OAuth2 was designed so that the backend or API could be independent of the server that authenticates the user.
In OAuth2 a "scope" is just a string that declares a specific permission required.
It doesn't matter if it has other characters like : or if it is a URL. - "users:read" or "items:read", "https://www.googleapis.com/auth/drive"
"""


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def fake_hash_password(password: str):
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user
    # return User(
    #     username=token + "fakedecoded",
    #     email="john@example.com",
    #     full_name="John Doe",
    # )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    # user = fake_decode_token(token)
    # if not user:
    #     raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    # print(f"current_user.disabled:{current_user.disabled}")
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

    # user_dict = fake_users_db.get(form_data.username)
    # if not user_dict:
    #     raise HTTPException(
    #         status_code=400, detail="Incorrect username or password"
    #     )
    # user = UserInDB(**user_dict)
    # hashed_password = fake_hash_password(form_data.password)
    # if not hashed_password == user.hashed_password:
    #     raise HTTPException(
    #         status_code=400, detail="Incorrect username or password"
    #     )

    # return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":

    # hashed_password = get_password_hash("secret")
    # print(hashed_password)

    import uvicorn

    # TODO: read the app version
    # print(f"Running the version:{settings.APP_VERSION}")
    print(f"simplecrud is running on {settings.HOST}:{settings.PORT}")
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )


"""
# TODO:
1. create endpoints for CRUD operations
2. connect to the database
3. create a model for the database
4. Log requests and responses(status code, response time, )
5. Add authentication(optional)
"""
