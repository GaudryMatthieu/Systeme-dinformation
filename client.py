import socket
import sys

HOST, PORT = "localhost", 9999

# Joindre les arguments de la ligne de commande pour former l'action
action = " ".join(sys.argv[1:])
data = [action]

def input_book():
    author = input("Entrez l'auteur : ")
    title = input("Entrez le titre : ")
    content = input("Entrez le contenu : ")
    data.append(author)
    data.append(title)
    data.append(content)

if action == "créer" or action == "modifier" or action == "suppr":
    input_book()

# Vérifier si data est non vide avant de joindre et d'envoyer
if data:
    data_str = "$".join(data)

    # Créer une socket (SOCK_STREAM signifie une socket TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
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
