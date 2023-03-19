import view
import read
import record

last_id = 0
data = read.get_data(sample_data_base.txt, ",") 

# view.menu()
# view.new_contact()
# view.search_contact():  имя, фамилия, отчество, телефон
# view.edit_contact() 

def main_logic(): 
    # value или user_choice
    
    user_choice = view.main_menu() # возвращает цифру
# "Phone book: \n"             
# "1. Show all records\n"      
# "2. Add a record\n"          
# "3. Search a record\n"       
# "4. Change\n"                
# "5. Delete\n"                
# "6. Exp/Imp\n"               
# "7. Exit\n") )  
    while user_choice != 7 : 
        if user_choice == 1 : 
            view.show_all_contact()
        elif user_choice == 2: 
            new_contact = view.add_new_contact() # вернет словарь с 'id': '' и данными нового контакта
            add_contact (new_contact)
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