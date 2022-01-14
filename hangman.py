import random
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_word(niveau):
    url = "http://www.idees-gages.com/mots-jeu-pendu.php"
    page = urlopen(url)
    html = page.read().decode("utf-8")

    if niveau == 1:
        # list with 3 letter long word
        start_bloc_index = html.find("Âne")
        end_bloc_index = html.find("Tic")
        # To include the last word we move the index to the end of the word
        end_bloc = end_bloc_index + len("Tic")

        text = html[start_bloc_index:end_bloc]

        # Between each word in text there is "\r\n"
        list_mot = BeautifulSoup(text, "html.parser").get_text().split("\r\n")
        list_mot = [each_string.lower() for each_string in list_mot]

        return list_mot[random.randint(0, len(list_mot))]

    elif niveau == 2:
        # list with 4 letter long word
        start_bloc_index = html.find("Âtre")
        end_bloc_index = html.find("Vert")
        end_bloc = end_bloc_index + len("Vert")

        text = html[start_bloc_index:end_bloc]

        list_mot = BeautifulSoup(text, "html.parser").get_text().split("\r\n")
        list_mot = [each_string.lower() for each_string in list_mot]

        return list_mot[random.randint(0, len(list_mot))]

    elif niveau == 3:
        # List with 5 letters long word
        start_bloc_index = html.find("Accès")
        end_bloc_index = html.find("Valse")
        end_bloc = end_bloc_index + len("Valse")

        text = html[start_bloc_index:end_bloc]

        list_mot = BeautifulSoup(text, "html.parser").get_text().split("\r\n")
        list_mot = [each_string.lower() for each_string in list_mot]

        return list_mot[random.randint(0, len(list_mot))]

    elif niveau == 4:
        # List with 6 letters long word
        start_bloc_index = html.find("Acajou")
        end_bloc_index = html.find("Zipper")
        end_bloc = end_bloc_index + len("Zipper")

        text = html[start_bloc_index:end_bloc]

        list_mot = BeautifulSoup(text, "html.parser").get_text().split("\r\n")
        list_mot = [each_string.lower() for each_string in list_mot]

        return list_mot[random.randint(0, len(list_mot))]


def check(input, mot, control):
    # Temporary variable to check if player found at least letter
    change = False

    if input == mot:
        return True

    for i in range(len(mot)):
        if input == mot[i]:
            control[i] = True
            change = True

    if change:  # If no change then player missed
        return control

    return False


def show_mot_mystere(mot, control):
    for i, value in enumerate(control):
        if value:
            print(mot[i], end=" ")
        else:
            print("_", end=" ")

    print("\n")
    return


def show_pendu(erreur):

    if erreur == 1:
        print("""




        _______
        """)
    elif erreur == 2:
        print("""

           |
           |
           |
        ___|____
        """)
    elif erreur == 3:
        print("""
            ______
           |
           |
           |
        ___|____
        """)
    elif erreur == 4:
        print("""
            ______
           |      |
           |
           |
        ___|____
        """)
    elif erreur == 5:
        print("""
            ______
           |      |
           |      O
           |
        ___|____
        """)
    elif erreur == 6:
        print("""
            ______
           |      |
           |      O
           |      |
        ___|____
        """)
    elif erreur == 7:
        print("""
            ______
           |      |
           |      O
           |      |--
        ___|____
        """)
    elif erreur == 8:
        print("""
            ______
           |      |
           |      O
           |    --|--
        ___|____
        """)
    elif erreur == 9:
        print("""
            ______
           |      |
           |      O
           |    --|--
        ___|____ /
        """)
    elif erreur == 10:
        print("""
            ______
           |      |
           |      O
           |    --|--
        ___|____ / \\
        """)
    return


print("Welcome to hangman.")

# List of player creation
print("How many players?")

nbr_player = int(input("> "))
player_list = []

for i in range(nbr_player):
    print(f"Nom du joueur {i+1}: ")
    player_list.append(input("> "))
print("Ravie de jouer avec vous.")

# Selection of the level of the game and getting a word
print("Quel niveau de difficulté : 1, 2, 3, 4 (1 étant le plus facile)?")
niveau = int(input("> "))
mot = get_word(niveau)


# initialize the control list, list of tries, error counter
# This list control the print of the mysterious word,
control = [False for _ in range(len(mot))]

tries = []
error_counter = 0

# Compteur qui permet de savoir qui joue
joueur = 0

print('test')

# Starting the game
print("C'est parti mon kiki.")
print("Votre pendu :"+"\n"*10)
print("Vos essais : ")
show_mot_mystere(mot, control)

while True:
    print(f"{player_list[joueur]}, veuillez donner une lettre ou un mot.")
    essai = input("> ")

    # Check if the letter or word is good
    output = check(essai, mot, control)
    if output == True:
        print(f"Vous avez gagné, bravo à {player_list[joueur]}. Ciao")
        break
    elif output is False:
        error_counter += 1
        tries.append(essai)
        pass
    else:
        print("Bravo, vous en avez trouvé un.")
        control = output

    show_pendu(error_counter)
    print("Vos essais: ", tries)
    show_mot_mystere(mot, control)

    # If every elements of control are true, then it's a win
    if all(control):
        print(f"Vous avez gagné, bravo à {player_list[joueur]}. Ciao")
        break
    if error_counter == 10:
        print("Vous avez perdu bande de looser. Ciao")
        break

    # On change de joueur
    joueur += 1
    # Check if we are at the end of the list of nbr_player
    if joueur == len(player_list):
        joueur = 0
