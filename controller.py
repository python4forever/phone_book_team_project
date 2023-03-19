import view
import read
import record

# all_data = read.get_data(sample_data_base.txt, ",") 

all_data = [{"id":"1", "surname":"Калашникова", "name":"Татьяна", "patronymic":"Борисовна",
        "phone":"89150550573", "comment":"Я"}, 
        {"id":"2", "surname":"Кузькина", "name":"Екатерина", "patronymic":"Андреевна",
        "phone":"89150550569", "comment":"Дочь"}, 
        {"id":"3", "surname":"Калашникова", "name":"Галина", "patronymic":"Владимировна",
        "phone":"89165869834", "comment":"мама"},
        {"id":"4", "surname":"Кузькин", "name":"Андрей", "patronymic":"Анатольевич",
        "phone":"89163616869", "comment":"Катин папа"}, 
        {"id":"5", "surname":"Афанасьева", "name":"Тамара", "patronymic":"Кондратьевна",
        "phone":"89035860606", "comment":"Соседка из 177 кв."}, 
        {"id":"6", "surname":"Власова", "name":"Ирочка", "patronymic":"",
        "phone":"89163429834", "comment":"Без комментариев"}, 
        {"id":"7", "surname":"Валюшок", "name":"Андрей", "patronymic":"Сергеевич",
        "phone":"89268930932", "comment":"Угарный господин"}]

last_id = int(all_data[-1]["id"])

# Метод add_contact добавляет переданный в него контакт (словарь с пустым id) в 
# нашу базу. Присваивает ему следующий за last_id идентификатор и увеличивает last_id на 1
def add_contact(new_contact) : 
    global all_data
    global last_id
    i = 0

    while i < len(all_data) : 
        print(f"Внешний цикл, i = {i}")
        is_same_contact = 0
        # [i for i in data if value in i.values()]
        for j in set(all_data[i].keys())-{"id"} : 
            print(f"Внyтренний цикл, j = {j}")
            is_same_contact += (all_data[i][j] == new_contact[j])
            print(is_same_contact)
        if is_same_contact == 5 : 
            print(f"Такая запись уже существует. Это запись с идентификатором {i}.\n")
            break
        i += 1
    else: 
        last_id += 1
        print(last_id)
        new_contact["id"] = str(last_id)
        print(f"Добавили идентификатор к контакту: \n{new_contact}")
        all_data.append(new_contact)

# Метод find_by принимает на вход строку и возвращает список всех тех словарей 
# из нашего справочника, в которых в каком-либо из полей встретилась искомая строка
def find_by (string_to_search) :
    global all_data 
    global last_id

    result = []
    for i in range(len(all_data)) : 
        equal = 0
        for key in {"surname","name", "patronymic", "phone"} :
            if string_to_search == all_data[i][key] :
                equal +=1
                break
        if equal > 0 : 
            result.append(all_data[i])
    return result

# Функция index_by_phone возвращает индекс элемента в списке all_data по номеру телефона. 
# Если контакта с таким номером телефона нет, возвращает -1
def index_by_phone (phone_number) : 
    global all_data
    global last_id
    found = False

    i = 0
    while i < len(all_data) : 
        if all_data[i]["phone"] == phone_number : 
            found = True
            break
        i += 1
    if i < len(all_data) : 
        return i
    else : 
        return -1  

# Функция index_by_id возвращает индекс элемента в списке all_data по номеру id.
# Если такого контакта нет, возвращает -1
def index_by_id (id_number) : 
    global all_data
    global last_id
    found = False

    i = 0
    while i < len(all_data) : 
        if all_data[i]["id"] == str(id_number) : 
            found = True
            break
        i += 1
    if i < len(all_data) : 
        return i
    else : 
        return -1  

# Функция delete_by_phone удаляет из справочника контакт с заданным номером телефона, 
# если такой контакт в нем есть
def delete_by_phone (phone_number) : 
    global all_data
    global last_id
    ind = index_by_phone(phone_number)
    if ind != -1 : 
        all_data.pop(i)

def delete_by_id (id_number) : 
    global all_data
    global last_id
    ind = index_by_id(id_number)
    if ind != -1 : 
        all_data.pop(i)

def change_record (index, key, meaning) : #index - индекс записи в all_data, нумерация с нуля
                            # "id" - 0, "surname" - 1, "name" - 2, ... "comment" - 5
                            # key - ключ, который меняем
                            # meaning - строка, на которую меняем
    global all_data
    global last_id

    all_data[index][key] = meaning
    
def main_logic(): 
    # value или user_choice
    global all_data
    global last_id

    user_choice = view.main_menu() # возвращает цифру
# "Phone book: \n"             
# "1. Show all records\n"      
# "2. Add a record\n"          
# "3. Search a record\n"       
# "4. Change\n"                
# "5. Delete\n"                
# "6. Exp/Imp\n"               
# "7. Exit\n") )  
    play = True
    while play : 
        user_choice = view.main_menu()
        match user_choice : 
            case 1 : 
                view.show_all_contact(all_data)

            case 2: 
                new_contact = view.add_new_contact() # вернет словарь с 'id': '' и данными нового контакта
                add_contact (new_contact)
                view.message("Контакт добавлен в базу")

            case 3: 
                if find_by (view.search_contact()) != [] : 
                    view.message("Вот все найденные по вашему ключу контакты: ")
                    view.show_all_contact (find_by(view.search_contact()))
                else : 
                    view.message("По заданному ключу контактов не найдено.")

            case 4:
                key_str = view.get_text_field("Введите ключ для поиска : ")
                res = find_by(key_str)
                if len(res) == 0 : 
                    view.message("Такой контакт отсутствует в справочнике.")
                else : 
                    if len(res) == 1 : 
                        view.message("По вашему ключу найдена одна запись: ")
                        view.show_all_contact(res)
                        id = res[0]["id"]
                    else : 
                        view.message("По вашему ключу найдено несколько записей: ")
                        view.show_all_contact(res)
                        id = view.get_text_field("Введите id записи, которую будем менять: ")
                
                    ind = index_by_id(id)

                    key = view.get_user_answer("Какое поле меняем? \n"+ 
                                        " s - surname\n"+
                                        " n - name\n"+
                                        " p - patronymic\n"+ 
                                        " t - phone\n"+
                                        " c - comment\n"+
                                        " Enter a corresponding symbol ==> ")
                    if key in {"s","n","p","t","c"} : 
                        change_record(ind, key, view.get_text_field("На что меняем?"))
                        view.message("В телефонный справочник внесено изменение: \n")        
                        view.show_all_contact((all_data[ind]))
                    else :
                        view.mesage("Incorrect data") 

            case 5:
                key_str = view.get_text_field("Введите ключ для поиска : ")
                res = find_by(key_str)

                if len(res) == 0 : 
                    view.message("Такой контакт отсутствует в справочнике.")
                else : 
                    if len(res) == 1 : 
                        view.message("По вашему ключу найдена одна запись: ")
                        view.show_all_contact(res)
                        id = res[0]["id"]
                    else : 
                        view.message("По вашему ключу найдено несколько записей: ")
                        view.show_all_contact(res)
                        id = view.get_text_field(f"Введите id записи, которую хотите удалить =>")
                    
                    agree = view.get_text_field(f"Удаляем запись с ключом {id} (Y/N)? ")
                
                    if agree == "Y" : 
                        delete_by_id (id)
                        view.message(f"Запись с ключом {id} удалена из справочника.")
                    else : 
                        view.message(f"Никаких изменений внесено не было.")
# Export/Import : 
            case 6:
                action = view.get_text_field(f"Введите i для импорта, e - для экспорта =>")
                match action : 
                    case "i" : 
                        file_name = view.get_text_field(f"Введите имя файла для импорта данных =>")
                        read.import_data(file_name)
                    case "e" : 
                        file_name = view.get_text_field(f"Введите имя файла для экспорта данных =>")
                        reсord.export_data(file_name)
                    case _ : 
                        view.message("Incorrect data")
            
            case 7 : 
                play = False

            case _ : 
                pass
# Метод show_all принимает на вход список словарей вида 
# [{"ID":<Номер записи>, "Name":<Имя_чел>, "Surname":<Отчество>, ... "Tel":<Телефон>}, 
# {}, {}, ... {}] и передает его в модуль view для вывода на экран

def show_all (data) : 
    view.show_data(data) 

# Метод find_by_last_name принимает на вход список словарей вида 
# [{"ID":<Номер записи>, "Name":<Имя_чел>, "Surname":<Отчество>, ... "Tel":<Телефон>}, 
# {}, {}, ... {}], в котором надо найти все записи с определенной фамилией, 
#  и передает его в модуль view для вывода на экран

# Предполагается, что метод get_last_name() из модуля data_input возвращает 
# строковые значения ФИО с уже примененной к ним функцией capitalize()

def find_by_last_name (data) : 
    last_name = view.get_last_name()
    records_of_interest = [data[i] for i in range(len(data)) if data[i][1] == last_name]
    view.show_data(records_of_interest) 
    return records_of_interest

def find_by_name (data) : 
    name = view.get_name()
    records_of_interest = [data[i] for i in range(len(data)) if data[i][2] == name]
    view.show_data(records_of_interest) 
    return records_of_interest

def find_by_patronymic (data) : 
    patronymic = view.get_patronymic()
    records_of_interest = [data[i] for i in range(len(data)) if data[i][3] == patronymic]
    view.show_data(records_of_interest) 
    return records_of_interest

# Предполагается, что метод get_telephone модуля data_input возвращает 
# строку из 13-ти цифр, и в таком же виде телефоны хранятся в нашей базе

def find_by_telephone (data) : 
    patronymic = view.get_telephone()
    records_of_interest = [data[i] for i in range(len(data)) if data[i][4] == patronymic]
    view.show_data(records_of_interest) 
    return records_of_interest

def add_contact (contact) : 
    new_contact = view.get_new_contact() 
# Функция get_new_contact должна возвращать словарь с данными нового контакта 
# с ключом (last_id+1), если у нас last_id - глобальная для всех модулей
    while i in range(len(data)) : 
        is_same_contact = 0
        # [i for i in data if value in i.values()]
        for j in {'surname','name','patronymic','phone','contact'} : 
            is_same_contact += (data[i][j] == new_contact[j])
        if is_same_contact == 5 : 
            view.message(f"Такая запись уже существует. Ее идентификатор равен {i}.\n")
            break
    else: 
        last_id += 1

    return data