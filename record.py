last_id = 0
all_data = []
file_base = 'tel_book.csv'


def record(name, patronymic, surname, phone, comment):
    global last_id
    global all_data


    if(name == ''):
        print('Поле не заполнено!')
        return
    if(patronymic == ''):
        print('Поле не заполнено!')
        return
    if(surname == ''):
        print('Поле не заполнено!')
        return
    if(phone == ''):
        print('Поле не заполнено!')
        return
    if(comment == ''):
        print('Поле не заполнено!')
        return

    for i in all_data:
        if(i[1] == name.title() and 
           i[2] == patronymic.title() and 
           i[3] == surname.title() and 
           i[4] == phone and 
           i[5] == comment.title()):
            print('Контакт уже существует!')
            return

    last_id += 1
    new_all_data = [str(last_id), name.title(), patronymic.title(), surname.title(), phone, comment.title()]
    all_data.append(new_all_data)

    with open('tel_book.csv', 'a') as file:
        file.write('record;\n')
