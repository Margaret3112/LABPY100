users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']


dic1 = {"Общее количество": 0,
"Уникальные посещения":0}
dic1["Общее количество"] = len(users)
change = set(users)
dic1["Уникальные посещения"] = len(change)
print(dic1)

