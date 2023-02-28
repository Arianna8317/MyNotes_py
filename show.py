class Show:
    def greeting(self):
        print("Приложение ЗАМЕТКИ")

    def main_menu(self):
        print("Выберите, что необходимо сделать с заметками:\n"
              "\t1. Добавить новую\n"
              "\t2. Работать с существующей \n"
              "\t3. Показать все\n"
              "\t4. Сохранить \n"
              "\t0. Выход")

    def secondary_menu(self):
        print("Что вы хотите сделать? Выберите пункт меню:\n"
              "\t1. Прочитать заметку\n"
              "\t2. Изменить заметку\n"
              "\t3. Удалить заметку\n")
    def saving_message(self):
        print("Заметки сохранены в файл!")

    def error_message(self):
        print("Некорректный ввод")
    def not_found(self):
        print("Такого значения не найдено. Попробуйте еще раз.")


    def note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)

    def total(self, count):
        print(f"Всего заметок: {count}\n")

    def inform(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def input_name(self):
        return input(f"Введите название заметки:")

    def input_text(self):
        return input(f"Текст заметки:")

    def edit(self, note):
        note.set_text(self.input_text())
        note.update()
        self.inform('edit')

    def input_menu_item(self, limit, preset):
        endings = {'id': 'заметки', 'menu': 'пункта меню'}
        number = 0
        while True:
            try:
                number = int(input(f"Введите номер {endings[preset]}: "))
            except ValueError:
                self.error_message()
                continue
            if 0 <= number <= limit:
                break
            else:
                self.not_found()
        return number

    def exit_message(self):
        print("Работа закончена!")