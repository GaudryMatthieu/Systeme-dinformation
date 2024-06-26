'''
The goal of this Python script is to simulate CRUD operations in the terminal.
We can create some books and store them in a library.
We can also read, modify, or delete the books in the library.
I used 2 classes to make my script. The first one is for the books and the second one is to store them.
'''
from prometheus_client import Counter, start_http_server, Gauge
import jsonpickle
import os
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server and must
    override the handle() method to implement communication with the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        print()
        self.data = self.request.recv(1024).strip()
        print(self.data)
        new_data = self.data.decode('utf-8').split('$')
        lib = Library()
        
        if new_data[0] == 'créer':
            lib.add_book(new_data)
            self.request.sendall("livre ajouté".encode("utf-8"))
        
        elif new_data[0] == 'lire':
            if not lib.get_shelf():
                self.request.sendall("Aucun livre dans la bibliothèque".encode("utf-8"))
            else:
                books = lib.read_library()
                self.request.sendall(books.encode("utf-8"))
                
        elif new_data[0] == 'suppr':
            if not lib.get_shelf():
                self.request.sendall("Aucun livre dans la bibliothèque".encode("utf-8"))
            else:
                lib.remove_book(new_data)
                self.request.sendall("livre supprimé".encode("utf-8"))
                    
        elif new_data[0] == 'modifier':
            if not lib.get_shelf():
                self.request.sendall("Aucun livre dans la bibliothèque".encode("utf-8"))
            else:
                lib.update_book(new_data)
                self.request.sendall("livre modifié".encode("utf-8"))
        else:
            self.request.sendall("commande inconnue".encode("utf-8"))

class Book:
    def __init__(self, author, title, content):
        self.__author = author
        self.__title = title
        self.__content = content
    
    def display_details(self):
        return f"Auteur : {self.__author}, Titre : {self.__title}, Contenu : {self.__content}"
        
    def update(self, author, title, content):
        self.__author = author
        self.__title = title
        self.__content = content
    
    # Getter to get the title
    def get_title(self):
        return self.__title
    
    # Function to get the title as a string and not the address location
    def __str__(self):
        return f"{self.__title}"

class Library:
    global_file = "save.json"
    
    def __init__(self):
        self.__shelf = []
        self.__load()
    
    def add_book(self, data):
        print("1")
        book = Book(data[1], data[2], data[3])
        print("2")
        self.__shelf.append(book)
        print("3")
        self.save()
        c.inc()
        g.inc()
        
    def read_library(self):
        books = ""
        for book in self.__shelf:
            books += book.display_details()
        return books
            
    def remove_book(self, data):
        counter = 0
        for book in self.__shelf:
            counter += 1
            if book.get_title() == data[2]:
                self.__shelf.remove(book)
                print("Le livre a été supprimé de la liste")
                self.save()
                g.dec()
                return  # Exit the loop after deletion
            
    def update_book(self, data):
        book_to_update = input("Entrez le nom du livre à modifier : ")
        for book in self.__shelf:
            if book.get_title() == book_to_update:
                book.update(data[1], data[2], data[3])
                print("Le livre a été modifié")
                self.save()
                return  # Exit the loop after update
        
    def get_shelf(self):
        return self.__shelf
    
    def __str__(self):
        return f"{[book.get_title() for book in self.__shelf]}"
    
    def __load(self):
        if os.path.exists(Library.global_file):
            with open(Library.global_file, 'r') as f:
                strjson = f.read()
                self.__shelf = jsonpickle.decode(strjson)._Library__shelf

    def save(self):
        with open(Library.global_file, 'w') as f:
            f.write(jsonpickle.encode(self))

"""def input_book():
    author = input("Entrez l'auteur : ")
    title = input("Entrez le titre : ")
    content = input("Entrez le contenu : ")
    return author, title, content

 def main():
    print("Bienvenue! Tapez 'exit' pour quitter.")
    lib = Library()
    while True:
        user_input = input("Entrez une commande: ").lower()
        if user_input == 'créer':
            lib.add_book()
        
        elif user_input == 'lire':
            if not lib.get_shelf():
                print("Aucun livre n'a été ajouté.")
            else:
                lib.read_library()
                
        elif user_input == 'suppr':
            if not lib.get_shelf():
                print("Aucun livre ne peut être supprimé.")
            else:
                book_to_delete = input("Entrez le nom du livre à supprimer : ")
                lib.remove_book(book_to_delete)
                    
        elif user_input == 'modifier':
            if not lib.get_shelf():
                print("Aucun livre ne peut être modifié.")
            else:
                lib.update_book()
                
        elif user_input == 'exit':
            lib.save()
            print("Au revoir!")
            break

        else:
            print(f"Commande inconnue: {user_input}") """

# This condition checks if the script is executed as the main script
if __name__ == "__main__":
    start_http_server(7777)
    HOST, PORT = "0.0.0.0", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Serving on {HOST}:{PORT}")
        c = Counter('ADD', 'a book has been add to the librairie')
        g = Gauge('Toto_BOOK', 'Description of gauge')
        g.set(4) 
        server.serve_forever()