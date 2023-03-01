import pickle
from note import Note
from show import Show


class Notebook:
    __notes = []
    __show = Show()
    __index = 0
    __indexes = [] # стек индексов

    def __init__(self):
        try:
            with open('notebook.pkl', 'rb') as file:
                self.__notes = pickle.load(file)
                self.__index = len(self.__notes)
            with open('indexes.pkl', 'rb') as file:
                self.__indexes = pickle.load(file)
        except FileNotFoundError:
            self.__notes = []
            self.__show = Show()
            self.__index = 0
            self.__indexes = []



    def add(self):
        note = Note()
        note.set_name(self.__show.input_name())
        note.set_text(self.__show.input_text())
        note.update()
        if len(self.__indexes) == 0:
            note.set_id(self.__index)
        else:
            note.set_id(self.__indexes.pop())
        self.__notes.append(note)
        self.__index = len(self.__notes)
        self.__show.inform('add')

    def delete(self, note):
        self.__indexes.append(note.get_id())
        self.__notes.remove(note)
        if len(self.__notes) == 0:
            self.__indexes.clear()
        self.__show.inform('del')


    def show_all(self):
        self.__show.total(len(self.__notes))
        for note in self.__notes:
            self.__show.note(note)

    def secondary(self):
        menu_items =  {1: self.__show.note,
                     2: self.__show.edit,
                     3: self.delete}
        flag = False
        self.__show.secondary_menu()
        choice = self.__show.input_menu_item(len(menu_items.keys()), 'menu')
        value = self.__show.input_menu_item(self.__index, 'id')
        for note in self.__notes:
            if note.get_id() == value:
                menu_items[choice](note)
                flag = True
        if not flag:
            self.__show.not_found()

    def save(self):
        with open('notebook.pkl', 'wb') as file:
            pickle.dump(self.__notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes.pkl', 'wb') as file:
            pickle.dump(self.__indexes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.__show.saving_message()



