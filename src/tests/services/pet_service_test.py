import unittest
from entities.pet import Pet
from services.pet_service import (
    PetService)


class MockPetRepository:
    def __init__(self, pets=None):
        self.pets = pets or []

    def locate_all_pets(self):
        return self.pets

    def create(self, pet):
        self.pets.append(pet)

        return pet

    def delete_all_pets(self):
        self.pets = []

    def locate_pet_by_name(self, pet_name):
        matching_pets = [match for match in self.pets if pet_name == match]

        return matching_pets[0] if len(matching_pets) > 0 else None


class TestPetService(unittest.TestCase):
    def setUp(self):
        self.pet_service = PetService(MockPetRepository())
        self.pet_mustikki = Pet("Mustikki", "mustikka")

    def login_test_pet(self, pet):
        self.pet_service.adopt_pet(pet.name, pet.password)

    def test_locate_current_pet(self):
        self.login_test_pet(self.pet_mustikki)

        current_pet = self.pet_service.get_current_pet()

        self.assertEqual(current_pet.name, self.pet_mustikki.name)
