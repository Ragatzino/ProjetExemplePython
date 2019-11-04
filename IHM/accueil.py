from IHM.listing_voitures import Listing
from IHM.creation_voiture import CreationVoiture
from IHM.abstract_vue import AbstractVue
from PyInquirer import Separator, prompt


questions = [
    {
        'type': 'list',
        'name': 'choix',
        'message': 'Quel est votre choix',
        'choices': [
            'Consulter la liste des voitures',
            Separator(),
            'Ajouter une voiture',
            Separator(),
            'Quitter'
        ]
    }
]


class Accueil(AbstractVue):

    def display_info(self):
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(questions)
        if reponse['choix'] == 'Consulter la liste des voitures':
            return Listing()
        elif reponse['choix'] == 'Ajouter une voiture':
            return CreationVoiture()
        else:
            print("programme terminé")