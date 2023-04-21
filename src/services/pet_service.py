from entities.pet import Pet

from repositories.pet_repository import (
    pet_repository as default_pet_repository
)


class InvalidCredentialsError(Exception):
    pass


class PetNameAlreadyInUseError(Exception):
    pass


class PetService:
    def __init__(self, pet_repository=default_pet_repository):
        self._pet = None
        self._pet_repository = pet_repository

    def adopt_pet(self, name, password, login=True):

        existing_pet = self._pet_repository.locate_pet_by_name(name)

        if existing_pet:
            raise PetNameAlreadyInUseError(f"{name} already exists!")

        pet = self._pet_repository.create(Pet(name, password))

        if login:
            self._pet = pet

        return pet

    def login_pet(self, name, password):

        pet = self._pet_repository.locate_pet_by_name(name)

        if not pet or pet.password != password:
            raise InvalidCredentialsError(
                "Login failed, no such name or invalid password")

        self._pet = pet

        return pet

    def get_current_pet(self):
        return self._pet


pet_service = PetService()
