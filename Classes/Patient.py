from datetime import datetime
from datetime import date

class Patient:
    liste_patients = []

    def __init__(self, p_numero_patient: str = "", p_nom_famille: str = "", p_prenom: str = "",
                 p_date_naissance: datetime = "", p_liste_medicaments_achete: list = None):
        """
        Constructeur de la classe Patient
        :param p_numero_patient: Le numéro du patient
        :param p_nom_famille: Le nom de famille du patient
        :param p_prenom: Le prénom du patient
        :param p_date_naissance: La date de naissance du patient
        :param p_liste_medicaments_achete: La liste de médicaments acheté par le patient
        """
        self._numero_patient = p_numero_patient
        self._nom_famille = p_nom_famille
        self._prenom = p_prenom
        self._date_naissance = p_date_naissance
        if p_liste_medicaments_achete is None:
            self.liste_medicaments_achete = []
        else:
            self.liste_medicaments_achete = p_liste_medicaments_achete

    @property
    def numero_patient(self):
        return self._numero_patient

    @numero_patient.setter
    def numero_patient(self, v_numero_patient):
        if isinstance(v_numero_patient, str) and len(v_numero_patient) == 7 and v_numero_patient.isnumeric():
            premier_chiffre = int(v_numero_patient[0])
            if premier_chiffre == 0:
                self._numero_patient = v_numero_patient
            elif premier_chiffre % 2 == 0:
                self._numero_patient = v_numero_patient
        else:
            raise ValueError("Le numéro du patient doit être de 7 chiffres et le premier doit être pair !")

    @property
    def nom_famille(self):
        return self._nom_famille

    @nom_famille.setter
    def nom_famille(self, v_nom_famille):
        if isinstance(v_nom_famille, str) and len(v_nom_famille) <= 50:
            self._nom_famille = v_nom_famille
        else:
            raise ValueError("Le nom de famille du patient ne doit pas dépasser 50 caractères !")

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, v_prenom):
        if isinstance(v_prenom, str) and len(v_prenom) <= 50:
            self._prenom = v_prenom
        else:
            raise ValueError("Le prénom du patient ne doit pas dépasser 50 caractères !")

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, v_date_naissance):
        if isinstance(v_date_naissance, date):
            self._date_naissance = v_date_naissance
        else:
            raise ValueError("La date de naissance du patient doit être valide !")

    def _calculer_age(self):
        """
        Calcule l'âge du patient
        :return: L'âge du patient en années
        """
        age = int(datetime.now().year - self.date_naissance.year)
        if self.date_naissance.month > datetime.now().month:
            age = age - 1
            return age
        elif self.date_naissance.month == datetime.now().month:
            if self.date_naissance.day > datetime.now().day:
                age = age - 1
                return age
            else:
                return age
        else:
            return age

    def est_adulte(self):
        """
        Retourne True si le patient est adulte, False s'il ne l'est pas
        :return: True si le patient est adulte, False s'il ne l'est pas
        """
        age = self._calculer_age()
        if age >= 18:
            return True
        else:
            return False

    def afficher_medicament(self):
        """
        Affiche les informations sur le médicament acheté par le patient
        :return: Les informations sur le médicament
        """
        for medicament in self.liste_medicaments_achete:
            print(f"Code du médicament : {medicament.code_medicament}\n"
                  f"Nom chimique : {medicament.nom_chimique}\n"
                  f"Nom commercial : {medicament.nom_commercial}\n"
                  f"Prix : {medicament.prix}\n")

    def ajouter_medicament(self, medicament_ajouter):
        """
        Ajoute un médicament dans la liste des médicaments achetés par le patient
        :param medicament_ajouter: Un médicament
        :return: None
        """
        for medicament in self.liste_medicaments_achete:
            if medicament.code_medicament == medicament_ajouter.code_medicament:
                break
        else:
            self.liste_medicaments_achete.append(medicament_ajouter)

    def supprimer_medicament(self, medicament_supprimer):
        """
        Supprime un médicament de la liste des médicaments achetés par le patient
        :param medicament_supprimer: Le médicament à supprimer
        :return: None
        """
        for medicament in self.liste_medicaments_achete:
            if medicament.code_medicament == medicament_supprimer.code_medicament:
                self.liste_medicaments_achete.remove(medicament)
                return None
