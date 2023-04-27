from entities.pet import Pet
from database_connection import get_database_connection


def locate_pet_by_row(row):
    return Pet(row["name"], row["password"]) if row else None


class PetRepository:
    """Luokka, joka vastaa käyttäjän ja tietokannan välisestä tietojenkäsittelystä.
    """

    def __init__(self, connection):
        """PetRepository-luokan konstruktori.

        Args:
            connection: Tietokantayhteys.
        """
        self._connection = connection

    def create(self, pet):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO pets (name, password) VALUES (?, ?);",
            (pet.name, pet.password)
        )

        self._connection.commit()

        return pet

    def locate_pet_by_name(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM pets WHERE name = ?;",
            (name,)
        )

        row = cursor.fetchone()

        return locate_pet_by_row(row)

    def punish_player(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name = ?;",
            (name,)
        )

        self._connection.commit()

    def cleanup_data(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name IS NULL OR TRIM(name) = '';"
        )

        self._connection.commit()

    def delete_all_pets(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM pets;")

        self._connection.commit()

    def locate_all_pets(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM pets;")

        rows = cursor.fetchall()

        return list(map(locate_pet_by_row, rows))


pet_repository = PetRepository(get_database_connection())
