import unittest
import math


# ФУНКЦИИ ДЛЯ ВЫЧИСЛЕНИЯ ОБЪЕМОВ
def volume_cube(a):
    """Объем куба: сторона * сторона * сторона"""
    return a * a * a


def volume_sphere(r):
    """Объем шара: (4/3) * пи * радиус * радиус * радиус"""
    return (4 / 3) * math.pi * r * r * r


def volume_cylinder(r, h):
    """Объем цилиндра: пи * радиус * радиус * высота"""
    return math.pi * r * r * h


# ТЕСТЫ
class TestVolumes(unittest.TestCase):

    #  ТЕСТЫ ДЛЯ КУБА
    def test_cube_side_3(self):
        """Куб со стороной 3: 3*3*3 = 27"""
        result = volume_cube(3)
        self.assertEqual(result, 27)

    def test_cube_side_5(self):
        """Куб со стороной 5: 5*5*5 = 125"""
        result = volume_cube(5)
        self.assertEqual(result, 125)

    def test_cube_side_10(self):
        """Куб со стороной 10: 10*10*10 = 1000"""
        result = volume_cube(10)
        self.assertEqual(result, 1000)

    def test_cube_side_2_5(self):
        """Куб со стороной 2.5 (дробное число): 2.5*2.5*2.5 = 15.625"""
        result = volume_cube(2.5)
        self.assertEqual(result, 15.625)

    # ТЕСТЫ ДЛЯ ШАРА
    def test_sphere_radius_1(self):
        """Шар с радиусом 1: (4/3)*π*1*1*1"""
        result = volume_sphere(1)
        # Используем math.pi для точного сравнения
        self.assertAlmostEqual(result, (4 / 3) * math.pi, places=5)

    def test_sphere_radius_2(self):
        """Шар с радиусом 2: (4/3)*π*8"""
        result = volume_sphere(2)
        expected = (4 / 3) * math.pi * 8
        self.assertAlmostEqual(result, expected, places=5)

    def test_sphere_radius_3(self):
        """Шар с радиусом 3: (4/3)*π*27"""
        result = volume_sphere(3)
        expected = (4 / 3) * math.pi * 27
        self.assertAlmostEqual(result, expected, places=5)

    def test_sphere_radius_1_5(self):
        """Шар с радиусом 1.5 (дробный)"""
        result = volume_sphere(1.5)
        expected = (4 / 3) * math.pi * (1.5 ** 3)
        self.assertAlmostEqual(result, expected, places=5)

    #  ТЕСТЫ ДЛЯ ЦИЛИНДРА
    def test_cylinder_radius_1_height_1(self):
        """Цилиндр r=1, h=1: π*1*1 = π"""
        result = volume_cylinder(1, 1)
        self.assertAlmostEqual(result, math.pi, places=5)

    def test_cylinder_radius_2_height_5(self):
        """Цилиндр r=2, h=5: π*4*5 = 20π"""
        result = volume_cylinder(2, 5)
        expected = math.pi * 4 * 5  # 20 * π
        self.assertAlmostEqual(result, expected, places=5)

    def test_cylinder_radius_3_height_4(self):
        """Цилиндр r=3, h=4: π*9*4 = 36π"""
        result = volume_cylinder(3, 4)
        expected = math.pi * 9 * 4
        self.assertAlmostEqual(result, expected, places=5)

    def test_cylinder_radius_2_5_height_3(self):
        """Цилиндр с дробными числами: r=2.5, h=3"""
        result = volume_cylinder(2.5, 3)
        expected = math.pi * (2.5 ** 2) * 3
        self.assertAlmostEqual(result, expected, places=5)


#  ЗАПУСК ТЕСТОВ
if __name__ == '__main__':
    unittest.main()