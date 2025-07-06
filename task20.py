permissions = {"read": True, "write": False, "delete": True}
keys_list = list(permissions.keys())
values_list = list(permissions.values())
print(type(values_list))

for i in range(len(values_list)):
    if values_list[i] == True:
        print(keys_list[i], end="  ")
