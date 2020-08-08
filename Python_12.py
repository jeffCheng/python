
# file = open("data.txt", mode="w", encoding="utf-8")
# file.write("Hello File \nSeconde line")
# file.close()

with open("data.txt", mode = "w") as file:
    file.write("fffff")

with open("data.txt", mode = "r") as file:
    data = file.read()

print(data)

sum_num = 0
with open("data1.txt", mode = "w") as file:
    file.write("5\n3")

with open("data1.txt", mode = "r") as file:
    for line in file:
        sum_num+=int(line)

print(sum_num)

import json
with open("config.json", mode = 'r') as file:
    data = json.load(file)

print("name", data["name"])
data["name"] ="HaHa"

with open("config.json", mode = 'w') as file:
    json.dump(data, file)
