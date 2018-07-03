import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# with open("data_file.json","w") as write_file:
#     json.dump(data,write_file)


json_string = json.dumps(data)

print(json_string)
json_string = json.dumps(data, indent=4)
print(json_string)

#Deserializing
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

print(type(encoded_hand))#<class 'str'>
print(type(decoded_hand))#<class 'list'>

print(blackjack_hand == tuple(decoded_hand)) #True

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print(data)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(json_string)

print(data)





#https://realpython.com/python-json/
