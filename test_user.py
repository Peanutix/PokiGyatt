"""
Player types:
- User
- Opponent
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'Username: {self.username}, Password: {self.password}'

