class CodeCesar:

    def __init__(self, cle):
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

    def decale(self, lettre):
        num1 = self.alphabet.find(lettre)
        num2 = (num1+self.cle) % 26 # Remplace l'ancienne méthode, et permet d'utiliser des cle bien plus élevé

        nouvelle_lettre = self.alphabet[num2]
        return nouvelle_lettre

    def cryptage(self, texte):
        texte_crypte = ""
        
        if texte.islower():
            texte = texte.upper()

            for lettre in texte:
                if lettre.isalpha():
                    lettre_cryptagee = self.decale(lettre)
                    texte_crypte += lettre_cryptagee
                else:
                    texte_crypte += lettre
            texte_crypte = texte_crypte.lower()

        else:
            for lettre in texte:
                if lettre.isalpha():
                    lettre_cryptagee = self.decale(lettre)
                    texte_crypte += lettre_cryptagee
                else:
                    texte_crypte += lettre
        return texte_crypte
