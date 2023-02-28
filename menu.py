from notebook import Notebook
from show import Show


class Menu:
    __show = Show()
    __notebook = Notebook()
    __menu_items = {0: __show.exit_message, 1: __notebook.add, 2: __notebook.sort_id, 3: __notebook.read_all,
                  4: __notebook.save}
    def run(self):
        while(True):
            print (" \n З  А  М  Е  Т  К  И\n")
            self.__show.main_menu()
            item = self.__show.input_menu_item(len(self.__menu_items.keys()), 'menu')
            self.__menu_items[item]()
            if item == 0:
                 break
        