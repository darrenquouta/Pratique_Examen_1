from Classes.Patient import Patient
import jsonpickle

class Fournisseur:
    liste_fournisseurs = []
    nb_fournisseurs = 0

    def __init__(self, p_code_fournisseur: str = "", p_nom_compagnie: str = "", p_liste_medicaments_fourni: list = None,
                 p_liste_patients: list[Patient] = []):
        """
        Constructeur de la classe Fournisseur
        :param p_code_fournisseur: Code du fournisseur
        :param p_nom_compagnie: Nom de la compagnie pharmaceutique
        :param p_liste_medicaments_fourni: La liste des médicaments fournis par la compagnie
        :param p_liste_patients: La liste des patients qui consomment les produits du fournisseur
        """
        self._code_fournisseur = p_code_fournisseur
        self._nom_compagnie = p_nom_compagnie
        if p_liste_medicaments_fourni is None:
            self.liste_medicaments_fourni = []
        else:
            self.liste_medicaments_fourni = p_liste_medicaments_fourni
        if p_liste_patients is None:
            self.liste_patients = []
        else:
            self.liste_patients = p_liste_patients
        Fournisseur.nb_fournisseurs += 1
        Fournisseur.liste_fournisseurs.append(self)

    @property
    def code_fournisseur(self):
        return self._code_fournisseur

    @code_fournisseur.setter
    def code_fournisseur(self, v_code_fournisseur):
        if (isinstance(v_code_fournisseur, str) and len(v_code_fournisseur) == 7 and v_code_fournisseur[0].isalpha()
                and v_code_fournisseur[1] == "-" and v_code_fournisseur[2:].isnumeric()):
            self._code_fournisseur = v_code_fournisseur
        else:
            raise ValueError(
                "Le code du fournisseur doit commencer par une lettre, suivit par un tiret et 5 chiffres !")

    @property
    def nom_compagnie(self):
        return self._nom_compagnie

    @nom_compagnie.setter
    def nom_compagnie(self, v_nom_compagnie):
        if isinstance(v_nom_compagnie, str) and len(v_nom_compagnie) <= 30 and v_nom_compagnie.isalpha():
            self._nom_compagnie = v_nom_compagnie
        else:
            raise ValueError("La longueur du nom de la compagnie ne peut pas dépasser 30 caractères !")

    def serialiser_fournisseur(self, nom_fichier):
        """
        Sérialise un objet fournisseur dans un fichier .json
        :param nom_fichier: Le nom du fichier donné
        :return: False si la sérialisation échoue
        """
        try:
            with open(nom_fichier, "w") as file:
                file.write(jsonpickle.encode(self))
        except OSError:
            return False

    @staticmethod
    def deserialiser_fournisseur(nom_fichier):
        """
        Désérialise un objet de type fournisseur
        :param nom_fichier: Le nom du fichier à désérialiser
        :return: False si la désérialisation échoue
        """
        try:
            with open(nom_fichier, "w") as file:
                dataFournisseur = file.read()
                fournisseur = jsonpickle.decode(dataFournisseur)
                return fournisseur
        except OSError:
            return False

    def ajouter_medicament_patient(self, numero_patient, medicament):
        """
        Ajoute un médicament à un patient
        :param numero_patient: Le numéro du patient recherché
        :param medicament: Le médicament à ajouter
        :return: None
        """
        for patient in self.liste_patients:
            if patient.numero_patient == numero_patient:
                patient.liste_medicaments_achete.append(medicament)
                break

    @classmethod
    def afficher_liste_fournisseurs(cls):
        """
        Affiche tous les fournisseurs
        :return: None
        """
        for fournisseur in cls.liste_fournisseurs:
            print(f"Code du fournisseur : {fournisseur._code_fournisseur}\n"
                  f"Nom de la compagnie : {fournisseur._nom_compagnie}\n")

    def __str__(self):
        """
        Affiche les informations sur un fournisseur
        :return: Les informations sur un fournisseur
        """
        return (f"Code du fournisseur : {self._code_fournisseur}\n"
                f"Nom de la compagnie : {self._nom_compagnie}")