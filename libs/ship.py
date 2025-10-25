class ship:
    # Статичные свойства класса
    num_count = 0 # Общее число кораблей

    # Конструктор класса
    # Входные параметры:
    #  type - тип корабля (число палуб)
    def __init__(self, type):
        ship.num_count += 1 # Увеличиваем общее число созданных кораблей
        self._damage = 0 # Уровень повреждения корбаля (от 0 до 100%)
        self._type = type # Тип корабля

        # Отладочное сообщение (временно)
        print(f"Повреждение коробля - {self._damage}, всего кораблей - {ship.num_count}")
        print(f"количество клеток у коробля - {self._type}")


    # Геттер для damage
    @property
    def damage(self):
        return self._damage

    # Сеттер для damage
    @damage.setter
    def damage(self, value):
        self._damage = value
   
   
    # Геттер для type
    @property
    def type(self):
        return self._type