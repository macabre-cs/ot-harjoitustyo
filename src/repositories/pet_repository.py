from entities.pet import Pet
from database_connection import get_database_connection


def locate_pet_by_row(row):
    return Pet(row["name"], row["password"], row["progress"], row["image"]) if row else None


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
        """Tallentaa lemmikin tietokantaan.

        Args:
            pet (olio): Pet-olio, joka tallennetaan tietokantaan.

        Returns:
            olio: Pet-oliona tallennettu lemmikki
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO pets (name, password, progress, image) VALUES (?, ?, ?, ?);",
            (pet.name, pet.password, pet.progress, pet.image)
        )

        self._connection.commit()

        return pet

    def locate_pet_by_name(self, name):
        """Etsii lemmikin tietokannasta lemmikin nimellä.

        Args:
            name (str): Lemmikin nimi, jonka Pet-olio palautetaan.

        Returns:
            Pet-olio, jos lemmikki löytyy tietokannasta. Jos ei löydy palautetaan None.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM pets WHERE name = ?;",
            (name,)
        )

        row = cursor.fetchone()

        return locate_pet_by_row(row)

    def punish_player(self, name):
        """Etsii pelaajan nykyisen lemmikin nimellä lemmikin, joka poistetaan tietokannasta.

        Args:
            name (str): Lemmikin nimi.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name = ?;",
            (name,)
        )

        self._connection.commit()

    def cleanup_data(self):
        """Kutsutaan jos lemmikki poistetaan tietokannasta. Poistaa tietokannasta tyhjän rivin.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE name IS NULL OR TRIM(name) = '';"
        )

        self._connection.commit()

    def delete_all_pets(self):
        """Poistaa kaikki lemmikit tietokannasta.
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM pets;")

        self._connection.commit()

    def locate_all_pets(self):
        """Etsii kaikki lemmikit tietokannasta.

        Returns:
            list: Palauttaa listan Pet-olioita.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM pets;")

        rows = cursor.fetchall()

        return list(map(locate_pet_by_row, rows))

    def save_progress(self, progress, name):
        """Tallentaa lemmikin rakkausmittarin tilan tietokantaan.

        Args:
            progress (int): Lemmikin rakkausmittarin edistystä kuvaava arvo.
            name (str): Lemmikin nimi
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE pets SET progress=? WHERE name=?;", (progress, name))

        self._connection.commit()


pet_repository = PetRepository(get_database_connection())
