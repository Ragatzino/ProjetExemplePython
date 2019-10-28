import psycopg2
import DAO.resources.connexion.properties as properties

def get_connection():
    return psycopg2.connect(host=properties.db_host, port=properties.db_port,database=properties.db_database, user=properties.db_id, password=properties.db_password)