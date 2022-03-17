from abc import ABC
from typing import Dict


class Warehouse(ABC):
    def __init__(self, title: str):
        self.title = title
        self.goods: Dict[OfficeEquipment, int] = {}


class Storage(Warehouse):
    def __init__(self, title: str, volume: int):
        super().__init__(title)
        self.volume = volume
        self.volume_used = 0

    def __str__(self) -> str:
        return f'Склад "{self.title}" ({self.volume} м.куб.)'


class Division(Warehouse):
    def __init__(self, title: str):
        super().__init__(title)

    def __str__(self) -> str:
        return f'Подразделение "{self.title}"'


class OfficeEquipment(ABC):
    def __init__(self, brand: str, model: str, size: float):
        self.model = model
        self.brand = brand
        self.size = size


class Printers(OfficeEquipment):
    def __init__(self, brand: str, model: str, size: float, print_type: str, is_color: bool):
        super().__init__(brand, model, size)
        self.print_type = print_type
        self.is_color = is_color

    def __str__(self) -> str:
        return f'Принтер {self.brand} {self.model} ({self.print_type}, {"цветной" if self.is_color else "ч/б"})'


class Scanners(OfficeEquipment):
    def __init__(self, brand: str, model: str, size: float, mode: str, max_dpi: int):
        super().__init__(brand, model, size)
        self.mode = mode
        self.max_dpi = max_dpi

    def __str__(self) -> str:
        return f'Сканер {self.brand} {self.model} ({self.mode}, {self.max_dpi} DPI)'


class Copiers(OfficeEquipment):
    def __init__(self, brand: str, model: str, size: float, print_type: str, is_color: bool, speed: int):
        super().__init__(brand, model, size)
        self.print_type = print_type
        self.is_color = is_color
        self.speed = speed

    def __str__(self) -> str:
        return f'Ксерокс {self.brand} {self.model} ({self.print_type}, {"цветной" if self.is_color else "ч/б"}, {self.speed} страниц/мин.)'


if __name__ == '__main__':
    storage_1 = Storage('Склад №1', 100)
    print(storage_1)  # Склад "Склад №1" (100 м.куб.)
    storage_2 = Storage('Склад №2', 500)
    print(storage_2)  # Склад "Склад №2" (500 м.куб.)

    division_1 = Division('Подразделение №1')
    print(division_1)  # Подразделение "Подразделение №1"
    division_2 = Division('Подразделение №2')
    print(division_2)  # Подразделение "Подразделение №2"

    equipment_1 = Printers('Epson', 'EP-124s', 0.8, 'лазерный', False)
    print(equipment_1)  # Принтер Epson EP-124s (лазерный, ч/б)
    equipment_2 = Scanners('Plustek', 'SmartOffice PN2040', 0.8, 'планшетный А4', 1200)
    print(equipment_2)  # Сканер Plustek SmartOffice PN2040 (планшетный А4, 1200 DPI)
    equipment_3 = Copiers('Panasonic', 'KX-MB763', 1, 'лазерный', True, 18)
    print(equipment_3)  # Ксерокс Panasonic KX-MB763 (лазерный, цветной, 18 страниц/мин.)
