import socket
import select

# https://www.gatevidyalay.com/transmission-control-protocol-tcp-header/
HEADER_LENGTH= 10
# IP standard pour localhost
ADRESSE_IP_SERVEUR="127.0.0.1"
PORT_SERVEUR=1234
server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# Associe le serveur a l'adresse IP et au port
server_socket.bind((ADRESSE_IP_SERVEUR,PORT_SERVEUR))
# Le serveur attend des connexion sur son port -> Réactivité
server_socket.listen((ADRESSE_IP_SERVEUR,PORT_SERVEUR))

sockets_list=[server_socket]
clients={}
# Fonction de recupération des messages des utilisateurs
def get_message(client_socket):
    try:
        message_header=client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
                return False
        message_length= int(message_header.decode("utf-8").strip())
        return {"header":message_header,"data":client_socket.recv(message_header)}

    except:
        return False

while True:
        read_sockets, _, exception_sockets=select.select(sockets_list)
        for notified_socket in read_sockets:
            if notified_socket === server_socket:
                client_socket,client_adress = server_socket.accept()

                user=receive_message(client_socket)
                if user is False:
                    continue

                sockets_list.append()