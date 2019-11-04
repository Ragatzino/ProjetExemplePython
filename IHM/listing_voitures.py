from IHM.abstract_vue import AbstractVue
"""  from BusinessObject.utils.ordonnanceur.consultation_voiture_thread import ConsultationVoitureThread"""


class Listing(AbstractVue):
    """  def __init__(self):
      global voitures
        self.ordonnanceur = ConsultationVoitureThread()
        self.ordonnanceur.start()"""

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
        with open('assets/error.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        from IHM.accueil import Accueil
        self.ordonnanceur.stop()
        return Accueil()
