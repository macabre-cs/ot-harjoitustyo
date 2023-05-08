import unittest
from entities.pet import Pet
from services.pet_service import (
    PetService, InvalidCredentialsError, PetNameAlreadyInUseError)


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

    def locate_pet_by_name(self, name):
        matching_pets = filter(lambda pet: pet.name == name, self.pets)

        matching_pets_list = list(matching_pets)

        return matching_pets_list[0] if len(matching_pets_list) > 0 else None


class TestPetService(unittest.TestCase):
    def setUp(self):
        self.pet_service = PetService(MockPetRepository())
        self.pet_mustikki = Pet("Mustikki", "mustikka",
                                0, "Rotta_Otus_300x300.png")
        self.pet_karvikki = Pet("Karvikki", "karviainen",
                                0, "Ace_Rotta_Otus_300x300.png")

    def login_test_pet(self, pet):
        self.pet_service.adopt_pet(
            pet.name, pet.password, 0, pet.image)

    def test_locate_current_pet(self):
        self.login_test_pet(self.pet_mustikki)

        current_pet = self.pet_service.get_current_pet()

        self.assertEqual(current_pet.name, self.pet_mustikki.name)

    def test_valid_login(self):
        self.pet_service.adopt_pet(
            self.pet_mustikki.name, self.pet_mustikki.password, 0, "Rotta_Otus_300x300.png")

        pet = self.pet_service.login_pet(
            self.pet_mustikki.name, self.pet_mustikki.password)

        self.assertEqual(pet.name, self.pet_mustikki.name)

    def test_invalid_login(self):
        self.assertRaises(InvalidCredentialsError,
                          self.pet_service.login_pet, "kanan", "muna")

    def test_adopt_pet_that_exists(self):
        name = self.pet_mustikki.name

        self.pet_service.adopt_pet(
            name, "mustikkavale", 0, "Rotta_Otus_300x300.png")

        self.assertRaises(PetNameAlreadyInUseError,
                          self.pet_service.adopt_pet, name, "valemustikka", 0, "Rotta_Otus_300x300.png")

    def test_logout(self):
        self.pet_service.adopt_pet(
            self.pet_mustikki.name, self.pet_mustikki.password, 0, "Rotta_Otus_300x300.png")

        pet = self.pet_service.login_pet(
            self.pet_mustikki.name, self.pet_mustikki.password)

        pet = self.pet_service.logout()

        self.assertEqual(None, pet)

    def test_progres_at_start_is_zero(self):
        self.pet_service.adopt_pet(
            self.pet_mustikki.name, self.pet_mustikki.password, 0, "Rotta_Otus_300x300.png")

        pet = self.pet_service.login_pet(
            self.pet_mustikki.name, self.pet_mustikki.password)

        self.assertEqual(0, pet.progress)

    def test_get_progress(self):
        self.pet_service.adopt_pet(
            self.pet_mustikki.name, self.pet_mustikki.password, 0, "Rotta_Otus_300x300.png")

        pet = self.pet_service.login_pet(
            self.pet_mustikki.name, self.pet_mustikki.password)

        current_progress = self.pet_service.get_progress()

        self.assertEqual(current_progress, pet.progress)

    def test_get_trans_pet_img(self):
        self.login_test_pet(self.pet_mustikki)

        img_name = self.pet_service.get_pet_img(1)

        self.assertEqual(img_name, self.pet_mustikki.image)

    def test_get_ace_pet_img(self):
        self.login_test_pet(self.pet_karvikki)

        img_name = self.pet_service.get_pet_img(3)

        self.assertEqual(img_name, self.pet_karvikki.image)

    def test_value_gives_correct_img(self):
        self.login_test_pet(self.pet_karvikki)

        img_name = self.pet_service.get_pet_img(2)

        self.assertNotEqual(img_name, self.pet_karvikki.image)
