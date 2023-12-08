import string
import hashlib
import json
import random

def password_generator():
    print('''Votre mot de passe doit contenir au moins : 
          - huit caractères
          - une lettre majuscule
          - une lettre minuscule
          - un chiffre
          - un caractère spécial
          ''')
    
    while True:
        pwd = input("Veuillez entrer un mot de passe : ")

        if len(pwd) < 8:
            print("Le mot de passe doit contenir au moins huit caractères.")
            continue

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in pwd:
            if char in string.ascii_uppercase:
                has_upper = True
            elif char in string.ascii_lowercase:
                has_lower = True
            elif char in string.digits:
                has_digit = True
            elif char in string.punctuation:
                has_symbol = True

        if has_upper and has_lower and has_digit and has_symbol:
            print("Le mot de passe respecte les critères précédemment cités.")
            break
        else:
            print("Le mot de passe ne respecte pas tous les critères. Veuillez réessayer.")
            continue

    def hash_password(pwd):
        password_bytes = pwd.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()

    hashed_password = hash_password(pwd)
    print("hachage de mot de passe réussi :", hashed_password)


    with open('password.json', 'r') as file:
            content = file.read()
            if content:
                loaded_password = json.loads(content)
                with open('password.json', 'w') as file: 
                    json.dump(content, file)
                print(f"Mot de passe pour ajouté avec succès.")
            else:
                loaded_password = []
                print("Le fichier est vide. Initialisation d'une liste vide.")
    
    again = input("voulez-vous ajouter un nouveau mot de passe (oui/non) ?\n")

    def switch(again):
        if again == "oui":
            hash_password(pwd)
            password_generator()
        elif again == "non":
            quit()

    switch(again)
    hash_password(pwd)

password_generator()
