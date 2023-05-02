from entities.pet import Pet

from repositories.pet_repository import (
    pet_repository as default_pet_repository
)


class InvalidCredentialsError(Exception):
    pass


class PetNameAlreadyInUseError(Exception):
    pass


class PetService:
    """Luokka, joka vastaa käyttäjän ja tietokannan välisestä toiminnallisuudesta.
    """

    def __init__(self, pet_repository=default_pet_repository):
        """Luokan konstruktori, jossa luodaan määritellystä toiminnallisuudesta vastaava palvelu.

        Args:
            pet_repository (olio): Olio, jolla on PetRepository-luokan metodit.
        """
        self._pet = None
        self._pet_repository = pet_repository

    def adopt_pet(self, name, password, login=True):
        """Luo uuden lemmikin. Kirjaa myös sisään tarvittaessa.

        Args:
            name (str): Lemmikin nimi.
            password (str): Lemmikin salasana.
            login (bool): Oletuksena True. Kirjaa lemmikin sisään, jos adoptointi onnistuu.

        Raises:
            PetNameAlreadyInUseError: Virhe. Tapahtuu kun luodaan lemmikki, jonka nimi on käytössä.

        Returns:
            olio: Pet-olio luodusta lemmikistä. 
        """

        existing_pet = self._pet_repository.locate_pet_by_name(name)

        if existing_pet:
            raise PetNameAlreadyInUseError(f"{name} already exists!")

        pet = self._pet_repository.create(Pet(name, password))

        if login:
            self._pet = pet

        return pet

    def login_pet(self, name, password):
        """Kirjaa lemmikin sisään.

        Args:
            name (str): Lemmikin nimi.
            password (str): Lemmikin salasana.

        Raises:
            InvalidCredentialsError: Jos nimi ja salasana eivät ole oikein tapahtuva virhe.

        Returns:
            olio: Palauttaa sisään kirjatun lemmikin Pet-olion.
        """

        pet = self._pet_repository.locate_pet_by_name(name)

        if not pet or pet.password != password:
            raise InvalidCredentialsError(
                "Login failed, no such name or invalid password")

        self._pet = pet

        return pet

    def get_current_pet(self):
        """Palauttaa lemmikin, joka on kirjattu sisään.

        Returns:
            olio: Palauttaa sisään kirjatun lemmikin Pet-olion.
        """
        return self._pet

    def logout(self):
        """Kirjaa ulos lemmikin, joka on kirjattu sisään.
        """

        self._pet = None


pet_service = PetService()
