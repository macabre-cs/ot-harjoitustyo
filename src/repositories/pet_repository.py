from entities.pet import Pet
from database_connection import get_database_connection


def locate_pet_by_row(row):
    return Pet(row["name"], row["password"]) if row else None


class PetRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, pet):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO pets (name, password) VALUES (?, ?)",
            (pet.name, pet.password)
        )

        self._connection.commit()

        return pet

    def locate_pet_by_name(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM pets WHERE name = ?",
            (name,)
        )

        row = cursor.fetchone()

        return locate_pet_by_row(row)

    def punish_player(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name = ?",
            (name,)
        )

        self._connection.commit()

    def cleanup_data(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name IS NULL OR TRIM(name) = '';"
        )

        self._connection.commit()


pet_repository = PetRepository(get_database_connection())
