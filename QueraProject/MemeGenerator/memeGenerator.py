import os
from datetime import date

class DataBase:
    def __init__(self):
        self.users = []
        self.usernames = []
        self.emails = []
        self.memes = []
        self.meme_names = []
    def login(self,id,username,password):
        if username in self.usernames:
            for i in self.users:
                if i.username == username and i.password == password:
                    i.id = id
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'welcome {username} with id {id}')
                    return True
        else:
            print("invalid Credentials")
    
    def register(self,id,firstname,lastname,email,username,password,re_password):
        if username not in self.usernames and email not in self.emails:
            if password == re_password:
                self.emails.append(email)
                self.usernames.append(username)
                self.users.append(Users(id,firstname,lastname,email,username,password))
                print(f"{username} has been succesfully submited with id of {id}")
                return True
            else:
                print("Password do not match")
        else:
            print("Username or Email already exists. Please try again.")
    def create_Meme(self,meme):
        self.meme_names.append(meme.meme_name)
        self.memes.append(meme)
    def fetch_meme(self,id):
        for meme in self.memes:
            if meme.id == id:
                return meme
        return f"no meme was found with that {id}"
    def delete_meme(self,id):
        for meme in self.memes:
            if meme.id == id:
                self.memes.remove(meme)
    def fetch_user(self,id):
        for user in self.users:
            if user.id == id:
                return user
        return f'no user with that {id} was found in the database'
    def update_user(self,username,password,new_entry,field):
        for i in self.users:
            if i.username == username and i.password == password:
                if field == "username":
                    i.username = new_entry
                    self.usernames.remove(username)
                    self.usernames.append(new_entry)
                elif field == "password":
                    i.password = new_entry
    
class Users:
    def __init__(self,id,firstname,lastname,email,username,password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
    def __str__(self):
        return f"Id: {self.id}, Name: {self.firstname} {self.lastname}, Email: {self.email}, Username: {self.username}"
    
class Meme:
    def __init__(self,id,username,meme_name,genre,description,max_receipt_date):
        self.id = id
        self.username = username
        self.meme_name = meme_name
        self.genre = genre
        self.description = description
        self.max_receipt_date = max_receipt_date
    def __str__(self):
        return f"Craetor of Meme:{self.username} Meme name: {self.meme_name}, Genre: {self.genre}, Max receipt date: {self.max_receipt_date}, Description: {self.description}, Id: {self.id}"

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
            name = input("State your F rst name: ")
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
                    print("meme {memeName} has been created with id of {meme_id} created by {username} and is valid until {memeMaxReceiptDate}")
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