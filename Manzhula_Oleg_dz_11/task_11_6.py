from abc import ABC
from typing import Dict


class WarehouseException(Exception):
    message = 'Ошибка выполнения складской операции'

    def __init__(self, message: str):
        if message:
            self.message = message

    def __str__(self):
        return f'!!! Ошибка выполнения складской операции:\n{self.message}'


class Warehouse(ABC):
    """
    Абстрактный класс описания мест храниения (учета) офисной техники
    """
    def __init__(self, title: str):
        if not title.strip():
            raise WarehouseException('Наименование склада не может быть пустым')

        self.title = title
        self.goods: Dict[OfficeEquipment, int] = {}

    def print_info(self):
        if len(self.goods):
            sep = '\n'
            print(f'На {self} хранится:')
            print(f'{sep.join(list(str(key) + ": " + str(value) + " шт." for key, value in self.goods.items()))}')
            if isinstance(self, Storage):
                print(f'(использовано {self.volume_used} м.куб. из {self.volume}; '
                      f'осталось: {self.free_volume} м.куб.)')
        else:
            print(f'{self} не используется')


class Storage(Warehouse):
    """
    Класс описания Складов
    Имеет наименование и хранит перечень и количество техники, которая на нем числится
    Имеет ограничения по объему хранения
    """
    def __init__(self, title: str, volume: int):
        if not isinstance(volume, int):
            raise WarehouseException('Неверный тип значения объема склада - объем склада должен быть числом')

        super().__init__(title)
        self.volume = volume
        self.volume_used = 0

    def __str__(self) -> str:
        return f'Склад "{self.title}" ({self.volume} м.куб.)'

    @property
    def free_volume(self):
        return self.volume - self.volume_used


class Division(Warehouse):
    """
    Класс описания Подразделений
    Имеет наименование и хранит перечень и количество техники, которая на нем числится
    НЕ имеет ограничения по объему хранения
    """
    def __init__(self, title: str):
        super().__init__(title)

    def __str__(self) -> str:
        return f'Подразделение "{self.title}"'


class OfficeEquipment(ABC):
    """
    Абстрактный класс описания офисной техники
    """
    def __init__(self, brand: str, model: str, size: float):
        self.model = model
        self.brand = brand
        self.size = size

    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, int):
            raise WarehouseException('Неверный тип значения количества - количество должно быть числом')

        if not quantity > 0:
            raise WarehouseException(f'Количество должно быть больше 0')

    def receive_to_warehouse(self, warehouse: Warehouse, quantity: int):
        OfficeEquipment.validate_quantity(quantity)

        try:
            if isinstance(warehouse, Storage):
                if warehouse.volume_used + self.size * quantity > warehouse.volume:
                    raise WarehouseException(f'На {warehouse} недостаточно места для принятия {quantity} шт. {self}: '
                          f'требуется {self.size * quantity} м.куб, '
                                             f'доступно - {warehouse.volume - warehouse.volume_used}')
                warehouse.volume_used += self.size * quantity

            warehouse.goods.setdefault(self, 0)
            warehouse.goods[self] += quantity
        except WarehouseException as err:
            print(err)

    def move_from_warehouse(self, warehouse: Warehouse, quantity: int):
        OfficeEquipment.validate_quantity(quantity)

        stock = warehouse.goods.get(self, 0)
        try:
            if quantity > stock:
                raise WarehouseException(f'На {warehouse} недостаточно {self} для перемещения: '
                                         f'требуется {quantity} шт., в наличии {stock} шт.')

            if isinstance(warehouse, Storage):
                warehouse.volume_used -= self.size * quantity

            warehouse.goods[self] -= quantity
            if not warehouse.goods[self]:
                warehouse.goods.pop(self)
        except WarehouseException as err:
            print(err)

    def move_between(self, warehouse_from: Warehouse, warehouse_to: Warehouse, quantity: int):
        OfficeEquipment.validate_quantity(quantity)

        if warehouse_from == warehouse_to:
            # перемещение внутри одного и того же склада/подразделения == ничего делать не надо
            return

        self.move_from_warehouse(warehouse_from, quantity)
        self.receive_to_warehouse(warehouse_to, quantity)


class Printers(OfficeEquipment):
    """
    Класс описания офисной техники типа Принтер
    Имеет бренд, модель и объемный размер единицы техники
    А также: тип принтера (напр. 'лазерный' или 'струйный') и признак является ли принтер цветным
    """
    def __init__(self, brand: str, model: str, size: float, print_type: str, is_color: bool):
        super().__init__(brand, model, size)
        self.print_type = print_type
        self.is_color = is_color

    def __str__(self) -> str:
        return f'Принтер {self.brand} {self.model} ({self.print_type}, {"цветной" if self.is_color else "ч/б"})'


class Scanners(OfficeEquipment):
    """
    Класс описания офисной техники типа Сканер
    Имеет бренд, модель и объемный размер единицы техники
    А также: тип (напр. 'планшетный А4' или 'строчный') и макс. разрешение сканирования (DPI)
    """
    def __init__(self, brand: str, model: str, size: float, mode: str, max_dpi: int):
        super().__init__(brand, model, size)
        self.mode = mode
        self.max_dpi = max_dpi

    def __str__(self) -> str:
        return f'Сканер {self.brand} {self.model} ({self.mode}, {self.max_dpi} DPI)'


class Copiers(OfficeEquipment):
    """
    Класс описания офисной техники типа Ксерокс
    Имеет бренд, модель и объемный размер единицы техники
    А также: тип печати (напр. 'лазерный' или 'струйный'), признак есть ли цветная печать и производительность (л./мин)
    """
    def __init__(self, brand: str, model: str, size: float, print_type: str, is_color: bool, speed: int):
        super().__init__(brand, model, size)
        self.print_type = print_type
        self.is_color = is_color
        self.speed = speed

    def __str__(self) -> str:
        return f'Ксерокс {self.brand} {self.model} ({self.print_type}, {"цветной" if self.is_color else "ч/б"}, ' \
               f'{self.speed} страниц/мин.)'


if __name__ == '__main__':
    print('-- Создание складов:')
    storage_1 = Storage('Склад №1', 100)
    print(storage_1)
    storage_2 = Storage('Склад №2', 500)
    print(storage_2)

    print('\n-- Создание подразделений:')
    division_1 = Division('Подразделение №1')
    print(division_1)
    division_2 = Division('Подразделение №2')
    print(division_2)

    print('\n-- Создание разных видов оргтехники:')
    equipment_1 = Printers('Epson', 'EP-124s', 0.8, 'лазерный', False)
    print(equipment_1)  # Принтер Epson EP-124s (лазерный, ч/б)
    equipment_2 = Scanners('Plustek', 'SmartOffice PN2040', 0.8, 'планшетный А4', 1200)
    print(equipment_2)  # Сканер Plustek SmartOffice PN2040 (планшетный А4, 1200 DPI)
    equipment_3 = Copiers('Panasonic', 'KX-MB763', 1, 'лазерный', True, 18)
    print(equipment_3)  # Ксерокс Panasonic KX-MB763 (лазерный, цветной, 18 страниц/мин.)

    print('\n-- Добавление новых позиций на склад:')
    equipment_1.receive_to_warehouse(storage_1, 10)  # добавляем новую позицию на склад
    storage_1.print_info()
    print()
    equipment_2.receive_to_warehouse(storage_1, 5)  # добавляем новую позицию на склад
    storage_1.print_info()

    print('\n-- Дополнение существующих позиций на складе:')
    equipment_1.receive_to_warehouse(storage_1, 3)  # добавляем количество по уже существующей позиции на склад
    storage_1.print_info()
    print()
    equipment_2.receive_to_warehouse(storage_1, 8)  # добавляем количество по уже существующей позиции на склад
    storage_1.print_info()
    print()
    storage_2.print_info()

    print('\n-- Ошибка переполнения склада:')
    equipment_3.receive_to_warehouse(storage_1, 100)  # ошибка переполнения склада
    storage_1.print_info()

    print('\n-- Частичное перемещение существующих позиций со склада на подразделение:')
    equipment_1.move_between(storage_1, division_1, 5)
    storage_1.print_info()
    print()
    division_1.print_info()

    print('\n-- Полное перемещение существующих позиций со склада на подразделение:')
    equipment_2.move_between(storage_1, division_1, 13)
    storage_1.print_info()
    print()
    division_1.print_info()

    print('\n-- Ошибка нехватки остатка для перемещения существующей позиции со склада на подразделение:')
    equipment_2.move_between(storage_1, division_1, 13)
    storage_1.print_info()
    print()
    division_1.print_info()

    print('\n-- Списание существующей позиции с подразделения:')
    equipment_1.move_from_warehouse(division_1, 2)
    division_1.print_info()
