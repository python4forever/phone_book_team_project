from tabulate import tabulate

def add_new_contact():
    contact = {'id': ''}
    contact['surname'] = input('Input surname: ')
    while contact['surname'] == '':
        contact['surname'] = input('Surname is mandatory: ')
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


def show_all_contact(): #(data)
    contact_in = {'id': '', 'surname': '65156', 'name': 'Hyt', 'patronymic': 'UHT', 'phone': '651', 'comment': 'jkhlj'}
    contact_out = []

    for i in range(len(contact_in)):
        contact_line = list(contact_in.values())
        contact_line.pop(0)
    contact_out.append(contact_line)


    heads = ["Surname", "Name", "Patronymic", "Phone number", "Comment"]
    print(tabulate(contact_out, headers=heads, tablefmt="rounded_outline", colalign="right"))

def search_contact():
    print("Your can search a contact by surname, name or phone number")
    search_by = input("Write here: ")
    return search_by



show_all_contact()