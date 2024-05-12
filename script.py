def coder(text: str, key: str) -> str:
    """Fonction qui permet de crypter un texte au moyen de la méthode de chiffrement à clé secrète.

    :param text: le texte à crypter
    :type text: str
    :param key: la clé secrète
    :type key: str
    :return: le texte crypté
    :rtype: str
    """
    while len(text) % len(key) != 0:
        text += "*"

    return "".join(element[1:] for element in sorted(f"{key[i]}{text[i::len(key)]}" for i in range(len(key)))).replace(" ", "_")


def decoder(text: str, key: str) -> str:
    """Fonction qui permet de décrypter un texte crypté au moyen de la méthode de chiffrement à clé secrète.

    :param text: le texte crypté à décrypter
    :type text: str
    :param key: la clé secrète (qui doit être la même que celle ayant permis le cryptage)
    :type key: str
    :return: le texte décrypté
    :rtype: str
    """
    letters = [letter for letter in key]
    characters = [character for character in text]
    decryption_list = []

    for i in range(len(key)):
        decryption_list.append(f"{''.join(sorted(letters)[i][0])}{''.join(characters[:len(text)//len(key)])}")
        del characters[:len(text)//len(key)]

    for element in decryption_list:
        if element[0] in letters:
            letters.insert(letters.index(element[0]), element[1:])

    return "".join("".join(letters[::2])[i::len(text)//len(key)] for i in range(len(text)//len(key))).replace("*", "").replace("_", " ")