import read
import view
import record

data_base = "sample_data_base.txt"
all_data = read.get_data(data_base, ",")
last_id = int(all_data[-1]["id"])

# Есть ли контакты, содержащие заданную строку? 
# Результат - структура, аналогичная all_data (пустая или нет), 
# содержащая список контактов, содержащих заданную строку хотя бы в одном из полей
def contacts_containing_string (str) :
    global all_data
    
    result = []
    for i in range(len(all_data)) :
        equal = 0
        for key in {"surname","name", "patronymic", "phone"} :
            if str == all_data[i][key] :
            # Можно заменить на in, если мы хотим находить по части строки
                equal += 1
                break
        if equal > 0 :
            result.append(all_data[i])
    return result # возвращает список контактов, в которые (в любое поле) входит заданная строка

# Есть ли в базе контакт, содержащий заданный телефон? 
# Результат - -1, если такого контакта нет; index в all_data - если такой контакт есть. 
def found_contact_by_phone (phone_str) :
    global all_data    
    res = -1
    for i in range(len(all_data)) :
        if all_data[i]["phone"] == phone_str : 
            res = i
            break
    return res # возвращает список контактов, в которые (в любое поле) входит заданная строка

# Функция ищет переданный ей контакт в базе данных и возвращает 1, 
# если контакт существует, и 0 - если такого контакта нет
def contact_exists (new_contact) : 
    global all_data
    i = 0
    res = 0
    while i in range(len(all_data)) and res == 0 :
        same_contact = 0 
        # id и комментарий не проверяем : 
        for j in {'surname','name','patronymic','phone','contact'} :
            same_contact += (all_data[i][j] == new_contact[j])
        if same_contact == 5 :
            res = 1
            view.info_message(f"Такая запись уже существует.")
            break
        i += 1
    return res

user_choice = view.main_menu()

while user_choice != 7:
# **********ПОКАЗАТЬ ВСЕ КОНТАКТЫ**********************
    if user_choice == 1:
        # !!!!!!!!!!!!!! НЕ РАБОТАЕТ !!!!!!!!!!!!!!!!!!
        view.show_all_contact(all_data)

# **********ДОБАВИТЬ КОНТАКТ В БАЗУ ДАННЫХ**********************
    elif user_choice == 2:
        new_contact = view.add_new_contact()
        if not contact_exists (new_contact) : 
            last_id += 1
            new_contact["id"] = last_id
            all_data.append(new_contact)
            record.write_data(all_data, data_base)
        # Мы хотим, чтобы на экран вывелся один контакт? 
            view.info_message("Контакт добавлен")
        else : 
            view.info_message("Такой контакт уже существует. ")

    # **********НАЙТИ КОНТАКТ(Ы) В БАЗЕ ДАННЫХ ПО ЗАДАННОЙ СТРОКЕ*********
    elif user_choice == 3:
        string_to_find = view.search_contact()
        found_list_of_contacts = []
        found_list_of_contacts += contacts_containing_string(string_to_find)
        view.show_all_contact (found_list_of_contacts)

    # **********ВНЕСТИ ИЗМЕНЕНИЕ В КОНТАКТ*********
    elif user_choice == 4:
        ind, digit, meaning = view.change_contact()
        key = ''
        match digit : 
            case 1 : 
                key = "surname"
            case 2 : 
                key = "name"
            case 3 : 
                key = "patronymic"
            case 4 : 
                key = "phone"
            case 5 :  
                key = "comment"
            case _ : 
                ind = -1
        if ind != -1 : 
            all_data[ind][key] = meaning
            view.info_message("Изменения внесены в справочник")
            record.write_data(all_data, data_base)

    # **********УДАЛИТЬ КОНТАКТ ПО НОМЕРУ ТЕЛЕФОНА*********        
    elif user_choice == 5:
            tel_number = view.delete_contact()
            ind = found_contact_by_phone (tel_number)
            if ind >= 0 : 
                all_data.pop(ind)

    # **********ЭКСПОРТИРОВАТЬ ИЛИ ИМПОРТИРОВАТЬ СПРАВОЧНИК ********* 
     elif user_choice == 6:
            digit, file_name = view.exp_imp()
            match digit : 
                case 1 : # Export
                    record.write_data(all_data, file_name)
                case 2 : # Import
                    write_data (all_data, data_base)
                    # Если хотим дальше работать с этим справочником
                    # read_data (all_data, file_name) 
                    # data_base = file_name

                    # А если хотим "дописать" этот файл к тому, с которым работем, 
                    # нужно применить функцию дозаписи в файл data_base, и желательно 
                    # потом показать пользователю полное содержимое обновленной базы

    user_choice = view.main_menu()


















