# authentication class for the p.py program with api
BASE_URL = 'https://mak-laid.herokuapp.com/api/v1'
AUTH_URL = BASE_URL + '/auth/login'
USERS_URL = BASE_URL + '/users'

import requests
import json

class Crud:
    def __init__(self):
        self.token = self.get_token_from_file()

    def get_users(self):
        headers = {'Authorization': 'Bearer ' + self.token}
        r = requests.get(USERS_URL, headers=headers)
        return r.json()


    def get_token_from_file(self):
    #    check if token file exists
        try:
            with open('token.txt', 'r') as f:
                self.token = f.read()
                return self.token
        except FileNotFoundError:
            # call login function from Authentication class
            return Authentication().login()

class Authentication:
    def __init__(self):
        self.email = ""
        self.password = ""
        self.token = None

    def login(self):
        # get details from user
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        data = {
            'email': self.email,
            'password': self.password
        }

        # stringify the data
        data = str(data).replace("'", '"')
        # add json to the header
        headers = {'Content-Type': 'application/json'}
        # send the request
        response = requests.post(AUTH_URL, data=data, headers=headers)
        if response.status_code == 200:
            self.token = response.json()['token']

            # save the token to a file
            with open('token.txt', 'w') as f:
                f.write(self.token)
            return True
        return False

    def get_token(self):
        # return token olnly if it is not None
        if self.token is not None:
            return self.token
        return "You are not logged in"

    def get_email(self):
        return self.email

# create a cli to interact with the api
class CLI:
    def __init__(self, auth, crud):
        self.auth = auth
        self.crud = crud

    def run(self):
        while True:
            command = input('> Enter command: ')
            if command == 'exit':
                break
            elif command == 'login':
                if self.auth.login():
                    print('Login successful')
                else:
                    print('Login failed')
            elif command == 'token':
                print(self.auth.get_token())
            elif command == 'email':
                print(self.auth.get_email())
                # add help command
            elif command == 'help':
                print('Available commands:')
                print('login - login to the api')
                print('token - get the token')
                print('email - get the email')
                print('exit - exit the program')
            elif command == 'users':
                print(self.crud.get_users())
            else:
                print('Invalid command')


if __name__ == '__main__':
    auth = Authentication()
    crud = Crud()
    cli = CLI(auth, crud)
    cli.run()

