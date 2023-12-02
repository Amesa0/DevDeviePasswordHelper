import os
import hashlib
import string
import random
import time
from halo import Halo
import itertools

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    print("""
  
██████╗ ███████╗██╗   ██╗██████╗ ███████╗██╗   ██╗██╗███████╗    ██╗   ██╗██████╗ 
██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝██║   ██║██║██╔════╝    ██║   ██║╚════██╗
██║  ██║█████╗  ██║   ██║██║  ██║█████╗  ██║   ██║██║█████╗      ██║   ██║ █████╔╝
██║  ██║██╔══╝  ╚██╗ ██╔╝██║  ██║██╔══╝  ╚██╗ ██╔╝██║██╔══╝      ╚██╗ ██╔╝██╔═══╝ 
██████╔╝███████╗ ╚████╔╝ ██████╔╝███████╗ ╚████╔╝ ██║███████╗     ╚████╔╝ ███████╗
╚═════╝ ╚══════╝  ╚═══╝  ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝
                                                                                  
                                                                       
""")

def get_hash(password):
    spinner = Halo(text='Hashing password...', spinner='dots')
    spinner.start()
    time.sleep(2)
    hash_object = hashlib.sha1(password.encode())
    spinner.stop()
    return hash_object.hexdigest()

def generate_wordlist(word_length=4):
    chars = string.ascii_letters + string.digits + string.punctuation
    word_list = [''.join(i) for i in itertools.product(chars, repeat=word_length)]
    return word_list

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_username(length=12):
    spinner = Halo(text=f'Generating username with {length} words...', spinner='dots')
    spinner.start()
    time.sleep(2)
    fruit_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pineapple', 'plum', 'raspberry', 'strawberry', 'tomato', 'ugli fruit', 'vanilla', 'watermelon', 'zucchini']
    username = ' '.join(random.choice(fruit_list) for _ in range(length))
    spinner.stop_and_persist(symbol='🍏', text=f'Generated username: {username}')
    return username

def hash_password(password):
    spinner = Halo(text='Hashing password...', spinner='dots')
    spinner.start()
    time.sleep(2)
    hash_object = hashlib.sha1(password.encode())
    hashed_password = hash_object.hexdigest()
    spinner.stop_and_persist(symbol='🔒', text=f'Hashed password: {hashed_password}')
    return hashed_password

def get_password_strength(password):
    strength = "Weak"
    if len(password) >= 12 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        strength = "Strong"
    return strength

def change_password(username):
    new_password = input(f"Enter a new password for {username}: ")
    return new_password

def save_credentials(username, password):
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

def check_username_availability(username):
    used_usernames = ["example", "user", "test"]  # Replace with real used usernames
    return username not in used_usernames

def generate_gmail_username():
    spinner = Halo(text='Generating Gmail username...', spinner='dots')
    spinner.start()
    time.sleep(2)
    username = generate_username(3)  # Generate a 3-word username for Gmail
    spinner.stop_and_persist(symbol='📧', text=f'Generated Gmail username: {username}')
    
    is_available = check_username_availability(username)
    if is_available:
        print("Username is available for Gmail.")
    else:
        print("Username is already taken. Please try another one.")

def check_password_complexity(password):
    complexity = "Weak"
    if len(password) >= 8:
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)
        
        if has_upper and has_lower and has_digit and has_special:
            complexity = "Strong"
    return complexity

def show_credits():
    print("""

███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗     █████╗ ███╗   ███╗███████╗███████╗ █████╗  ██████╗ 
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗ ████║██╔════╝██╔════╝██╔══██╗██╔═████╗
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ███████║██╔████╔██║█████╗  ███████╗███████║██║██╔██║
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║████╔╝██║
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ██║  ██║██║ ╚═╝ ██║███████╗███████║██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                
 ██╗ ██████╗██╗     ██████╗  ██████╗ ██████╗ ██████╗       ██████╗  ██████╗ ██████╗  █████╗                     
██╔╝██╔════╝╚██╗    ╚════██╗██╔═████╗╚════██╗╚════██╗      ╚════██╗██╔═████╗╚════██╗██╔══██╗                    
██║ ██║      ██║     █████╔╝██║██╔██║ █████╔╝ █████╔╝█████╗ █████╔╝██║██╔██║ █████╔╝╚█████╔╝                    
██║ ██║      ██║    ██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗╚════╝██╔═══╝ ████╔╝██║██╔═══╝ ██╔══██╗                    
╚██╗╚██████╗██╔╝    ███████╗╚██████╔╝███████╗██████╔╝      ███████╗╚██████╔╝███████╗╚█████╔╝                    
 ╚═╝ ╚═════╝╚═╝     ╚══════╝ ╚═════╝ ╚══════╝╚═════╝       ╚══════╝ ╚═════╝ ╚══════╝ ╚════╝                     
                                                                                                                

""")

def main():
    clear_screen()
    print_banner()
    choice = input("Choose an option: \n1. Generate a strong password \n2. Generate a cool username \n3. Hash a password \n4. Check password strength \n5. Change password \n6. Save credentials \n7. Generate a Gmail username and check availability \n8. Check password complexity \n9. Show credits \nEnter your choice: ")
    
    if choice == '1':
        password_length = int(input("Enter the desired password length (default is 8): ") or 8)
        password = generate_password(password_length)
        print(f"Generated password: {password}")
        
    elif choice == '2':
        username_length = int(input("Enter the desired username length in words (default is 12): ") or 12)
        generate_username(username_length)
        
    elif choice == '3':
        password = input("Enter the password to hash: ")
        hash_password(password)
        
    elif choice == '4':
        password = input("Enter the password to check strength: ")
        strength = get_password_strength(password)
        print(f"Password strength: {strength}")
        
    elif choice == '5':
        username = input("Enter your username: ")
        new_password = change_password(username)
        print(f"Password changed for {username} to: {new_password}")
        
    elif choice == '6':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        save_credentials(username, password)
        print("Credentials saved successfully!")
        
    elif choice == '7':
        generate_gmail_username()
        
    elif choice == '8':
        password = input("Enter the password to check complexity: ")
        complexity = check_password_complexity(password)
        print(f"Password complexity: {complexity}")  
        
    elif choice == '9':
        show_credits()

if __name__ == "__main__":
    main()
