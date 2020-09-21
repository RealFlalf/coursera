import unittest
from course1.week4_file import File

class Car_test(unittest.TestCase):
    def test_create_and_write(self):
        path_to_file = 'some_filename'
        file_obj = File(path_to_file)
        file_obj.write('some text')
        file_obj.write('other text')
        self.assertEqual(file_obj.read(), 'other text')

    def test_add(self):
        path_to_file = 'some_filename'
        file_obj_1 = File(path_to_file + '_1')
        file_obj_2 = File(path_to_file + '_2')
        file_obj_1.write('line 2\n')
        file_obj_2.write('line 1\n')
        new_file_obj = file_obj_1 + file_obj_2
        self.assertTrue(isinstance(new_file_obj, File))