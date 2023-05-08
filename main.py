import random

# Définition des options du jeu
options = ["Pierre", "Feuille", "Ciseaux"]


# Fonction pour l'entrée utilisateur et validation
def user_choice():
    choice = input("Pierre, Feuille ou Ciseaux? ").capitalize()
    while choice not in options:
        choice = input("Choix invalide. Veuillez entrer Pierre, Feuille ou Ciseaux: ").capitalize()
    return choice


# Fonction pour la sélection aléatoire de l'ordinateur
def computer_choice():
    return random.choice(options)


# Fonction pour déterminer le résultat du jeu
def game_result(user, compCuter):
    if user == computer:
        return "Match nul!"
    elif user == "Pierre":
        if computer == "Ciseaux":
            return "Vous avez gagné!"
        else:
            return "L'ordinateur a gagné!"
    elif user == "Feuille":
        if computer == "Pierre":
            return "Vous avez gagné!"
        else:
            return "L'ordinateur a gagné!"
    elif user == "Ciseaux":
        if computer == "Feuille":
            return "Vous avez gagné!"
        else:
            return "L'ordinateur a gagné!"


# Boucle principale du jeu
while True:
    user = user_choice()
    computer = computer_choice()
    result = game_result(user, computer)
    print(f"Vous avez choisi {user}, l'ordinateur a choisi {computer}. {result}")
    play_again = input("Voulez-vous jouer à nouveau? (Oui/Non)").lower()
    if play_again != "oui":
        break

print("Merci d'avoir joué!")
