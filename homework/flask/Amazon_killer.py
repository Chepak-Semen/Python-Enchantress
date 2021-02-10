from datetime import datetime

from flask import Flask, request

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
user_counter = 1


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amazon_killer.route('/users', methods=["POST"])
def get_users(user_id: int):
    user = USERS_DATABASE


@amazon_killer.route('/users', methods=["POST"])
def update_users():
    pass

@amazon_killer.route('/users', methods=["POST"])
def delete_users():
    pass



if __name__ == '__main__':
    amazon_killer.run(debug=True)
