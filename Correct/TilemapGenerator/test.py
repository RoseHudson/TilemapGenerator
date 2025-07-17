import unittest
# from skel_code import create_enemy
# from create_enemy import create_enemy
# from response import create_enemy
# from response2 import create_enemy
from Enemy import Enemy
  
class TestCreateEnemy(unittest.TestCase):

    enemies_dict = {
        "bat" : [0, 15], 
        "minion" : [5, 25],
        "bat swarm" : [20, 40],
        "sorcerer's apprentice" : [30, 45],
        "lesser vampire" : [30, 50],
        "werewolf" : [30, 60],
        "vampire" : [50, 70],
        "sorcerer" : [60, 85],
        "master sorcerer": [80, 100]
    }

    # Helper assertion
    def assertInRange(self, level, min, max):
        self.assertGreaterEqual(level, min)
        self.assertLessEqual(level, max)

    # Category 1 - No args provided
    def test_1_1_dict_structure(self):
        enemy = Enemy()
        self.assertTrue(hasattr(enemy, 'type'))
        self.assertTrue(hasattr(enemy, 'level'))
        self.assertTrue(hasattr(enemy, 'row'))
        self.assertTrue(hasattr(enemy, 'col'))

    def test_1_2_valid_type(self):
        enemy = Enemy()
        self.assertIn(enemy.type, self.enemies_dict.keys())

    def test_1_3_level_in_default_range(self):
        enemy = Enemy()
        self.assertInRange(enemy.level, 
                           self.enemies_dict[enemy.type][0], 
                           self.enemies_dict[enemy.type][1])

    def test_1_4_enemy_randomness(self):
        counts = {enemy: 0 for enemy in self.enemies_dict}
        for _ in range(1000):
            result = Enemy()
            counts[result.type] += 1
        active_types = [enemy for enemy, count in counts.items() if count > 0]
        self.assertGreaterEqual(len(active_types), 7)

    def test_1_5_level_randomness(self):
        for enemy, (min_lvl, max_lvl) in self.enemies_dict.items():
            levels_seen = set()
            for _ in range(200):
                result = Enemy(type=enemy)
                levels_seen.add(result.level)
                if len(levels_seen) > 1:
                    break
            self.assertGreater(len(levels_seen), 1)

    # Category 2 - only type provided
    def test_2_1_correct_type_returned(self):
       enemy = Enemy('sorcerer')
       self.assertIs('sorcerer', enemy.type)

    def test_2_2_all_levels_correct(self):
        enemy = Enemy('sorcerer')
        self.assertInRange(enemy.level, self.enemies_dict['sorcerer'][0], self.enemies_dict['sorcerer'][1])

    # Category 3 - all args provided
    def test_3_1_override_levels(self):
        enemy = Enemy('bat', 50, 60)
        self.assertInRange(enemy.level, 50, 60)

    def test_3_2_min_equals_max(self):
        enemy = Enemy('bat', 50, 50)
        self.assertEqual(enemy.level, 50)

    # Category 4 - only min and max provided
    def test_4_1_valid_selection(self):
        enemy = Enemy(None, 20, 30)
        self.assertIn(enemy.type, ["minion", "bat swarm", "sorcerer's apprentice", "lesser vampire", "werewolf"])

    def test_4_2_level_from_intersection(self):
        enemy = Enemy(None, 20, 22)
        self.assertInRange(enemy.level, 20, 22)

    def test_4_3_narrow_overlap(self):
        enemy = Enemy(None, 75, 82)
        if enemy.type == "sorcerer":
            self.assertInRange(enemy.level, 75, 82)
        else:
            self.assertInRange(enemy.level, 80, 82)

    def test_4_4_single_point_overlap(self):
        enemy = Enemy(None, 40, 40)
        self.assertIn(enemy.type, ["bat swarm", "sorcerer's apprentice", "lesser vampire", "werewolf"])
        self.assertEqual(enemy.level, 40)

    # Category 5 - errors and invalid inputs
    def test_5_1_min_level_only(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(None, 3, None)

    def test_5_2_max_level_only(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(None, None, 100)
    
    def test_5_3_type_and_only_one_bound(self):
        with self.assertRaises(ValueError):
            enemy = Enemy("vampire", None, 100)

    def test_5_4_invalid_type(self):
        with self.assertRaises(ValueError):
            enemy = Enemy("dragon")

    def test_5_5_min_greater_than_max(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(None, 50, 20)

    def test_5_6_min_too_small(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(None, -5, 20)

    def test_5_7_max_too_large(self):
        with self.assertRaises(ValueError):
            enemy = Enemy(None, 0, 150)

    def test_5_8_case_sensitivity_in_type(self):
        with self.assertRaises(ValueError):
            enemy = Enemy("Vampire")


if __name__ == '__main__':
    unittest.main()
