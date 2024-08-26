#!/usr/bin/python3

access_nested_map = __import__("utils").access_nested_map

nested_map = {"a": {"c": 1}}
count = access_nested_map(nested_map, ["a", "b", "c"])

print(nested_map["c"])
