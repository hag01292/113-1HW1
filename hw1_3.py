# test_hw1_3.py
import unittest

def convert_temperature(celsius: float) -> float:
 """將攝氏溫度轉換為華氏溫度"""
 return (celsius * 9/5) + 32

class TestTemperatureConversion(unittest.TestCase):

 def test_freezing_point(self):
    self.assertEqual(convert_temperature(0), 32, "冰點轉換失敗")

 def test_boiling_point(self):
    self.assertEqual(convert_temperature(100), 212, "沸點轉換失敗")

 def test_negative_temperature(self):
    self.assertEqual(convert_temperature(-40), -40, "負溫度轉換失敗")

 def test_fractional_temperature(self):
    self.assertAlmostEqual(convert_temperature(36.6), 97.88, places=2, msg="體溫轉換失敗")

if __name__ == '__main__':
 unittest.main()