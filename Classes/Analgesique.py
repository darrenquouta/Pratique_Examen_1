from Classes.Medicament import Medicament
from Classes.Patient import Patient
from Classes.Fournisseur import Fournisseur


class Analgesique(Medicament):

    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "", p_nom_commercial: str = "",
                 p_prix: float = 0.0, p_categorie_medicament: str = "",
                 p_liste_patients_achete: list[Patient] = None, p_fournisseur: Fournisseur = None,
                 p_prise_quotidienne_maximale: int = 0):
        """
        Constructeur de la classe Analgesique
        :param p_code_medicament: Code du médicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Le prix du médicament
        :param p_categorie_medicament: La catégorie du médicament
        :param p_liste_patients_achete: La liste des patients qui ont acheté ce médicament
        :param p_fournisseur: Le fournisseur de ce médicament
        :param p_prise_quotidienne_maximale: La prise quotidienne maximale de pilules
        """
        self._prise_quotidienne_maximale = p_prise_quotidienne_maximale
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix,
                            p_categorie_medicament, p_liste_patients_achete, p_fournisseur)

    @property
    def prise_quotidienne_maximale(self):
        return self._prise_quotidienne_maximale

    @prise_quotidienne_maximale.setter
    def prise_quotidienne_maximale(self, v_prise_quotidienne_maximale):
        if isinstance(v_prise_quotidienne_maximale, int) and v_prise_quotidienne_maximale > 0:
            self._prise_quotidienne_maximale = v_prise_quotidienne_maximale

    def __str__(self):
        """
        Affiche les informations sur le médicament
        :return: Les informations sur le médicament
        """
        return (f"Code du médicament : {self._code_medicament}\n"
                f"Nom chimique : {self._nom_chimique}\n"
                f"Nom commercial : {self._nom_commercial}\n"
                f"Prix : {self._prix}\n"
                f"Catégorie : {self._categorie_medicament}\n"
                f"Prise quotidienne maximale : {self._prise_quotidienne_maximale} pilules par jour")
