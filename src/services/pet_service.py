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

    def adopt_pet(self, name, password, progress, pet_img, login=True):
        """Luo uuden lemmikin. Kirjaa myös sisään tarvittaessa.

        Args:
            name (str): Lemmikin nimi.
            password (str): Lemmikin salasana.
            progress (int): Lemmikin rakkausmittarin arvo.
            pet_img (str): Lemmikin kuvan nimi.
            login (bool): Oletuksena True. Kirjaa lemmikin sisään, jos adoptointi onnistuu.

        Raises:
            PetNameAlreadyInUseError: Virhe. Tapahtuu kun luodaan lemmikki, jonka nimi on käytössä.

        Returns:
            olio: Pet-olio luodusta lemmikistä. 
        """

        existing_pet = self._pet_repository.locate_pet_by_name(name)

        if existing_pet:
            raise PetNameAlreadyInUseError(f"{name} already exists!")

        pet = self._pet_repository.create(
            Pet(name, password, progress, pet_img))

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

    def get_progress(self):
        """Palauttaa lemmikin rakkausmittarin arvon.

        Returns:
            int tai None: Lemmikin rakkausmittarin edistystä kuvaava arvo.
        """
        return self._pet.progress

    def save_progress(self, progress, name):
        """Tallentaa lemmikin rakkausmittarin edistyksen tietokantaan ja lemmikin olioon.

        Args:
            progress (int): Lemmikin rakkausmittarin edistystä kuvaava arvo.
            name (str): Lemmikin nimi.
        """
        self._pet_repository.save_progress(progress, name)
        self._pet.progress = progress

    def get_pet_img(self, value):
        """Palauttaa käyttäjän valitseman lemmikin kuvan nimen.

        Args:
            value (int): Muuttuja, joka saa arvokseen käyttäjän valitseman kuvan tunnisteen.

        Returns:
            str: Value-muuttujaa vastaava lemmikin kuva.
        """
        if value == 1:
            image_name = "Rotta_Otus_300x300.png"
        if value == 2:
            image_name = "Homo_Rotta_Otus_300x300.png"
        if value == 3:
            image_name = "Ace_Rotta_Otus_300x300.png"
        if value == 0:
            return
        return image_name


pet_service = PetService()
