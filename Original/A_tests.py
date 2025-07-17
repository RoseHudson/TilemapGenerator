import unittest
from unittest.mock import patch
import sys
import os

# Add the TilemapGenerator directory to the path
sys.path.append('/tmp/inputs/TilemapGenerator')
from Enemy import Enemy

class TestEnemy(unittest.TestCase):
    
    def test_init_no_arguments(self):
        """Test initialization with no arguments."""
        with patch('random.choice', return_value='bat'), \
             patch('random.randint', return_value=10):
            
            enemy = Enemy()
            self.assertEqual(enemy.type, 'bat')
            self.assertEqual(enemy.level, 10)
            self.assertIsNone(enemy.row)
            self.assertIsNone(enemy.col)
    
    def test_init_with_type_only(self):
        """Test initialization with only type argument."""
        with patch('random.randint', return_value=40):
            enemy = Enemy(type='werewolf')
            self.assertEqual(enemy.type, 'werewolf')
            self.assertEqual(enemy.level, 40)
    
    def test_init_with_level_range_only(self):
        """Test initialization with only min_level and max_level arguments."""
        with patch('random.choice', return_value='vampire'), \
             patch('random.randint', return_value=60):
            
            enemy = Enemy(min_level=50, max_level=70)
            self.assertEqual(enemy.type, 'vampire')
            self.assertEqual(enemy.level, 60)
    
    def test_init_with_all_arguments(self): #4
        """Test initialization with all arguments (type, min_level, max_level)."""
        with patch('random.randint', return_value=85):
            enemy = Enemy(type='sorcerer', min_level=80, max_level=85)
            self.assertEqual(enemy.type, 'sorcerer')
            self.assertEqual(enemy.level, 85)
    
    def test_invalid_type(self):
        """Test that initializing with an invalid type raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(type='invalid_enemy')
        self.assertEqual(str(context.exception), "Invalid enemy type.")
    
    def test_min_level_only(self): #6
        """Test that providing only min_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=20)
        self.assertEqual(str(context.exception), "Both min_level and max_level must be provided together.")
    
    def test_max_level_only(self):
        """Test that providing only max_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(max_level=50)
        self.assertEqual(str(context.exception), "Both min_level and max_level must be provided together.")
    
    def test_min_level_greater_than_max_level(self): #8
        """Test that min_level > max_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=70, max_level=50)
        self.assertEqual(str(context.exception), "min_level argument must be smaller than or equal to max_level argument.")
    
    def test_level_out_of_range(self):
        """Test that levels outside of [0, 100] raise ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=-10, max_level=50)
        self.assertEqual(str(context.exception), "Levels can only be between 0 and 100.")
        
        with self.assertRaises(ValueError) as context: 
            Enemy(min_level=50, max_level=110)
        self.assertEqual(str(context.exception), "Levels can only be between 0 and 100.")
    
    # def test_no_enemy_in_range(self): #10 
        # """Test that providing a level range with no matching enemies raises ValueError."""
        # # The valid ranges for enemies according to the class are:
        # # "bat": (0, 15), "minion": (5, 25), "bat swarm": (20, 40),
        # # "sorcerer's apprentice": (30, 45), "lesser vampire": (30, 50),
        # # "werewolf": (30, 60), "vampire": (50, 70), "sorcerer": (60, 85),
        # # "master sorcerer": (80, 100)
        
        # # So a range of [90, 95] should only match with "master sorcerer"
        # # Let's test a range that doesn't match any enemy
        # with self.assertRaises(ValueError) as context:
        #     # This range is above all enemies except master sorcerer,
        #     # but we'll mock random.choice to pretend no enemies were found
        #     with patch('random.choice', side_effect=IndexError('No enemies in range')):
        #         Enemy(min_level=95, max_level=100)
        # self.assertEqual(str(context.exception), "No enemy type found within the given level range.")
    
    def test_enemy_type_level_constraints(self): 
        """Test that enemy types respect their level constraints."""
        # Test that the enemy level respects both the provided range and the enemy's default range
        with patch('random.choice', return_value='bat'), \
             patch('random.randint', return_value=10):
            
            # Bat has range (0, 15), providing range (5, 20) should result in level range (5, 15)
            enemy = Enemy(min_level=5, max_level=20)
            self.assertEqual(enemy.type, 'bat')
            self.assertEqual(enemy.level, 10)
    
    def test_enemy_loc(self): #12
        """Test setting the enemy location."""
        enemy = Enemy(type='bat')
        enemy.enemy_loc(5, 10)
        self.assertEqual(enemy.row, 5)
        self.assertEqual(enemy.col, 10)
    
    def test_enemy_loc_update(self):
        """Test updating the enemy location."""
        enemy = Enemy(type='bat')
        enemy.enemy_loc(5, 10)
        self.assertEqual(enemy.row, 5)
        self.assertEqual(enemy.col, 10)
        
        # Update to new location
        enemy.enemy_loc(8, 15)
        self.assertEqual(enemy.row, 8)
        self.assertEqual(enemy.col, 15)

    def test_random_behavior_with_real_random(self): #14
        """Test the randomness aspect without mocking."""
        # Create multiple enemies with the same parameters and check if we get variation
        enemies = [Enemy(min_level=30, max_level=60) for _ in range(10)]
        
        # Check that we have at least 2 different types or levels (indicating randomness)
        types = set(enemy.type for enemy in enemies)
        levels = set(enemy.level for enemy in enemies)
        
        # This test could potentially fail due to true randomness, but it's very unlikely
        self.assertGreaterEqual(len(types) + len(levels), 2, 
                              "Expected some variation in randomly generated enemies")
    
    def test_deterministic_behavior_with_fixed_seed(self): 
        """Test that with a fixed random seed, we get deterministic results."""
        import random
        
        # Set a fixed seed
        random.seed(42)
        enemy1 = Enemy()
        
        # Reset to the same seed
        random.seed(42)
        enemy2 = Enemy()
        
        # The enemies should be identical
        self.assertEqual(enemy1.type, enemy2.type)
        self.assertEqual(enemy1.level, enemy2.level)

if __name__ == '__main__':
    unittest.main()