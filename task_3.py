books = []
cathalog_books = []


class Book:
    def __init__(self, title, authors, year, publisher, number_of_pages):
        self.title = title
        self.authors = authors
        self.year = year
        self.publisher = publisher
        self.number_of_pages = number_of_pages

    def checker(self):                # геттер класса Book
        return self.title, self.authors, self.year, self.publisher, self.number_of_pages


class Cathalog_Book(Book):
    def __init__(self, title, authors, year, publisher, number_of_pages, id, quantity, instances, *list_of_readers):
        Book.__init__(title, authors, year, publisher, number_of_pages)
        self.id = id
        self.quantity = quantity
        self.instances = instances
        self.list_of_readers = list_of_readers

    def info(self):
        print(self.title, self.authors, self.year, self.publisher, self.number_of_pages, self.id, self.quantity, self.instances, self.list_of_readers)
        print(*self.list_of_readers)

    def delete_book(self):             # геттер класса Cathalog_Book
        return self.title, self.authors, self.year, self.publisher, self.number_of_pages, self.id, self.quantity, self.instances, self.list_of_readers


class Menu:      # класс, отвечающий за меню программы
    def start(self): # приветствие и дальнейшие инструкции
        print("Добро пожаловать в электронную библиотеку!")
        print("Выберите номер желаемой операции (1 - 10):")
        menu.main_list()

    def main_list(self): # инструкции по использованию программы
        print("1. Создать книгу.")
        print("2. Удалить книгу.")
        print("3. Добавить книгу в каталог.")
        print("4. Удалить книгу из каталога.")
        print("5. Вывод информации по книге и читателям, взявшим книгу.")
        print("6. Поиск книги в каталоге по названию и по автору с выдачей идентификатора.")
        print("7. Выдача книги читателю.")
        print("8. Возврат книги читателем.")
        print("9. Вывод списка читателей, не вернувших книги в течение года.")
        print("10. Завершить сеанс.")
        menu.operator()

    def operator(self):
        n = int(input("Выберите номер желаемой операции (1 - 10): "))
        if n < 1 or n > 10:
            print('Ошибка, введите корректный номер операции')
            n = int(input("Выберите номер желаемой операции (1 - 10): "))
            menu.operator()
        if n == 1:
            menu.point_1() # вызов метода "Создание книги"
        elif n == 2:
            menu.point_2() # вызов метода "Удаление книги"
        elif n == 3:
            menu.point_3() # вызов метода "Добавление книги в каталог"
        elif n == 4:
            menu.point_4() # вызов метода "Удаление книги из каталога по id"
        elif n == 5:
            menu.point_5() # вызов метода "Вывод информации о книге по id"
        elif n == 6:
            menu.point_6() # вызов метода "Выдача id по автору и названию"
        elif n == 7:
            menu.point_7() # вызов метода "Выдача книги читателю"
        elif n == 8:
            menu.point_8() # вызов метода "Возврат книги читателем"
        elif n == 9:
            menu.point_9() # вызов метода "Вывод читателей, не вернувших книгу в течение года"
        elif n == 10:
            menu.point_10() # вызов метода "Окончание работы программы"

    def point_1(self):  # Создание книги
        global books
        title = input('Введите название книги: ')
        authors = input('Укажите автора (авторов) книги: ')
        year = int(input('Укажите год выпуска книги: '))
        publisher = input('Укажите издательство книги: ')
        number_of_pages = int(input('Укажите количество страниц в книге: '))
        new_book = Book(title, authors, year, publisher, number_of_pages)
        books.append(new_book)
        menu.main_list()
        menu.operator()

    def point_2(self):  # Удаление книги
        global books
        title = input('Введите название книги, которую хотите удалить: ')
        authors = input('Укажите автора книги, которую хотите удалить: ')
        year = int(input('Укажите год выпуска книги, которую хотите удалить: '))
        publisher = input('Укажите издательство книги, которую хотите удалить: ')
        number_of_pages = int(input('Укажите количество страниц в книге, которую хотите удалить: '))
        for i in range(len(books)):
            if books[i].checker() == (title, authors, year, publisher, number_of_pages):
                books.pop(i)
                break
        menu.main_list()
        menu.operator()

    def point_3(self): # Добавление книги в каталог
        global cathalog_books
        title = input('Введите название книги, которую хотите добавить в каталог: ')
        authors = input('Укажите автора (авторов) книги, которую хотите добавить в каталог: ')
        year = int(input('Укажите год выпуска книги, которую хотите добавить в каталог: '))
        publisher = input('Укажите издательство книги, которую хотите добавить в каталог: ')
        number_of_pages = int(input('Укажите количество страниц в книге, которую хотите добавить в каталог: '))
        for i in range(len(books)):
            if books[i].checker() == (title, authors, year, publisher, number_of_pages):
                id = int(input('Укажите id книги: '))
                quantity = int(input('Укажите общее количество экземпляров: '))
                instances = int(input('Укажите количество экземпляров в наличии: '))
                list_of_readers = []
                n_readers = quantity - instances
                print('Перечислите через запятую имя и дату выдачи книги (Пример: Иванов Иван, 01.04.2022) для каждого из', n_readers, 'читателей.')
                for j in range(n_readers):
                    list_of_readers.append(input())
                new_cathalog_book = Cathalog_Book(title, authors, year, publisher, number_of_pages, id, quantity, instances, *list_of_readers)
                cathalog_books.append(new_cathalog_book)
                break
            else:
                print('Ошибка! Сначала необходимо создать эту книгу.')
        menu.main_list()
        menu.operator()

    def point_4(self): # Удаление книги из каталога по id
        id = int(input('Введите id книги, которую хотите удалить: '))
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[5] == id:
                cathalog_books.pop(i)
                break
        menu.main_list()
        menu.operator()

    def point_5(self): # Вывод информации о книге по id
        id = int(input('Укажите id интересующей Вас книги: '))
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[5] == id:
                cathalog_books[i].info()
                break
        menu.main_list()
        menu.operator()

    def point_6(self): # Выдача id по автору и названию
        authors = input('Укажите автора интересующей Вас книги: ')
        name = int(input('Введите название книги, которую Вас интересует: '))
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[0] == name and cathalog_books[i].delete_book()[1] == authors:
                print(cathalog_books[i].delete_book()[5])
                break
        menu.main_list()
        menu.operator()

    def point_7(self): # Выдача книги читателю
        id = int(input('Укажите id интересующей Вас книги: '))
        name = input('Укажите свое имя: ')
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[5] == id:
                if cathalog_books[i].delete_book()[7] > 0:
                    cathalog_books[i].delete_book()[7] -= 1
                    cathalog_books[i].delete_book()[8].append(name + ', ' + '04.04.2022')
                else:
                    print('Приносим свои извинения, данной книги на данный момент нет в наличии.')
            else:
                print('Книга с указанным id отсутствует в библиотеке.')
        menu.main_list()
        menu.operator()

    def point_8(self): # Возврат книги читателем
        id = int(input('Укажите id книги, которую хотите вернуть: '))
        name = input('Укажите свое имя: ')
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[5] == id:
                cathalog_books[i].delete_book()[7] += 1
                for j in range(len(cathalog_books[i].delete_book()[8])):
                    if (cathalog_books[i].delete_book()[8][j].split(', ')[0]) == name:
                        cathalog_books[i].delete_book()[8].pop(j)
                        break
                    else:
                        print('Ошибка, ваше имя не найдено в базе. Убедитесь в правильности указанных данных.')
            else:
                print('Книга с указанным id отсутствует в библиотеке.')
        menu.main_list()
        menu.operator()

    def point_9(self): # Вывод читателей, не вернувших книгу в течение года
        id = int(input('Укажите id интересующей Вас книги: '))
        for i in range(len(cathalog_books)):
            if cathalog_books[i].delete_book()[5] == id:
                for j in range(len(cathalog_books[i].delete_book()[8])):
                    if 2022 - int(cathalog_books[i].delete_book()[8][j].split(', ')[1].split('.')[2]) > 1:
                        print(cathalog_books[i].delete_book()[8][j])
                    elif 2022 - int(cathalog_books[i].delete_book()[8][j].split(', ')[1].split('.')[2]) == 1:
                        if 4 - int(cathalog_books[i].delete_book()[8][j].split(', ')[1].split('.')[1]) > 0:
                            print(cathalog_books[i].delete_book()[8][j])
                        elif 4 - int(cathalog_books[i].delete_book()[8][j].split(', ')[1].split('.')[1]) == 0:
                            if 4 - int(cathalog_books[i].delete_book()[8][j].split(', ')[1].split('.')[0]) > 0:
                                print(cathalog_books[i].delete_book()[8][j])
            else:
                print('Книга с указанным id отсутствует в библиотеке.')
        menu.main_list()
        menu.operator()

    def point_10(self): # Окончание работы программы
        print('Спасибо, что пользуетесь нашей библиотекой, до новых встреч!')



menu = Menu()  # запуск программы с помощью объекта класса меню
menu.start()