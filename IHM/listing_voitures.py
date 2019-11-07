from PyInquirer import Separator, prompt

from IHM.abstract_vue import AbstractVue
from Service.utils.variables import global_vars
import time

questions = [
    {
        'type': 'list',
        'name': 'choix',
        'message': 'Quel est votre choix',
        'choices': [
            str(global_vars.voitures),
            Separator(),
            'Ajouter une voiture',
            Separator(),
            'Quitter'
        ]
    }
]


class Listing(AbstractVue):

    def display_info(self):
        """ map(lambda x:print(x), voitures)"""
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):

        answers = prompt(questions)
        time.sleep(10)
        from IHM.accueil import Accueil
        return Accueil()
