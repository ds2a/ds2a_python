import json

s = """{ "name" : "John" , "age" : 30 , "city" : "New York"}"""
# s = '{ "name" : "John" , "age" : 30 , "city" : "New York"}'

#converting (de serialising) json sting to a python object
python_s_object = json.loads(s)

print(python_s_object)
print(type(python_s_object))
print(python_s_object['name'])

#converting (serialising) python object to a json sting
s1 = json.dumps(python_s_object,indent=4, sort_keys=True)
print(s1)
print(type(s1))








