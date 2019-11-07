from BusinessObject.utils.ordonnanceur.stoppable_thread import StoppableThread
from Service.main.voiture_service import VoitureService
from Service.utils.variables import global_vars
import time


class ConsultationVoitureThread(StoppableThread):

    def run(self):
        voitureService = VoitureService()
        while not self.stopped():
            print(global_vars.voitures)
            global_vars.voitures = voitureService.trouver_voitures()
            print(global_vars.voitures)
            time.sleep(20)
