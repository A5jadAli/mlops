class ChatBook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.looggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to ChatBook! How would you like to proceed?
                           1. Press in for Sign up
                           2. Press 2 for Sign in
                           3. Press 3 to write a post
                           4. Press 4 to message someone
                           5. Press any other key to exit""")
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
