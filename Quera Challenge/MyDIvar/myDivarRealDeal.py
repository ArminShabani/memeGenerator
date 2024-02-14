import time 
import os

class DataBase:
    def __init__(self):
        self.users = []
        self.usernames = []
        self.adds = []
        self.adds_names = []
        self.adds_favourites = []
    def register(self,id,username):
        if username not in self.usernames:
            self.usernames.append(username)
            self.users.append(Users(id,username))
            print(f"{username} has been succesfully submited with id of {id}")
            return True
        else:
            print(f"{username} is already in the database choose another one")            
    def add_advertisment(self,id,username,adds_title):
        for user in self.users:
            if user.username ==  username:
                if adds_title not in self.adds_names:
                    self.adds_names.append(adds_title)
                    self.adds.append(Adds(id,username,adds_title))
                    print(f"Advertisement '{adds_title}' has been successfully added by user '{username}' with id of {id}")
                    return True
                else:
                    print(f"Title {adds_title} already exists in DataBase.Please try again!")
            else:
                print("Invalid Username,Check the username or Register")
    def rem_addvertisment(self,id,username,adds_title):
        for user in self.users:
            if user.username == username:
                for adds in self.adds:
                    if adds.username == username:
                        if adds.adds_name == adds_title:
                            self.adds.remove(adds)
                            print(f"Advertisement '{adds_title}' has been successfully removed by user '{username}' with id of {id}")
                            return True
                        else:
                            print("Invalid Adds Title,Check the Adds Title and try again")
                    else:
                        print("Invalid Username,access denied")
            else:
                print("Invalid Username,Check the username or Register")
    def list_my_advertise(self,username):
        user_adds = [ad.adds_name for ad in self.adds if ad.username == username]
        if user_adds:
            print(f"advertisments submitted by '{username}': {' ,'.join(user_adds)}")
        else:
            print(f"no advertisments submitted by '{username}'")
    def add_favorite(self,username,adds_title):
        for user in self.users:
            if user.username == username:
                for adds in self.adds:
                    if adds.username == username:
                        if adds.adds_name == adds_title:
                            self.adds_favourites.append(adds)
                            print(f"Advertisement '{adds_title}' has been successfully added to favorites by user '{username}' with id of {id}")
                            return True
                        else:
                            print("Invalid Adds Title,Check the Adds Title and try again")
                    else:
                        print("Invalid Username,access denied")
            else:
                print("Invalid Username,Check the username or Register")
    def rem_favorite(self,username,adds_title):
        for user in self.users:
            if user.username == username:
                for adds in self.adds_favourites:
                    if adds.username ==  username:
                        if adds.adds_name == adds_title:
                            self.adds_favourites.remove(adds)
                            print(f"Advertisement '{adds_title}' has been successfully removed from favorites by user '{username}' with id of {id}")
                            return True
                        else:
                            print("Invalid Adds Title,Check the Adds Title and try again")
                    else:
                        print("Invalid Username,access denied")
            else:
                print("Invalid Username,Check the username or Register")
    def list_favorites(self,username):
        user_favorite = [ad.adds_name for ad in self.add_favorite if ad.username ==  username]
        if user_favorite:
            print(f"favorites submitted by '{username}': {' ,'.join(user_favorite)}")
        else:
            print(f"no favorites submitted by '{username}'")
               
class Users:
    def __init__(self,id,username):
        self.id = id
        self.username = username
    def __str__(self):
        return f"Id = {self.id},Username = {self.username}"
class Adds:
    def __init__(self,adds_id,username,adds_name):
        self.id = adds_id
        self.username = username
        self.adds_name = adds_name
        
    def __str__(self):
        return f"Adds Id = {self.id},Adds Creator = {self.username},Adds Name = {self.adds_name}"
    
    
    
def main():
    user_id = 1
    adds_id = 1
    register_successfull = False
    add_registerr_successfull = False
    dataBase = DataBase()
    print("Welcome to my divar app")
    time.sleep(5)
    os.system("cls" if os.name == 'nt' else 'clear')
    print("1. Register")
    print("2. Create Addvertisment")
    print("3. Remove Addvertisment")
    print("4. List My Addvertisment")
    print("5. Add Addvertisemt to Favorite")
    print("6. Remove Addvertisemt from Favorite")
    print("7. List my Favorite")
    user_input = int(input("enter a number from (1/2/3/4): "))
    if user_input == 1:#register
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_successfull = dataBase.register(user_id,username,password)
        if register_successfull:
            user_id += 1
    elif user_input == 2:#add
        id = adds_id
        username = input("Enter your username: ")
        adds_title = input("Enter your addvertisment title: ")
        add_registerr_successfull = dataBase.add_addvertisment(id,username,adds_title)
        if add_registerr_successfull:
            adds_id += 1
    elif user_input == 3:#remove 
        id = adds_id
        username = input("Enter your username: ")
        adds_title = input("Enter your addvertisment title: ")
        dataBase.rem_addvertisment(id,username,adds_title)
    elif user_input == 4:#normal list view
        username = input("Enter your username: ")
        dataBase.list_addvertisment(username)
    elif user_input == 5:#add to favorite 
        username = input("Enter your username: ")
        adds_title = input("Enter your addvertisment title: ")
        dataBase.add_favorite(username,adds_title)
    elif user_input == 6:#remove from favorite
        username = input("Enter your username: ")
        adds_title = input("Enter your addvertisment title: ")
        dataBase.rem_favorite(username,adds_title)
    elif user_input == 7:#favorit list view
        username = input("Enter your username: ")
        dataBase.list_favorites(username)
    
main()
    
    
    