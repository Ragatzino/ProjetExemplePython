from DAO.resources.connexion.connection import get_connection


if __name__ == '__main__':
    connection = get_connection()
    cursor = connection.cursor()

    name_Table = "voitures"

    # Creation des tables

    cursor.execute(open("drop.sql", "r").read())

    connection.commit()

