from Classes.Patient import Patient
from Classes.Fournisseur import Fournisseur

class Medicament:
    liste_medicaments = []

    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "",
                 p_prix: float = 0.0, p_categorie_medicament: str = "",
                 p_liste_patients_achete: list[Patient] = None, p_fournisseur: Fournisseur = None):
        """
        Constructeur de la classe Medicament
        :param p_code_medicament: Code du médicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Le prix du médicament
        :param p_categorie_medicament: La catégorie du médicament
        :param p_liste_patients_achete: La liste des patients qui ont acheté ce médicament
        :param p_fournisseur: Le fournisseur de ce médicament
        """
        self._code_medicament = p_code_medicament
        self._nom_chimique = p_nom_chimique
        self._nom_commercial = p_nom_commercial
        self._prix = p_prix
        self.categorie_medicament = p_categorie_medicament
        if p_liste_patients_achete is None:
            self.liste_patients_achete = []
        else:
            self.liste_patients_achete = p_liste_patients_achete
        self.fournisseur = p_fournisseur

    @property
    def code_medicament(self):
        return self._code_medicament

    @code_medicament.setter
    def code_medicament(self, v_code_medicament):
        if (isinstance(v_code_medicament, str) and v_code_medicament[:2].isalpha()
                and v_code_medicament[-3:].isnumeric() and len(v_code_medicament) == 6):
            self._code_medicament = v_code_medicament
        else:
            raise ValueError("Le code du médicament doit être composé de 3 lettres au début et 3 chiffres à la fin !")

    @property
    def nom_chimique(self):
        return self._nom_chimique

    @nom_chimique.setter
    def nom_chimique(self, v_nom_chimique):
        if isinstance(v_nom_chimique, str) and len(v_nom_chimique) <= 50:
            self._nom_chimique = v_nom_chimique
        else:
            raise ValueError("Le nom chimique ne doit pas dépasser 50 caractères !")

    @property
    def nom_commercial(self):
        return self._nom_commercial

    @nom_commercial.setter
    def nom_commercial(self, v_nom_commercial):
        if isinstance(v_nom_commercial, str) and len(v_nom_commercial) <= 50:
            self._nom_commercial = v_nom_commercial
        else:
            raise ValueError("Le nom commercial ne doit pas dépasser 50 caractères !")

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, v_prix):
        if isinstance(v_prix, float) and 5.0 <= v_prix <= 100.0:
            self._prix = v_prix
        else:
            raise ValueError("Le prix du médicament doit se situer entre 5 et 100$")

    def __add__(self, medicament):
        """
        Calcule le prix total de deux médicaments
        :param medicament: Le deuxième médicament
        :return: Le prix total des deux médicaments
        """
        prix_total = self.prix + medicament.prix
        return prix_total

    def __str__(self):
        """
        Affiche les informations sur ce médicament
        :return: Les informations du médicament
        """
        return (f"Code du médicament : {self._code_medicament}\n"
                f"Nom chimique : {self._nom_chimique}\n"
                f"Nom commercial : {self._nom_commercial}\n"
                f"Prix : {self._prix}\n"
                f"Catégorie : {self.categorie_medicament}")