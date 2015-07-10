import unittest
from Hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):

        self.hero = Hero(10, 0)

    def test_hero_default(self):

        self.assertEqual(
            (self.hero.health,
             self.hero.magic,
             self.hero.x,
             self.hero.y), (10, 0, None, None))

    def test_setHealth(self):
        self.hero.setHealth(-1)
        self.assertEqual(self.hero.health, 0)
        self.hero.setHealth(5)
        self.assertEqual(self.hero.health, 5)


if __name__ == '__main__':
    unittest.main()
