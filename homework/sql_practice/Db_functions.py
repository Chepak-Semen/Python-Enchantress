import logging

import psycopg2

# set basicConfig for logging
logging.basicConfig(
    filename='DBloggers.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


class DatabaseConnection:

    def __enter__(self):
        self.connection = psycopg2.connect(dbname="chepak_s",
                                           user="chepak_s",
                                           password='999',
                                           host='localhost',
                                           port='5432'
                                           )

        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
        cursor = self.connection.cursor()

        logging.info(f'DB connecting successfully')
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

        return False


class DataBManager:

    @staticmethod
    def create_user(user_info: dict):
        """
        method create a new  record in table 'users'
        """
        with DatabaseConnection() as cursor:
            cursor.execute("""INSERT INTO users 
                            (name, email, registration_time)
                            VALUES  
                            (%(name)s, %(email)s, %(registration_time)s)""", user_info)

        logging.info(f'Adding new user {user_info["name"]} | {user_info["email"]}')

    @staticmethod
    def read_user_info(_id: int):
        """
        method show information about user with _id in table 'users'
        """
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (_id,))
            info = cursor.fetchone()
            return info

    @staticmethod
    def update_user(new_info: dict, _id: int):
        """
        method rewrite a user record in table 'users' for column {
                                                                name,
                                                                email,
                                                                registration_time
                                                              }
        """
        with DatabaseConnection() as cursor:
            cursor.execute(f"""UPDATE users SET 
                            name = %(name)s,
                            email = %(email)s, 
                            registration_time = %(registration_time)s
                            WHERE 
                            id = {_id}""", new_info)

        logging.info(f'Updating user _id | {_id}')

    @staticmethod
    def delete_user(_id: int):
        """
        method delete information about user with _id in table 'users'
        """
        with DatabaseConnection() as cursor:
            cursor.execute('DELETE FROM users WHERE id = %s', (_id,))

        logging.warning(f'Delete user with id {_id}')

    @staticmethod
    def create_cart(cart: dict):
        """
        method create a new record in table 'cart' & in DB 'cart_details'
        """
        with DatabaseConnection() as cursor:
            cursor.execute("""INSERT INTO cart (creation_time, user_id) 
                            VALUES 
                            (%(creation_time)s, %(user_id)s)""", cart)

            cursor.executemany("""INSERT INTO cart_details (cart_id, price, product) 
                                VALUES 
                                (%(cart_id)s, %(price)s, %(product)s)""", cart["cart_details"])

        logging.info(f'Adding new cart {cart["cart_details"]}')

    @staticmethod
    def update_cart(cart: dict):
        """
        method rewrite a user record in table 'cart' for column {
                                                                registration_time
                                                                }
        and in table 'cart_details' for column {
                                                price
                                                product
                                                }
        """
        with DatabaseConnection() as cursor:
            cursor.executemany(f"""UPDATE cart SET 
                            creation_time = '{cart["creation_time"]}' 
                            WHERE 
                            user_id = {cart['user_id']}""", cart)

            cursor.executemany(f"""UPDATE cart_details SET 
                                price = %(price)s, product = %(product)s
                                WHERE cart_id = %(cart_id)s""", cart["cart_details"], )
        logging.info(f' update cart | {cart["cart_details"]}')

    @staticmethod
    def read_cart(_id: int):
        """
        method show information about user with _id in table 'cart_details'
        """
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT * FROM cart_details WHERE cart_id = %s', (_id,))
            return cursor.fetchall()

    @staticmethod
    def delete_cart(_id: int):
        """
        method delete information about cart with _id in table 'cart'&'cart_details'
        """
        with DatabaseConnection() as cursor:
            cursor.execute('DELETE FROM cart_details WHERE cart_id = %s', (_id,))
            cursor.execute('DELETE FROM cart WHERE id = %s', (_id,))
        logging.warning(f'Delete cart with id {_id}')


if __name__ == '__main__':
    users_dict = {'user_id': 1, 'name': 'Semen', 'email': 'semen@gmail.com',
                  'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                  'cart_details': [{'cart_id': 1, 'price': 130, 'product': 'sony'}]}

    users_dict_update = {'user_id': 1, 'name': 'Ihor', 'email': 'Ihor@yahoo.com',
                         'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                         'cart_details': [{'cart_id': 1, 'price': 300, 'product': 'milk'}]}

    d = DataBManager()
    print(d.read_user_info(4))
    d.create_cart(users_dict)
