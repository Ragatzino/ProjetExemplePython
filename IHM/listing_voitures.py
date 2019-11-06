from IHM.abstract_vue import AbstractVue
from Service.voiture_service import VoitureService
import time
from BusinessObject.utils.ordonnanceur.consultation_voiture_thread import ConsultationVoitureThread


class Listing(AbstractVue):
    voiture_service = VoitureService()
    voitures=voiture_service.trouver_voitures()
    questions = [
        {
            'type': 'list',
            'name': 'choix',
            'message': 'Quel est votre choix',
            'choices': [
                'Quitter'
            ]
        }
    ]

    def display_info(self):
        """ map(lambda x:print(x), voitures)"""
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        time.sleep(10)
        from IHM.accueil import Accueil
        return Accueil()
