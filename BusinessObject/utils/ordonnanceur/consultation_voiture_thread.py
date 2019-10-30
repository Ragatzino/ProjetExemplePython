from BusinessObject.utils.ordonnanceur.stoppable_thread import StoppableThread
from DAO.main.VoitureDao import VoitureDAO
import time

class ConsultationVoitureThread(StoppableThread):
    def run(self):
        global voitures
        while not self.stopped():
            time.sleep(20)
            voitures = VoitureDAO.find_all()
