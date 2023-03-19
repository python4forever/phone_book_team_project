# Модуль тестирования контроллера

data = [{"id":1, "surname":"Калашникова", "name":"Татьяна", "patronymic":"Борисовна",
        "phone":"89150550573", "comment":"Я"}, 
        {"id":2, "surname":"Кузькина", "name":"Екатерина", "patronymic":"Андреевна",
        "phone":"89150550569", "comment":"Дочь"}, 
        {"id":3, "surname":"Калашникова", "name":"Галина", "patronymic":"Владимировна",
        "phone":"89165869834", "comment":"мама"},
        {"id":4, "surname":"Кузькин", "name":"Андрей", "patronymic":"Анатольевич",
        "phone":"89163616869", "comment":"Катин папа"}, 
        {"id":5, "surname":"Афанасьева", "name":"Тамара", "patronymic":"Кондратьевна",
        "phone":"89035860606", "comment":"Соседка из 177 кв."}, 
        {"id":6, "surname":"Власова", "name":"Ирочка", "patronymic":"",
        "phone":"89163429834", "comment":"Без комментариев"}, 
        {"id":7, "surname":"Валюшок", "name":"Андрей", "patronymic":"Сергеевич",
        "phone":"89268930932", "comment":"Угарный господин"}]
last_id = int(data[-1]["id"])

print(len(data))
print(last_id)

def add_contact(new_contact) : 
#     global data
    i = 0
#new_contact = view.get_new_contact() 
# Функция get_new_contact должна возвращать словарь с данными нового контакта 
# с ключом (last_id+1), если у нас last_id - глобальная для всех модулей
    while i < len(data) : 
        print(f"Внешний цикл, i = {i}")
        is_same_contact = 0
        # [i for i in data if value in i.values()]
        for j in set(data[i].keys())-{"id"} : 
            print(f"Внyтренний цикл, j = {j}")
            is_same_contact += (data[i][j] == new_contact[j])
            print(is_same_contact)
        if is_same_contact == 5 : 
            print(f"Такая запись уже существует. Это запись с идентификатором" {i}.\n")
            break
        i += 1
    else: 
        last_id += 1
        new_contact["id"] = last_id
        data.append(new_contact)
    return data

# print(type(data))
# print(dir(data))
# print(dir(data[0]))

for i in range(len(data)) : 
    for key,value in data[i].items() : 
        print(value, end="  ")
    print()

# keys = data[0].keys()
# values = data[0].values()

# print(f"Тип структуры keys есть {type(keys)}")
# print(f"Тип структуры values есть {type(values)}")
# print(set(data[0].keys()))

contact_to_add = {"id":3, "surname":"Калашникова", "name":"Галина", "patronymic":"Владимировна",
        "phone":"89165869834", "comment":"мама"} 

data = add_contact(contact_to_add)

print(data)
 