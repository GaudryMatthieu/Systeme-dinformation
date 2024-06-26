import socket
#import sys

HOST, PORT = "172.17.0.2", 9999

def send_data():
    if data:
        data_str = "$".join(data)

        # Créer une socket (SOCK_STREAM signifie une socket TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try :
            # Se connecter au serveur et envoyer les données
                sock.connect((HOST, PORT))
                sock.sendall(bytes(data_str, "utf-8"))
                # Recevoir les données du serveur et fermer la connexion
                received = str(sock.recv(1024), "utf-8")

                print("Sent:     {}".format(data_str))
                print("Received: {}".format(received))
            except ConnectionError as e:
                print(f"Failed to connect to server: {e}")
    else:
        print("No data to send.")

def input_book():
    author = input("Entrez l'auteur : ")
    title = input("Entrez le titre : ")
    content = input("Entrez le contenu : ")
    data.append(author)
    data.append(title)
    data.append(content)

data = []
action =""
while action != "q":
        action = input("choose action: ")
        data = [action]
        print(f"triggered action: {action}")
        match action:
            case "modifier":
                input_book()
                send_data()
            case "créer":
                input_book()
                send_data()
            case "suppr":
                input_book()
                send_data()
            case "lire":
                send_data()
            case _:
                pass