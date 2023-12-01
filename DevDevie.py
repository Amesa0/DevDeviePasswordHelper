import string
import time
import random
import sys

# Kullanıcı adına göre özel parola oluşturma
def generate_password(username):
    password_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_chars) for _ in range(len(username) * 3))

# Tüm tahminleri bir dosyaya yazma
def write_password_guesses(username):
    filename = f"{username}_password_guesses.txt"
    with open(filename, 'w') as file:
        for i in range(len(username)):
            password_guess = ''.join(random.choice(string.ascii_letters) if index != i else char for index, char in enumerate(username))
            file.write(password_guess + '\n')

# Hoş geldiniz ekranı
def display_welcome_banner():
    print("""
▓█████▄ ▓█████ ██▒   █▓▓█████▄ ▓█████ ██▒   █▓ ██▓▓█████ 
▒██▀ ██▌▓█   ▀▓██░   █▒▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▓█   ▀ 
░██   █▌▒███   ▓██  █▒░░██   █▌▒███   ▓██  █▒░▒██▒▒███   
░▓█▄   ▌▒▓█  ▄  ▒██ █░░░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒▓█  ▄ 
░▒████▓ ░▒████▒  ▒▀█░  ░▒████▓ ░▒████▒  ▒▀█░  ░██░░▒████▒
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░   ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░░ ▒░ ░
 ░ ▒  ▒  ░ ░  ░  ░ ░░   ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░ ░ ░  ░
 ░ ░  ░    ░       ░░   ░ ░  ░    ░       ░░   ▒ ░   ░   
   ░       ░  ░     ░     ░       ░  ░     ░   ░     ░  ░
 ░                 ░    ░                 ░              
""")

# Kırma işlemini simüle et
def crack_password(username):
    print(f"[*] Starting password cracking for the username '{username}'...")
    time.sleep(2)

    generated_password = generate_password(username)

    print(f"[*] Password for the username '{username}' is '{generated_password}'")

# Bitiş ekranı
def display_finish_banner():
    print("""

███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓    ▄▄▄       ███▄ ▄███▓▓█████   ██████  ▄▄▄
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒   ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▒████▄
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   ▒██  ▀█▄
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒░██▄▄▄▄██
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░    ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒ ▓█   ▓██▒
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒     ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░
""")

# Ana fonksiyon
def run_password_cracking_tool():
    display_welcome_banner()

    if len(sys.argv) != 2:
        print("[!] Usage: python3 DevDevie.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    write_password_guesses(username)
    crack_password(username)

    display_finish_banner()

run_password_cracking_tool()
