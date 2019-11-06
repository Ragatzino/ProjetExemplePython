import psycopg2

from DAO.main.abstract_dao import AbstractDao
from BusinessObject.main.Voiture.Voiture import Voiture

class VoitureDAO(AbstractDao):
    def create(self, voiture):
        cur = AbstractDao.connection.cursor()
        try:
            cur.execute(
                "insert into voiture(marque, prix) values (%s,%s)",
                    (voiture.marque, voiture.prix))
            AbstractDao.connection.commit()

        except psycopg2.Error as e:
                AbstractDao.connection.rollback()
                raise e
        finally:
                cur.close()

    def get_voiture_from_marque(self,marque):
        cur = AbstractDao.connection.cursor()
        try:
            cur.execute(
                "select marque, prix from voiture where marque = %s)",marque)
            found=cur.fetchone()
            if found:
                return Voiture(found[1],found[2])
            return None

        except psycopg2.Error as e:
            AbstractDao.connection.rollback()
            raise e
        finally:
            cur.close()

    def find_all(self):
        cur = AbstractDao.connection.cursor()
        try:
            cur.execute(
                "select * from voiture")
            found=cur.fetchall()
            if found:
                return Voiture(found[1],found[2])
            return None

        except psycopg2.Error as e:
            AbstractDao.connection.rollback()
            raise e
        finally:
            cur.close()