from BusinessObject.utils.ordonnanceur.stoppable_thread import StoppableThread
from DAO.main.VoitureDao import VoitureDAO
import time

class ConsultationVoitureThread(StoppableThread):

    def __init__(self,voitures):
        self.voitures=voitures

    def run(self):
        while not self.stopped():
            self.voitures = VoitureDAO.find_all()
            time.sleep(20)

    def get_voitures(self):
        return self.voitures