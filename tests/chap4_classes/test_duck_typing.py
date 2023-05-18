from unittest import TestCase

from src.chap4_classes.duck_typing import Duck, ElectricToy, Goose

DUCK_QUACK = "Quack!"


class DuckTyping(TestCase):
    def test_a_duck_SHOULD_quack(self):
        self._should_quack(Duck())

    def test_a_Goose_SHOULD_quack_SINCE_it_is_also_a_duck(self):
        self._should_quack(Goose())

    def test_an_electric_toy_SHOULD_quack_WHEN_it_is_duck_typing_a_duck(self):
        self._should_quack(ElectricToy())

    def test_a_goose_SHOULD_swim_like_a_duck(self):
        self.assertEqual(Duck().swim(), Goose().swim())

    def test_an_electric_toy_SHOULD_NOT_swim_like_a_duck(self):
        self.assertNotEqual(ElectricToy().swim(), Duck().swim())

    def test_a_goose_SHOULD_NOT_look_like_a_duck(self):
        self.assertNotEqual(Goose().color(), Duck().color())

    def test_an_electric_toy_SHOULD_look_like_a_duck(self):
        self.assertEqual(ElectricToy().color(), Duck().color())

    def test_an_electric_toy_SHOULD_have_batteries(self):
        self.assertTrue(ElectricToy().has_batteries())

    def test_real_ducks_SHOULD_NOT_have_batteries(self):
        self.assertFalse(hasattr(Duck(), 'has_batteries'))
        self.assertFalse(hasattr(Goose(), 'has_batteries'))

    def _should_quack(self, duck):
        self.assertEqual(duck.quack(), DUCK_QUACK)
