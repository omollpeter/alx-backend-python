#!/usr/bin/python3

get_json = __import__("utils").get_json

data = get_json("https://swapi.dev/api/people/1")
print(data)
