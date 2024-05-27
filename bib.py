class Book:
    def __init__(self, author, title, content):
        self.__author = author
        self.__title = title
        self.__content = content
    
    def display_author(self):
        print("author: ", self.author)
        print("title: ", self.title)
        print("content: ", self.content)

def main():
    print("Bienvenue! Tapez 'exit' pour quitter.")
    while True:
        user_input = input("Entrez une commande: ")
        if user_input.lower() == 'exit':
            print("Au revoir!")
            break
        else:
            print(f"Vous avez entré: {user_input}")

if __name__ == "__main__":
    main()