from IHM.abstract_vue import AbstractVue
from IHM.accueil import Accueil
from Service.voiture_service import VoitureService
from PyInquirer import Separator, prompt, Validator, ValidationError
import regex


class PriceValidator(Validator):
    def validate(self, document) -> None:
        ok = regex.match('^\+?\d[\d ]+\d$', document.text)
        if not ok:
            raise ValidationError(message = 'Please enter a valid phone number', cursor_position = len(document.text))


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
        'default':'Number'
        'validate': PriceValidator
    }
]


voiture_service=VoitureService()

class CreationVoiture(AbstractVue):

    def make_choice(self):
        answers = prompt(questions)
        voiture_service.creer_voiture(
                answers['marque'], answers['prix'])
        return Accueil()