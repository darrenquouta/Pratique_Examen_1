from Classes.Medicament import Medicament
from Classes.Patient import Patient
from Classes.Fournisseur import Fournisseur

class Corticoide(Medicament):

    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "",
                 p_prix: float = 0.0, p_categorie_medicament: str = "",
                 p_liste_patients_achete: list[Patient] = None, p_fournisseur: Fournisseur = None,
                 p_effet_medicament: str = ""):
        """
        Constructeur de la classe Medicament
        :param p_code_medicament: Code du médicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Le prix du médicament
        :param p_categorie_medicament: La catégorie du médicament
        :param p_liste_patients_achete: La liste des patients qui ont acheté ce médicament
        :param p_fournisseur: Le fournisseur de ce médicament
        :param p_effet_medicament: L'effet du médicament [Cours/Intermédaire/Prolongé]
        """
        self.effet_medicament = p_effet_medicament
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix,
                            p_categorie_medicament, p_liste_patients_achete, p_fournisseur)

    def __str__(self):
        """
        Affiche les informations sur le médicament
        :return: Les informations sur le médicament
        """
        return (f"Code du médicament : {self._code_medicament}\n"
                f"Nom chimique : {self._nom_chimique}\n"
                f"Nom commercial : {self._nom_commercial}\n"
                f"Prix : {self._prix}\n"
                f"Catégorie : {self.categorie_medicament}\n"
                f"Effet du médicament : {self.effet_medicament}")

