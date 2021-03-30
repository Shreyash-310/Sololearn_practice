from UT import Validator

username = 'Shreyash'
validator = Validator()
if validator.username_is_valid(username):
    print('username is valid')
else:
    print('username is invalid')
