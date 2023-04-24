import unittest
from entities.pet import Pet
from repositories.pet_repository import pet_repository


class TestPetRepository(unittest.TestCase):
    def setUp(self):
        pet_repository.delete_all_pets()
        self.pet_mansikki = Pet("Mansikki", "mansikka")

    def test_locate_pet_by_name(self):
        pet_repository.create(self.pet_mansikki)

        pet = pet_repository.locate_pet_by_name(self.pet_mansikki.name)

        self.assertEqual(pet.name, self.pet_mansikki.name)

    def test_create(self):
        pet_repository.create(self.pet_mansikki)

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 1)
        self.assertEqual(all_pets[0].name, self.pet_mansikki.name)

    def test_punish_player(self):
        pet_repository.create(self.pet_mansikki)

        pet_repository.punish_player(self.pet_mansikki.name)

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 0)