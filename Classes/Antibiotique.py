from Classes.Medicament import Medicament
from Classes.Patient import Patient
from Classes.Fournisseur import Fournisseur

class Antibiotique(Medicament):

    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "",
                 p_prix: float = 0.0, p_categorie_medicament: str = "",
                 p_liste_patients_achete: list[Patient] = None, p_fournisseur: Fournisseur = None,
                 p_duree_prise_maximale: int = 0):
        """
        Constructeur de la classe Antibiotique
        :param p_code_medicament: Code du médicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Le prix du médicament
        :param p_categorie_medicament: La catégorie du médicament
        :param p_liste_patients_achete: La liste des patients qui ont acheté ce médicament
        :param p_fournisseur: Le fournisseur de ce médicament
        :param p_duree_prise_maximale: La durée de prise maximale de ce médicament en jours
        """
        self._duree_prise_maximale = p_duree_prise_maximale
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie_medicament,
                            p_liste_patients_achete, p_fournisseur)

    @property
    def duree_prise_maximale(self):
        return self._duree_prise_maximale

    @duree_prise_maximale.setter
    def duree_prise_maximale(self, v_duree_prise_maximale):
        if isinstance(v_duree_prise_maximale, int) and v_duree_prise_maximale > 0:
            self._duree_prise_maximale = v_duree_prise_maximale
        else:
            raise ValueError("La durée de prise maximale doit être un nombre entier !")

    def __str__(self):
        """
        Affiche les informations sur l'antibiotique
        :return: Les informations sur l'antibiotique
        """
        return (f"Code du médicament : {self._code_medicament}\n"
                f"Nom chimique : {self._nom_chimique}\n"
                f"Nom commercial : {self._nom_commercial}\n"
                f"Prix : {self._prix}\n"
                f"Catégorie : {self.categorie_medicament}"
                f"Durée du prise maximale : {self._duree_prise_maximale} jours")