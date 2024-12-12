import main
from operator import itemgetter
import unittest


class TestMainMethods(unittest.TestCase):
    def test_first_task_method(self):
        test_list = [('first', 1999_45, "BMSTU_RK1"), ('forth', 1924_24, "BMSTU_IU3"), ('second', 2024_352,"BMSTU_L3")]
        result = main.first_task(test_list)
        reference = sorted(test_list, key=itemgetter(2))
        self.assertEqual(result, reference)

    def test_second_task_method(self):
        test_list = [("Pen", 1999_43, "John" ),
                    ("Car", 1945_21, "Alex"),
                    ("Stol", 1000_61, "Alex"),
                    ("Laptop", 1943_38, "Alex"),
                    ("Carry", 1942_47, "John"),
                    ("Lamp", 1999_42, "Jean")]
        result = main.second_task(test_list)
        reference = [('Alex', 3), ('John', 2), ('Jean', 1)]
        self.assertEqual(result, reference)

    def test_third_method(self):
        test_list = [("Soska", 1999_43,1),
                    ("Stul", 1945_214,2),
                    ("Stol", 1000_61,3),
                    ("Podik", 1943_38, 3),
                    ("Girya", 1942_474, 1),
                    ("Dver", 1999_4245, 1)]
        result = main.third_task(test_list, '4')
        reference = [('Stul', 2), ('Girya', 1)]
        self.assertEqual(result, reference)