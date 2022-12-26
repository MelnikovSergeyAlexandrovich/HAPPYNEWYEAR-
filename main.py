import os
import csv
from tabulate import tabulate
role = "user"
goods = {}
users = {}
def input_pos(prompt, error_message) -> str:
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка(позиция). В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        _str = input(prompt)
        if str.isalpha(_str):
            return _str
        print(error_message)

def input_str(prompt, error_message):
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка - ее длина меньше 3 и больше 21. В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        _str = input(prompt)
        str = len(_str)
        if str > 3 and str < 21:
            return _str
        print(error_message)

def input_ustr(prompt, error_message):
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка. В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        try:
            _str = input(prompt)
            return _str
        except:
            print(error_message)

def input_float(prompt, error_message):
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенно число с плавающей запятой. В другом случае возвращает введенное число
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        try:
            return float(input(prompt))
        except:
            print(error_message)


def input_int(prompt, error_message):
    """
        Функция, которая выводит сообщение о ошибке, если неправильно введенно целое число. В другом случае возвращает введеное число
        :param prompt:
        :param error_message:
        :return:
        """
    while True:
        try:
            return int(input(prompt))
        except:
            print(error_message)

def delete_position() -> None:
    """
    Функция, которая отвечате за удаление выбранной позиции. Пользователь вводит название товара и по данному индексу удаляется вся строка.
    :return:
    """
    string = input_ustr("Введите название товара, который хотите удалить: ","Ошибка. Название введенно неправильно")
    import fileinput
    for line in fileinput.input('shoplifting.csv', inplace=True):
        if string in line:
            continue
        print(line, end='')


def redact_position() -> None:
    """
    Функция, которая редактирует выбранную позицию - индекс. Сначала нужно ввести число строки, потом число столбца и в конце нужно ввести новый текст для данного индекса.
    Также в функции реализовано удаление всех пробелов из файлов, т.к. при работе данной функции в файлах появляются пробелы между строками и с ними становится невозможно работать.
    :return:
    """
    with open('shoplifting.csv', newline='') as in_file:
        with open('dublicate.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)

    pos_1 = input_int("Введите имя строки: ", "Имя строки введенно неправильно")
    pos_2 = input_int("Введите имя столбца: ", "Имя столбца введенно неправильно")
    new_text = input_ustr("Введите текст для данной ячейки:","Ошибка. Текст введён неверно")
    r = csv.reader(open('dublicate.csv'))  # Here your csv file
    lines = [l for l in r]
    list(r)
    lines[pos_1][pos_2] = new_text
    writer = csv.writer(open('shoplifting.csv', 'w'))
    writer.writerows(lines)

    with open('shoplifting.csv', newline='') as in_file:
        with open('dublicate.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)


def read_csv() -> None:
    """
    Функция, которая отвечает за чтение csv файла, который содержит в себе все товары. Все прочитанные данные помещает в словарь
    :return:
    """
    path = "shoplifting.csv"
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Для пропуска
        for row in csv_reader:
            number_of_pos, name, description, diller, price, num = row
            goods = {"name:": str(name), "description": str(description),
                     "diller": str(diller), "price": float(price), "number": int(num)}

def add_position() -> None: #(наименование, описание, поставщик, цена, доступное количество)
    """
    Функция, которая отвечает за добавление товаров в cvs файл. Все товары вводятся через консоль.
    """
    name = input_ustr("Введите имя товара: ","Недопустимое имя товара.")
    description = input_pos("Введите описание товара: ","Недопустимое описание товара")
    diller = input_pos("Введите поставщика данного товара: ","Недопустимое имя поставщика товара")
    price = input_float("Введите цену для данного товара: ","Недопустимая цена товара")
    num = input_int("Введите количество данного товара: ","Недопустимое количество товара")
    with open("shoplifting.csv", 'a') as f:
         f.write(f"\n{name},{description},{diller},{price},{num}")


def database_reader() -> None:
    """
    Функция, которая отвечает за прочтение файла из cvs файла - датабазы со всеми данными о пользователях. Все данные помещаются в словарь
    :return:
    """
    global users
    path = "data.csv"
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Для пропуска
        for row in csv_reader:
            login,password,role = row
            users = {"login":str(login),"paasword":str(password),"role":str(role)}

def interface_for_admin(file_name2) -> None:
    """
    Функция, которая является меню для админа. В ней есть 5 функций - Добавление позиции, редактирование позиции, удаление позиции, просмотр позиций и выход обратно в общее меню.
    :param file_name2:
    :return:
    """
    global number_of_pos
    global goods
    while True:
        print("==============================================")
        print("Выберете действие:")
        oper = int(input("1. Добавить позицию\n"
                     "2. Редактировать уже существующую позицию\n"
                     "3. Удалить позицию\n"
                     "4. Просмотр позиций\n"
                     "5. Выход\n"))
        if oper == 1:
            add_position()
        elif oper == 2:
            redact_position()
        elif oper == 3:
            delete_position()
        elif oper == 4:
            interface_for_user()
        elif oper == 5:
            return

def interface_for_user() -> None:
    """
    Функция, которая отвечает за интерфейс для обычного пользователя. Здесь с помощью прочитанного csv файла с товарами, функции sorted и tabulate выводятся все товары.
    Также эта функция реализована и в меню у админа. (ТЗ)
    :return:
    """
    global goods
    with open('shoplifting.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        sorted_dict = sorted(list(reader), key=lambda k: k['name'])
    print(tabulate(sorted_dict, headers="keys", tablefmt='grid'))


def autorization(file_name2) -> None:
    """
    Функция, которая отвечает за авторизацию пользователей. С помощью прочитанного csv файла со всеми пользователями через цикл for он проверяет наличие введенных данных в базе.
    Если пользователь является админом, то для него реализуется меню для админа, в другом случае, реализуется меню для обычного пользователя
    :param file_name2:
    :return:
    """
    global users
    print("==============================================")
    print("Войдите в аккаунт.")
    loginnn = input_str("Введите логин:\n","Недопустимый логин")
    passworddd = input_str("Введите пароль:\n","Недопустимый пароль")
    with open('data.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        sorted_dict = sorted(reader, key=lambda k: k['login'])
        for row in sorted_dict:
            login,password,role = row
            if row[login] == loginnn:
                if row[password] == passworddd:
                    print("Вы вошли!")
                    if loginnn == "admin" and passworddd == "admin":
                        interface_for_admin(file_name2)
                    else:
                        interface_for_user()




def registration() -> None:
    """
    Функция, которая отвечает за регистрацию пользователей. Если введенный логин подьзователем совпадает с логином из базы данных, то она повторно просит ввести логин.
    Если введенные пароли не совпадают, то она повторно просит ввести логин и пароль.
    Если регистрация прошла успешно - все введенно правильно, то она добавляет все данные о пользователе в файл.
    :return:
    """
    while True:
        print("==============================================")
        loginnn = input_str("Придумайте логин:\n", "Логин должен содержать от 4 до 20 символов")
        with open('data.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            sorted_dict = sorted(reader, key=lambda k: k['login'])
            for row in sorted_dict:
                login,password,role = row
                if row[login] == loginnn:
                    print("Ошибка. Это имя пользователя уже занято")
                else:
                    passworddd = input_str("Придумайте пароль:\n", "Пароль должен содержать от 4 до 20 символов")
                    password_2 = input_str("Придумайте пароль:\n", "Пароль должен содержать от 4 до 20 символов")
                    if passworddd != password_2:
                        print("Ошибка. Пароли не совпадают.")
                    else:
                        print("Регистрация прошла успешно!")
                        role = "user"
                        with open("data.csv", 'a') as f:
                            f.write(f"\n{loginnn},{passworddd},{role}")
                        return



def main() -> None:
    """Основная функция. В ней реализовано:
    1) Если файл для хранения инф-и о пользователях и товарах не существует, то она их создаёт.
    2) В ней реализовано меню, которое даёт пользователю выбор: Авторизация, Регистрация или же выход из программы.
    """
    file_name1 = "data.csv"
    file_name2 = "shoplifting.csv"
    if not os.path.exists(file_name2):
        with open(file_name2, 'w') as f:
            f.write("name,description,diller,price,num")

    if not os.path.exists(file_name1):
        with open(file_name1, 'w') as f:
            f.write("login,password,role")


    while True:
        print("\n===================================================")
        func = input_int("Выберете действие.\n"
            "1. Войти в аккаунт.\n"
            "У вас до сих пор нет аккаунта?\n"
            "2. Зарегистрироваться\n"
            "3. Выйти\n","Ошибка. Введенно не целое число или же такой операции не существует")
        if func == 1:
            autorization(file_name2)
        elif func == 2:
            registration()
        if func == 3:
            return


if __name__ == "__main__":
    main()