class Tache:
    def __init__(self, title, description, status):
        self.__title = title
        self.__description = description
        self.__status = status

    def set__title(self, title):
        self.__title = title

    def get__title(self):
        return self.__title
    
    def set__description(self, description):
        self.__description = description

    def get__description(self):
        return self.__description

    def set__status(self):
        if self.get__status() == 1:
            self.__status = 0
        else:
            self.__status = 1


    def get__status(self):
        return self.__status

class ListDeTaches:
    def __init__(self, to_do_list: list):
        self.__to_do_list = to_do_list

    def set__to_do_list(self, to_do_list):
        self.__to_do_list = to_do_list

    def get__to_do_list(self):
        return self.__to_do_list

    def add_task(self, task_class):
        self.__to_do_list.append(task_class)

    def delete_task(self, task_class):
        self.__to_do_list.remove(task_class)

    def mark_as_done(self, task_class):
        if task_class.get__status() == 1:
            print(f"La {task_class.get__title()} est terminée")

    def show_to_do_list(self):
        for task in self.__to_do_list:
            print([task.get__title(), task.get__description(), task.get__status()])

    def filter_list(self):
        list_finished = []
        list_running = []
        for task in self.__to_do_list:
            if task.get__status() == 1:
                list_finished.append([task.get__title(), task.get__description(), task.get__status()])
            else:
                list_running.append([task.get__title(), task.get__description(), task.get__status()])

        print("Tâches terminées:")
        print(list_finished)
        print("Tâches en cours:")
        print(list_running)

tache1 = Tache('nettoyer', 'prendre son eponde et frotter', True)
tache2 = Tache('faire les courses', 'aller au supermarché et acheter les produits nécessaires', False)
tache3 = Tache('étudier', 'consacrer du temps à la lecture et à la compréhension des cours', False)
tache4 = Tache('arroser les plantes', 'prendre un arrosoir et arroser chaque plante selon ses besoins', True)
tache5 = Tache('préparer le dîner', 'choisir une recette, acheter les ingrédients et cuisiner le repas', False)

list_task = ListDeTaches([])

list_task.add_task(tache1)
list_task.add_task(tache2)
list_task.add_task(tache3)
list_task.add_task(tache4)
list_task.add_task(tache5)

list_task.show_to_do_list()
list_task.filter_list()