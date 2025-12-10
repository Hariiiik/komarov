# main.py
import datetime


# --- МОДУЛЬ 1: MODELS (Моделі даних) ---
class Medicine:
    """Клас, що описує ліки"""

    def __init__(self, name: str, dosage_mg: int, current_stock: int):
        self.name = name
        self.dosage = dosage_mg
        self.stock = current_stock

    def __str__(self):
        return f"{self.name} ({self.dosage}mg) - Залишок: {self.stock}"


# --- МОДУЛЬ 2: SERVICE (Бізнес-логіка) ---
class DispenserService:
    """Клас, що керує логікою видачі ліків"""

    def __init__(self):
        self.inventory = {}  # Словник для зберігання ліків {назва: об'єкт}
        self.logs = []  # Журнал операцій


    def add_medicine(self, medicine: Medicine):
        """Додає нові ліки в диспенсер"""
        if medicine.name in self.inventory:
            raise ValueError(f"Ліки {medicine.name} вже додані.")
        self.inventory[medicine.name] = medicine
        self.logs.append(f"ADDED: {medicine.name} at   {datetime.datetime.now()}")


    def dispense_medicine(self, name: str):
        """Видає одну дозу ліків, якщо вони є в наявності"""
        if name not in self.inventory:
            raise KeyError(f"Ліки {name} не знайдені в диспенсері.")

        med = self.inventory[name]

        if med.stock > 0:
            med.stock -= 1
            log_entry = f"SUCCESS: Видано {name}. Залишилось: {med.stock}"
            self.logs.append(log_entry)
            return log_entry
        else:
            raise ValueError(f"Увага: Запаси {name} вичерпано!")


    def get_inventory_status(self):
        return [str(med) for med in self.inventory.values()]


# --- ДЕМОНСТРАЦІЯ РОБОТИ (Main Execution) ---
if __name__ == "__main__":
    # Ініціалізація системи
    my_dispenser = DispenserService()

    # Створення ліків
    aspirin = Medicine("Aspirin", 500, 2)
    vitamin_c = Medicine("Vitamin C", 1000, 10)

    # Додавання в систему
    my_dispenser.add_medicine(aspirin)
    my_dispenser.add_medicine(vitamin_c)

    print("--- Початковий стан ---")
    print(my_dispenser.get_inventory_status())

    # Спроба видачі
    print("\n--- Видача ліків ---")
    print(my_dispenser.dispense_medicine("Aspirin"))
    print(my_dispenser.dispense_medicine("Aspirin"))

    # Спроба видати, коли ліки закінчились
    try:
        print(my_dispenser.dispense_medicine("Aspirin"))
    except ValueError as e:
        print(f"ПОМИЛКА: {e}")
