import json


print("Started Reading JSON file")
with open("test.json", "r") as read_file:
 print("Converting JSON encoded data into Python dictionary")
 developer = json.load(read_file)

print(developer)
print(type(developer))

print("Decoded JSON Data From File")
for key, value in developer.items():
    print(key, ":", value)
    print("Done reading json file")


# write to a file
with open("test_1.json", "w") as write_file:
    json.dump(developer, write_file)








