
class Voiture:
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix

    def __str__(self):
        return 'Voiture (marque=%s, prix=%s)' % (self.marque, self.prix)
