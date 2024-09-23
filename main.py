"""
Ce module contient des fonctions pour tester si un nombre est premier et
pour exécuter une série de tests sur une liste de nombres.
"""

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un nombre donné est premier.

    Args:
        p (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """

    # votre code ici
    if p in (2,3):
        return True
    if p % 2 == 0 or p < 2:
        return False
    for i in range(3, int(p ** 0.5) + 1, 2):
        if p % i == 0:
            return False
    return True


#### Fonction principale


def main():
    """
    Fonction principale qui teste une série de nombres pour voir
    s'ils sont premiers et affiche les résultats.
    """
    test_numbers = [1, 2, 3, 4, 5, 9, 11, 13, 16, 17, 19, 23, 24, 29]

    # vos appels à la fonction secondaire ici

    for n in test_numbers :
        if isprime(n):
            print(f"{n} est un nombre premier")
        else:
            print(f"{n} n'est pas premier")


if __name__ == "__main__":
    main()
