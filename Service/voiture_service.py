from DAO.main.VoitureDao import VoitureDAO
from BusinessObject.main.Voiture import Voiture


class VoitureService():
    def creer_voiture(self, marque, prix):
        return VoitureDAO.create(self, Voiture(marque, prix))
