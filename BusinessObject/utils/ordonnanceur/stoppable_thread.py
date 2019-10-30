import threading


class StoppableThread(threading.Thread):
    """Threading avec fonction stop -> Récupéré ici : https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread"""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
