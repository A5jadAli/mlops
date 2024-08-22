class ChatBook:
    def __init__(self):
        self.__name = "Default"
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to ChatBook! How would you like to proceed?
                           1. Press in for Sign up
                           2. Press 2 for Sign in
                           3. Press 3 to write a post
                           4. Press 4 to message someone
                           5. Press any other key to exit
                           
                           -> """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.message()
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

    def write_post(self):
        if self.loggedin == True:
            post = input("What's on your mind? ")
            print(f"Following content has been posted {post}")
        else:
            print("Please signin to make a post.")
        print("\n")
        self.menu()

    def message(self):
        if self.loggedin == True:
            msg = input("Enter your message: ")
            recipient = input("Enter the recipient's email: ")
            print(f"Message sent to {recipient}")
        else:
            print("Please signin to send a message.")
        print("\n")
        self.menu()


obj = ChatBook()