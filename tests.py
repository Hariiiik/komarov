# test_dispenser.py
import unittest
from main import Medicine, DispenserService


class TestDispenserService(unittest.TestCase):

    def setUp(self):
        """Цей метод запускається перед КОЖНИМ тестом.
        Він створює чисте середовище для тестування."""
        self.service = DispenserService()
        self.test_med = Medicine("TestPill", 100, 2)  # Ліки з запасом



def test_add_medicine_success(self):
    """Тест: Чи успішно додаються ліки в систему"""
    self.service.add_medicine(self.test_med)
    # Перевіряємо, чи є ліки в інвентарі
    self.assertIn("TestPill", self.service.inventory)
    # Перевіряємо, чи правильна кількість
    self.assertEqual(self.service.inventory["TestPill"].stock, 2)


def test_dispense_medicine_success(self):
    """Тест: Чи зменшується кількість ліків при видачі"""
    self.service.add_medicine(self.test_med)

    result = self.service.dispense_medicine("TestPill")

    # Перевіряємо, чи успішне повідомлення
    self.assertIn("SUCCESS", result)
    # Перевіряємо, чи зменшився запас (було 2, стало 1)
    self.assertEqual(self.service.inventory["TestPill"].stock, 1)


def test_dispense_medicine_empty_stock(self):
    """Тест: Чи виникає помилка, коли ліки закінчились"""
    zero_stock_med = Medicine("EmptyPill", 100, 0)
    self.service.add_medicine(zero_stock_med)

    # Очікуємо помилку ValueError при спробі видачі
    with self.assertRaises(ValueError):
        self.service.dispense_medicine("EmptyPill")


def test_dispense_medicine_not_found(self):
    """Тест: Спроба видати неіснуючі ліки"""
    with self.assertRaises(KeyError):
        self.service.dispense_medicine("NonExistentPill")


if __name__ == '__main__':
    unittest.main()