def get_active_users(users: dict[str, dict[str, bool]]) -> list[str]:
    active_users_names = list()
    for user in list(users.items()):
        user2 = list(user[1].items())
        if user2[0][1]:
            active_users_names.append(user[0])
    return active_users_names

users = {
    "Ali" : {'active': False},
    "Vali" : {'active': True},   #1
    "Abdulla" : {'active': False},
    "G'aybulla" : {'active': False},
    "Abdujalil" : {'active': True}, #2
    "Aziz" : {'active': True},   #3
    "Bobur" : {'active': False},
    "G'anisher" : {'active': True}  #4
}
print(get_active_users(users))