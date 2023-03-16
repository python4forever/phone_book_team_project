import view

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

def add_new_contact (data) : 
    new_contact = view.get_new_contact() 
# Функция get_new_contact должна возвращать словарь с данными нового контакта 
# с ключом (last_id+1), если у нас last_id - глобальная для всех модулей
    indeed_new = True
    for i in range(len(data)) : 
        if data[i] == new_contact : 
            indeed_new = False
            view.message("Такая запись уже существует.")
            break
    if indeed_new : 
        data = data.append(new_contact)
        last_id += 1
    return data
