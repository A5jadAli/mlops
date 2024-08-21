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
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

        
    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("You have successfully signed up!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("You are not signed up yet!")
            print("\n")
            self.menu()
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == self.username and password == self.password:
                self.loggedin = True
                print("You have successfully signed in!")
                print("\n")
                self.menu()
            else:
                print("Invalid email or password!")
                print("\n")
                self.menu()


obj = ChatBook()