import datetime
import unittest
from unittest import TestCase

from Db_functions import DataBManager


class TestDataBaseUsers(TestCase):

    def setUp(self) -> None:
        self.database = DataBManager()
        self.new_user = {'name': 'Semen',
                         'email': 'chepak.semmy@gmail.com',
                         'registration_time': '2021-02-05 07:21:37'}

        self.updated_user = {'name': 'Andriy',
                             'email': 'chepak.andriy@gmail.com',
                             'registration_time': ' 2021-02-05 07:21:37'}

        self.new_user_info = (4, 'Semen', 'chepak.semmy@gmail.com', datetime.datetime(2021, 2, 5, 7, 21, 37))

        self.updated_user_info = (4, 'Andriy', 'chepak.andriy@gmail.com', datetime.datetime(2021, 2, 5, 7, 21, 37))

        self.users_dict = {'user_id': 2, 'name': 'Semen', 'email': 'semen@gmail.com',
                           'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                           'cart_details': [{'cart_id': 4, 'price': 130, 'product': 'sony'}]}

        self.users_dict_update = {'user_id': 2, 'name': 'Ihor', 'email': 'Ihor@yahoo.com',
                                  'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                                  'cart_details': [{'cart_id': 4, 'price': 300, 'product': 'milk'}]}

        self.info_dict_r = [(8, 4, 300, 'milk'),
                            (9, 4, 300, 'milk'),
                            (10, 4, 300, 'milk'),
                            (11, 4, 130, 'sony')]

        self.info_upd = [(8, 4, 300, 'milk'),
                         (9, 4, 300, 'milk'),
                         (10, 4, 300, 'milk'),
                         (11, 4, 300, 'milk')]

    def test_crud_user_positive(self):
        self.database.create_user(self.new_user)
        self.assertEqual(self.database.read_user_info(4), self.new_user_info)
        self.database.update_user(new_info=self.updated_user, _id=4)
        self.assertEqual(self.database.read_user_info(4), self.updated_user_info)
        self.database.delete_user(_id=4)
        self.assertEqual(self.database.read_user_info(4), None)

    def test_crud_users_negative(self):
        self.database.create_user(self.updated_user)
        self.assertNotEqual(self.database.read_user_info(5), self.new_user_info)
        self.database.update_user(new_info=self.new_user, _id=5)
        self.assertNotEqual(self.database.read_user_info(5), self.updated_user_info)
        self.database.delete_user(_id=5)
        self.assertNotEqual(self.database.read_user_info(4), int)

    def test_crud_cart_positive(self):
        self.database.create_cart(self.users_dict)
        self.assertEqual(self.database.read_cart(4), self.info_dict_r)
        self.database.update_cart(self.users_dict_update)
        self.assertEqual(self.database.read_cart(4), self.info_upd)
        self.database.delete_cart(4)
        self.assertEqual(self.database.read_cart(4), [])

    def test_crud_cart_negative(self):
        self.database.create_cart(self.users_dict)
        self.assertNotEqual(self.database.read_cart(2), self.info_upd)
        self.database.update_cart(self.users_dict_update)
        self.assertNotEqual(self.database.read_cart(2), self.info_dict_r)
        self.database.delete_cart(2)
        self.assertNotEqual(self.database.read_cart(2), self.info_upd)


if __name__ == '__main__':
    unittest.main(verbosity=2)
