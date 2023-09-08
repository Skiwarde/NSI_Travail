class CodeCesar:
    # Je crée la classe "Code César" qui va regrouper toutes les méthodes qui me permettront de me servir d'elle

    def __init__(self, cle):
        # La méthode spéciale __init__ permet d"être utiliser lors de la création d'instance dans la classe,
        # on l'utilise pour y initialiser les attributs de l'objet avec les valeurs spécifiés lors de sa création.
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def decale(self, lettre):
        # La méthode decale permet d'y attribuer une lettre et grâce à la valeur qu'on aura associé à la clé, de
        # nous donner ensuite la lettre selon notre code
        num1 = self.alphabet.find(lettre)
        # La lettre que l'on va attribuer (exemple : code1.decale("A"), A est la fameuse lettre.)
        num2 = num1+self.cle
        # On ajoute la lettre attribué (dans l'exemple, c'était A) et on y ajoute la valeur de la cle (si la cle était
        # code1=CodeCesar(3), alors A > B(1) > C(2) > D(3), le résulatat attendu est D)
        if num2 >= 26:
            num2 = num2-26
            # Si la valeur attribué à la cle est supérieur à 26, on retire 26 pour faire "le tour" des lettres de
            # l'alphabet et donc retourner. Si par exemple la valeur de la cle était 29, on peut dire que c'est 26 + 3,
            # alors on enlève 26 et la cle devient 3
        if num2 < 0:
            num2 = num2+26
            # Si la valeur attribué à la cle est inférieur à 0, alors on rajoute 26 pour
            # retrouver une valeur positive, et ainsi "retourner en arrière"
        nouvelle_lettre = self.alphabet[num2]  # On attribut à nouvelle lettre le résultat de self.alphabet selon num2
        return nouvelle_lettre  # Consiste à print ce qu'on à attribuer à nouvelle_lettre, soit self.alphabet[num2]

    def cryptage(self, texte):
        # La méthode cryptage permet d'utiliser la méthode Decale, mais sur plusieurs lettre à la fois
        texte_crypte = ""  # On définit le résultat de "texte_crypte"
        for lettre in texte:
            # Si la lettre fait parti de l'alphabet, la méthode va passer en revue chacune d'entre
            # elles pour les ajouter selon "decale", si elle la lettre ne fait pas parti de l'alphabet,
            # il va la conserver sans la faire passer par decale.
            if texte.isalpha():
                lettre_cryptee = self.decale(lettre)
                texte_crypte += lettre_cryptee
            else:
                texte_crypte += lettre
        return texte_crypte  # Retourne le résultat de texte_crypte

    """ La méthode transforme permet d'inverser la valeur de la cle 
    (si elle est positive, elle devient négative, et vice-versa)"""
    def transforme(self, texte):
        self.cle = -self.cle  # Inverse la valeur de la clé (positive > négative | négative > positive)
        message = self.cryptage(texte)
        # La variable message correspond au résultat du chiffrement cryptage avec la clé
        # inversée.
        self.cle = -self.cle # Remet la clé dans sa valeur par défaut avant de recommencer la méthode
        return message


cle = int(input("Insérer la valeur de la clé : "))
code = CodeCesar(cle)

texte_a_chiffre = input("Insérer le texte à chiffrer : ")

texte_chiffre = code.cryptage(texte_a_chiffre)
print("Voici votre texte décrypter selon votre clé :", texte_chiffre)


""" 
Commentaire sur la partie 4 :
print(CodeCesar(10).transforme("PSX")) Va afficher "FIN" car il inverse la 
valeur de la clé, puis assigne la lettre (dans ce cas, 10 id en arrières)
puis remet la valeur de la clé avant de recommencer pour la lettre suivante.
"""
