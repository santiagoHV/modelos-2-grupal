import unittest

from species.Ogro import Ogro

from species.Elfo import Elfo
from species.Imperial import Imperial
from species.Breton import Breton

class TestSpecies(unittest.TestCase):

    def test_elfo_live(self):
        elfo = Elfo('legolas',70,1.90,2000)
        assert 2000 == elfo.live


    def test_elfo_attack(self):
        elfo = Elfo('legolas',70,1.90,2000)
        assert 200 == elfo.attack


    def test_create_imperial(self):
        imperial = Imperial('Manin',78,1.67,52)
        assert 350 == imperial.attack
        assert 2500 == imperial.live


    def test_create_breton(self):
        breton = Breton('Magnus',58,1.70,50)
        assert 1800 == breton.live
        assert 300 == breton.attack


    def test_ogro(self):
        ogro = Ogro('david',200,2.30,50)

        assert ogro.attack == 500
        assert ogro.live == 5000


    def test_attack_1(self):
        ogro = Ogro('david', 200, 2.30, 50)
        imperial = Imperial('Manin', 78, 1.67, 52)

        assert 2500 == imperial.live

        imperial.is_attacked(ogro.attack)

        assert 2000 == imperial.live


if __name__ == "__main__":
    unittest.main()
