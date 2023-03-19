from tabulate import tabulate

def main_menu():
    # play = True
    # while play:
        #read_records()
        answer = int(input("Phone book: \n"             
                       "1. Show all records\n"      
                       "2. Add a record\n"          
                       "3. Search a record\n"       
                       "4. Change\n"                
                       "5. Delete\n"                
                       "6. Exp/Imp\n"               
                       "7. Exit\n") )                
        if 0 < answer < 8:
            print(answer)
            return answer
        else:
            print('Wrong number')

#main_menu()

def show_all_contact(contact_in): #(data)
    contact_in = {'id': ''} # входные значения контакта
    contact_out = [] # данные на ввод

    for i in range(len(contact_in)):
        contact_line = list(contact_in.values())
        contact_line.pop(0)
    contact_out.append(contact_line)

    heads = ["Surname", "Name", "Patronymic", "Phone number", "Comment"]
    print(tabulate(contact_out, headers=heads, tablefmt="rounded_outline", colalign="right"))

#show_all_contact()

def add_new_contact():
    contact = {'id': ''}
    contact['surname'] = input('Input surname: ')
    contact['name'] = input('Input name: ')
    while contact['name'] == '':
        contact['name'] = input('Name is mandatory: ')
    contact['patronymic'] = input('Input patronymic or press "Enter" to stay empty: ')
    contact['phone'] = input('Input phone number: ')
    while contact['phone'] == '':
        contact['phone'] = input('Phone number is mandatory: ')
    contact['comment'] = input('Write a comment or press "Enter" to stay empty: ')
    print(contact)
    return contact

#add_new_contact()

def search_contact():
    search_by = input("You can search a contact by surname, name, patronymic, phone number:  ")
    return search_by

#search_contact()

def change_contact(change_awnswer, data_change):
    changing = input('What a contact do you want to change? Input a phone number: ') # string with param for search
    return #отправляет данные на контроллер
    if controller_f(changing) == 0: # получение ответа от контроллера если такой номер существует или нет
        print('The phone number is absent')
    else:
        print('What do want to change?')          
        change_awnswer=int(input("1. Change a surname\n"      
                                "2. Change a name\n"          
                                "3. Change a patronymic\n"       
                                "4. Change a phone number\n"                
                                "5. Change a comment\n" ))   
        if change_awnswer == 1:
            data_change = input("Input a surname: ")    
        elif change_awnswer == 2:     
            data_change = input("Input a name: ")    
        elif change_awnswer == 3:     
            data_change = input("Input a patronymic: ")   
        elif change_awnswer == 4:     
            data_change = input("Input a phone number: ")
        elif change_awnswer == 5:     
            data_change = input("Input a comment: ")
        return change_awnswer, data_change



def delete_contact():
    deleting = input('What a contact do you want to delete? Input a phone number: ')
    controller_f(deleting) #отправляет данные на контроллер
    if controller_f(deleting) == 0: # получение ответа от контроллера если такой номер не существует или удален
        print('The phone number is absent')
    else:
        print('The contact is deleted')
    
#delete_contact()

def exp_imp():
    exp_imp_answer = int(input("Do you want to Export file or Import file: \n"             
                       "1. Export file\n"      
                       "2. Import file\n"))
    if exp_imp_answer == 1:
        exp_bd=input("Enter the name of the file: ")
        return exp_bd
    elif exp_imp_answer == 2:
        ipm_bd=input("Enter the name of the file: ")
        return ipm_bd
    else:
        print('Wrong number')