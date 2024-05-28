import tkinter as tk
import customtkinter as ctk
from csv import DictReader


class Login:

    def __init__(self):
        self.start_up_window = tk.Tk()
        self.start_up_window.config(bg='#86cf9a')
        self.start_up_window.geometry('700x400') # 500x300
        # self.start_up_window.minsize(500, 300)
        # self.start_up_window.maxsize(500, 300)
        self.entry_screen = tk.Frame(self.start_up_window, bg='#86cf9a')
        self.start_up_window.title('Login')

        self.welcome_label = tk.Label(self.entry_screen,
                                      text='Welcome to Pokes', font='Courier 35 bold',
                                      padx=30, pady=30,
                                      bg='#86cf9a')
        self.welcome_label.pack()

        self.existing_player = ctk.CTkButton(self.entry_screen,
                                             text='Login',
                                             command=self.existing_player_screen)
        self.existing_player.pack()

        self.login_button = ctk.CTkButton(self.entry_screen,
                                          text='New Player',
                                          command=self.new_player_screen)
        self.login_button.pack(pady=30)

        self.entry_screen.pack()

        self.username_entry = None
        self.password_entry = None
        self.confirm_password_entry = None

        self.existing_player_window = None
        self.new_player_window = None
        self.new_player_instruction = None

        self.entry_screen.mainloop()

    def back_login_entry(self):
        self.existing_player_window.pack_forget()
        self.entry_screen.pack()

    def back_new_entry(self):
        self.new_player_window.pack_forget()
        self.entry_screen.pack()

    def existing_player_screen(self):

        self.entry_screen.pack_forget()

        self.existing_player_window = tk.Frame(self.start_up_window)
        self.existing_player_window.config(bg='#86cf9a')

        tk.Label(self.existing_player_window,
                 text='Welcome back bozo',
                 bg='#86cf9a', font='Courier 28 bold').pack(pady=24)

        tk.Label(self.existing_player_window,
                 text='Username',
                 bg='#86cf9a').pack()
        self.username_entry = tk.Entry(self.existing_player_window)
        self.username_entry.pack(pady=5)
        self.username_entry.bind('<space>', lambda e: 'break')

        tk.Label(self.existing_player_window,
                 text='Password',
                 bg='#86cf9a').pack()
        self.password_entry = tk.Entry(self.existing_player_window, show='*')
        self.password_entry.pack(pady=5)
        self.password_entry.bind('<space>', lambda e: 'break')

        ctk.CTkButton(self.existing_player_window,
                      text='Login',
                      command=self.login_existing).pack(pady=12)

        ctk.CTkButton(self.existing_player_window,
                      text='Back',
                      command=self.back_login_entry).pack()

        self.existing_player_window.pack()

        self.start_up_window.mainloop()

    def login_existing(self):

        with open('user_info', 'r') as readfile:
            datas = [line for line in DictReader(readfile)]

        taken_usernames = [user['username'] for user in datas]
        taken_passwords = [user['password'] for user in datas]

        if self.username_entry.get() in taken_usernames and self.password_entry.get() in taken_passwords:
            self.login_existing_user()
        else:
            tk.messagebox.showwarning('Incorrect details', 'Username or password is incorrect bozo')

    def login_existing_user(self):
        print('Logging in to existing user')

    def new_player_screen(self):

        self.entry_screen.pack_forget()

        self.new_player_window = tk.Frame(self.start_up_window)
        self.new_player_window.config(bg='#86cf9a')

        tk.Label(self.new_player_window,
                 text='Create an account bozo',
                 bg='#86cf9a', font='Courier 28 bold').pack(pady=12)

        tk.Label(self.new_player_window,
                 text='Enter a username',
                 bg='#86cf9a').pack()
        self.username_entry = tk.Entry(self.new_player_window)
        self.username_entry.pack(pady=3)
        self.username_entry.bind('<space>', lambda e: 'break')

        tk.Label(self.new_player_window,
                 text='Enter a password',
                 bg='#86cf9a').pack()
        self.password_entry = tk.Entry(self.new_player_window, show='*')
        self.password_entry.pack(pady=3)
        self.password_entry.bind('<space>', lambda e: 'break')

        tk.Label(self.new_player_window,
                 text='Confirm password',
                 bg='#86cf9a').pack()
        self.confirm_password_entry = tk.Entry(self.new_player_window, show='*')
        self.confirm_password_entry.pack(pady=3)
        self.confirm_password_entry.bind('<space>', lambda e: 'break')

        ctk.CTkButton(self.new_player_window,
                      text='Create Account',
                      command=self.create_account).pack(pady=8)

        ctk.CTkButton(self.new_player_window,
                      text='Back',
                      command=self.back_new_entry).pack()

        tk.Label(self.new_player_window, text="Username must:\n"
                                              "- be between 3 and 20 characters\n"
                                              "- be alphanumeric (contain only a-b and 0-9)\n"
                                              "\n"  
                                              "Password must:\n"
                                              "- be between 3 and 25 characters\n",
                                              bg='#86cf9a', justify=tk.LEFT).pack(side=tk.LEFT)

        self.new_player_window.pack()

        self.new_player_window.mainloop()

    def create_account(self):
        # print(f'{self.username_entry.get()}')
        # print(f'{self.password_entry.get()}')
        # print(f'{self.confirm_password_entry.get()}')
        print('Creating account')


