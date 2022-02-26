from flask import *
my_api=Flask(__name__)
info_users=[
    {"id":1,
     "name":"Baron",
     "username":"@baron95",
     "fllowes":"5.9k"}
]
@my_api.route('/users')
def hi():
    return jsonify(info_users[0])

my_api.run()