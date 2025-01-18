
# Use an official Python runtime as a parent image
FROM python:3.10.14-slim

COPY requirements/base.txt /usr/local/src/requirements.txt  
# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir --ignore-installed --upgrade -r /usr/local/src/requirements.txt  

WORKDIR /usr/local/src/
# Prevents Python from writing pyc files to disc. Equivalent to python -B
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr. Equivalent to python -u
ENV PYTHONUNBUFFERED 1

COPY ./src /usr/local/src 
EXPOSE 8020

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8020"]

# # ---- Base ----
#     FROM alpine:3.19.1 AS base

#     ## needed for building grpcio - build-base linux-headers, python3-dev
#     RUN apk add --update --no-cache make git libffi-dev tk-dev build-base gcc musl-dev zip openssl \
#         python3 py3-pip linux-headers python3-dev py3-setuptools
    
#     RUN apk add --update --no-cache make bash git libffi-dev tk-dev build-base gcc musl-dev curl py3-pip zip openssl python3 py3-setuptools
#     COPY requirements/base.txt /usr/local/src/requirements.txt  
#     RUN pip3 install --no-cache-dir --ignore-installed --upgrade -r /usr/local/src/requirements.txt  
    
#     WORKDIR /usr/local/src/
#     # Prevents Python from writing pyc files to disc. Equivalent to python -B
#     ENV PYTHONDONTWRITEBYTECODE 1
#     # Prevents Python from buffering stdout and stderr. Equivalent to python -u
#     ENV PYTHONUNBUFFERED 1
    
#     COPY ./src /usr/local/src 
#     EXPOSE 8020
#     ## run health-check defaults:  --interval=30s --timeout=30s --retries=3
#     # HEALTHCHECK CMD curl -sf http://127.0.0.1:7600/status || exit 1
    
#     CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8020"]
#     # CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8020"]
#     # CMD ["gunicorn", "-c", "gunicorn.conf.py",  "main:app"]