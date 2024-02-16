import os
from datetime import date

class DataBase:
    def __init__(self):
        self.users = []
        self.memes = []
        self.emails = []
        self.username = []
    def login(self,id,username,password):
        if username in self.username:
            for i in self.users:
                if i.username == username and i.password == password:
                    id = i.id
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"welcome {username} with id {id}")
                    return True
        else :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid credentials. Please try again.")
    def register(self,id,name,second_name,email,username,password,re_password):
        if email not in self.emails and username not in self.username:
            if password == re_password:
                self.username.append(username)
                self.emails.append(email)
                self.users.append(Users(id,name,second_name,email,username,password))
                return True
            else: 
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Passwords do not match. Please try again.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username or email already exists. Please try again.")
    def create_Meme(self,meme):
        self.memes.append(meme)
    def fetch_meme(self,id):
        for i in self.memes:
            if i.id == id:
                return i
        return f"no meme was found with that {id}"
    def delete_meme(self,id):
        for i in self.memes:
            if i.id == id:
                self.memes.remove(i)
    def fetch_info(self, id):
        for i in self.users:
            if i.id == id:
                return i
    def update_user(self,username,password,new_entry,field):
        for i in self.users:
            if i.username == username and i.password == password:
                if field == "username":
                    i.username = new_entry
                    self.username.remove(username)
                    self.username.append(new_entry)
                elif field == "password":
                    i.password = new_entry
class Meme:
    def __init__(self,username, name, genre, max_receipt_date, description,id):
        self.username = username
        self.name = name
        self.genre = genre
        self.max_receipt_date = max_receipt_date
        self.description = description
        self.id = id
    def __str__(self):
        return f"Meme name: {self.name}, Genre: {self.genre}, Max receipt date: {self.max_receipt_date}, Description: {self.description}, Id: {self.id}"
class Users:
    def __init__(self,id,name,second_name,email,username,password):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.email = email
        self.username = username
        self.password = password
    def __str__(self):
        return f"Name: {self.name} {self.second_name}, Email: {self.email}, Username: {self.username}, Password: {self.password}"
        
def main():
    user_id = 1
    meme_id = 1
    dataBase = DataBase()
    login_success = False
    register_success = False
    flag = True
    
    
    while True:
        print("welcome")
        print("1.login")
        print("2.register")
        print("3.exit")
        choice = input("Enter a number (1/2/3): ")
        
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_success = dataBase.login(user_id,username,password) 
            
            
            
        elif choice == "2":
            
            print(f"your account id is {user_id}")
            id = user_id
            name = input("State your First name: ")
            second_name = input("State your Last Name: ")
            email = input("Enter your email: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            re_password = input("Re-Enter your password: ")
            register_success = dataBase.register(id,name,second_name,email,username,password,re_password)
            if register_success:
                user_id += 1
                
                
        elif choice == "3":
            print("thanks for using our app")
            break
        else:
            print("invalid number, please choose a number between 1/2/3:")
        
        if login_success:
            while True:
                print(f"Welcome to the Azizi's meme factory dear {username}!")
                print("1.Create a Meme")
                print("2. Nevermind(Delete Meme)")
                print("3.Show meme information")
                print("4.Show user information")
                print("5.Change user information")
                print("6.Logout")
                choice = input("Enter your choice (1/2/3/4/5/6): ")
                
                
                if choice == "1":
                    print(f"your meme id is {meme_id}")
                    memeName = input("Enter meme name: ")
                    memeGenre = input("Enter meme genre: ")
                    memeMaxReceiptDate = date.today()
                    memeDescription = input("Enter meme description: ")
                    dataBase.create_Meme(Meme(username, memeName, memeGenre, memeMaxReceiptDate, memeDescription, meme_id))
                    meme_id += 1
                    
                    
                elif choice == "2":
                    id_meme_delete = input("which meme would you like to delete(id): ")
                    dataBase.delete_meme(id_meme_delete)
                    print("your meme has been sucessfully deleted")
                    
                      
                elif choice == "3":
                    meme_choice = int(input("Enter meme id: "))
                    print(dataBase.fetch_meme(meme_choice))
                    
                    
                    
                elif choice == "4":
                    user_choice = int(input("enter user id:"))
                    print(dataBase.fetch_info(user_choice))
                    
                    
                    
                elif choice == "5":
                    field_choice = input("Enter field you want to change (username/password): ")
                    new_entry = input("Enter new value: ")
                    dataBase.update_user(username,password,new_entry,field_choice)
                        
                            
                            
                elif choice == "6":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("you have been logedout from your account")
                    flag = False
                    if flag == False:
                        break
                else:
                    print("invalid number, please choose a number between 1/2/3/4/5/6:")
                    
main()                
                
            
                