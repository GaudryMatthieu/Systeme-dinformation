class Book:
    def __init__(self, author, title, content):
        self.__author = author
        self.__title = title
        self.__content = content
    
    def display_details(self):
        print("Author: ", self.__author)
        print("Title: ", self.__title)
        print("Content: ", self.__content)
        
    def update(self, author, title, content):
        self.__author = author
        self.__title = title
        self.__content = content
    
    def get_title(self):
        return self.__title
    
    def __str__(self):
        return f"{self.__title}"


class Library:
    def __init__(self):
        self.__shelf = []
        
    def add_book(self):
        author = input("Entrez l'auteur : ")
        title = input("Entrez le titre : ")
        content = input("Entrez le contenu : ")
            
        book = Book(author, title, content)
        self.__shelf.append(book)
        
    def read_library(self):
        for book in self.__shelf:
            print(f"Voici le contenu de la bibliothèque : {book}")
            book.display_details()
            print("-----")
            
    def remove_book(self, book_to_delete):
        for book in self.__shelf:
            if book.get_title() == book_to_delete:
                self.__shelf.remove(book)
                print("Le livre a été supprimé de la liste")
                return  # Sortir de la boucle après suppression
            
    def update_book(self):
        book_to_update = input("Entrez le nom du livre à modifier : ")
        for book in self.__shelf:
            if book.get_title() == book_to_update:
                author = input("Entrez l'auteur à modifier: ")
                title = input("Entrez le titre à modifier : ")
                content = input("Entrez le contenu à modifier : ")
                new_book = Book(author, title, content)
                self.__shelf.remove(book)
                self.__shelf.append(new_book)
                print("Le livre a été modifié de la liste")
                return  # Sortir de la boucle après suppression
        
    def get_shelf(self):
        return self.__shelf
    
    def __str__(self):
        return f"{[book.get_title() for book in self.__shelf]}"

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
            print("Au revoir!")
            break

        else:
            print(f"Commande inconnue: {user_input}")

if __name__ == "__main__":
    main()
