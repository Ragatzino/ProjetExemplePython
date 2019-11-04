from IHM.abstract_vue import AbstractVue
from Service.voiture_service import VoitureService
from PyInquirer import prompt, Validator, ValidationError
import regex


class PriceValidator(Validator):
    def validate(self, document) -> None:
        ok = regex.match('^\+?\d[\d ]+\d$', document.text)
        if not ok:
            raise ValidationError(message='Please enter a number', cursor_position=len(document.text))


questions = [
    {
        'type': 'input',
        'name': 'marque',
        'message': 'Quel sera sa marque',

    },
    {
        'type': 'input',
        'name': 'mot de passe',
        'message': 'Quel son prix',
        'default': 'Number',
        'validate': PriceValidator
    }
]

voiture_service = VoitureService()


class CreationVoiture(AbstractVue):

    def make_choice(self):
        from IHM.accueil import Accueil
        answers = prompt(questions)
        voiture_service.creer_voiture(
            answers['marque'], answers['prix'])
        return Accueil()
