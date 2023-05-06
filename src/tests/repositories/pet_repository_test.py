import unittest
from entities.pet import Pet
from repositories.pet_repository import pet_repository


class TestPetRepository(unittest.TestCase):
    def setUp(self):
        pet_repository.delete_all_pets()
        self.pet_mansikki = Pet("Mansikki", "mansikka",
                                0, "Rotta_Otus_300x300.png")
        self.pet_omenikki = Pet("Omenikki", "omena", 0,
                                "Rotta_Otus_300x300.png")

    def test_locate_pet_by_name(self):
        pet_repository.create(self.pet_mansikki)

        pet = pet_repository.locate_pet_by_name(self.pet_mansikki.name)

        self.assertEqual(pet.name, self.pet_mansikki.name)

    def test_create(self):
        pet_repository.create(self.pet_mansikki)

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 1)
        self.assertEqual(all_pets[0].name, self.pet_mansikki.name)
        self.assertEqual(all_pets[0].password, self.pet_mansikki.password)

    def test_punish_player(self):
        pet_repository.create(self.pet_mansikki)

        pet_repository.punish_player(self.pet_mansikki.name)

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 0)

    def test_locate_all_pets(self):
        pet_repository.create(self.pet_omenikki)
        pet_repository.create(self.pet_mansikki)

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 2)
        self.assertEqual(all_pets[0].name, self.pet_omenikki.name)
        self.assertEqual(all_pets[0].password, self.pet_omenikki.password)
        self.assertEqual(all_pets[1].name, self.pet_mansikki.name)
        self.assertEqual(all_pets[1].password, self.pet_mansikki.password)

    def test_delete_all_pets(self):
        pet_repository.create(self.pet_omenikki)
        pet_repository.create(self.pet_mansikki)

        pet_repository.delete_all_pets()

        all_pets = pet_repository.locate_all_pets()

        self.assertEqual(len(all_pets), 0)
