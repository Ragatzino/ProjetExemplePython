from DAO.resources.connexion.connection import get_connection


if __name__ == '__main__':
    connection = get_connection()
    cursor = connection.cursor()

    name_Table = "voitures"

    # Creation des tables

    cursor.execute(open("tableCreation.sql", "r").read())

    connection.commit()

    # Remplissage des tables

    cursor.execute(open("script.sql", "r").read())

    connection.commit()

