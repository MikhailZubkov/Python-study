# def show_menu():
#     print("\nВыберите необходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. Найти абонента по фамилии\n"
#           "3. Найти абонента по номеру телефона\n"
#           "4. Добавить абонента в справочник\n"
#           "5. Сохранить справочник в текстовом формате\n"
#           "6. Закончить работу")
#     choice = int(input())
#     return choice

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def print_result(data):
    for i in data:
        for k, v in i.items():
            print(f"{k:10} : {v}")
        print()
    input("Для продолжения нажмите клавишу Enter")

def find_lastname(data):
    lastname = input("Введите фамилию: ")
    for i in data:
        if lastname in i["Фамилия"]:
            for k, v in i.items():
                print(f"{k:10} : {v}")
    input("Для продолжения нажмите клавишу Enter")

def find_number(data):
    number = input("Введите номер телефона: ")
    for i in data:
        if i["Телефон"] == number:
            for k, v in i.items():
                print(f"{k:10} : {v}")
    input("Для продолжения нажмите клавишу Enter")

def add_user(data):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    list_1 = []
    list_1.append(input("Введите фамилию: "))
    list_1.append(input("Введите имя: "))
    list_1.append(input("Введите номер: "))
    list_1.append(input("Введите описание: "))
    new_user = dict(zip(fields, list_1))
    data.append(new_user)
    print("Вы добавили нового пользователя")
    for k, v in new_user.items():
        print(f"{k:10} : {v}")
    print()
    input("Для продолжения нажмите клавишу Enter")

def save_changes(data):
    with open("phon.txt", 'w', encoding='utf-8') as new_file:
        for i in data:
            str_i = ""
            for v in i.values():
                str_i += v + ","
            str_i = str_i[:-1]
            new_file.write(str_i + "\n")
            print("Данные сохранены!")

choice = show_menu()
phone_book = read_csv("phonebook.csv")

while (choice != 6):
    if choice == 1:
        print_result(phone_book)

    elif choice == 2:
        find_lastname(phone_book)

    elif choice == 3:
        find_number(phone_book)

    elif choice == 4:
        add_user(phone_book)

    elif choice == 5:
        save_changes(phone_book)
    choice = show_menu()