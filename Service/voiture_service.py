import json
from DAO.main.VoitureDao import VoitureDAO
from BusinessObject.main.Voiture import Voiture


class VoitureService():

    def creer_voiture(self, marque, prix):
        voitureDao = VoitureDAO()
        voiture = Voiture(marque, prix)
        return voitureDao.create(voiture)

    def trouver_voitures(self):
        voitureDao = VoitureDAO()
        voitures = voitureDao.find_all()
        return voitures

    def get_voitures_names(self, voitures):
        tab=[]
        for names in voitures:
            tab+=names
        return tab

    def get_voitures_from_marque(self, name):
        voitures
        return
