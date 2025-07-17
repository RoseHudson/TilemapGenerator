import unittest
import random
from unittest.mock import patch, MagicMock
import sys
import os

# Add the source directory to the path to import the Enemy class
sys.path.append('/tmp/inputs/TilemapGenerator')
from Enemy import Enemy


class TestEnemy(unittest.TestCase):
    """Comprehensive unit tests for the Enemy class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.enemy_types = {
            "bat": (0, 15),
            "minion": (5, 25),
            "bat swarm": (20, 40),
            "sorcerer's apprentice": (30, 45),
            "lesser vampire": (30, 50),
            "werewolf": (30, 60),
            "vampire": (50, 70),
            "sorcerer": (60, 85),
            "master sorcerer": (80, 100)
        }

    def test_init_no_arguments(self):
        """Test Enemy initialization with no arguments."""
        with patch('random.choice') as mock_choice, \
             patch('random.randint') as mock_randint:
            
            # Mock random.choice to return a specific enemy type
            mock_choice.return_value = "bat"
            mock_randint.return_value = 10
            
            enemy = Enemy()
            
            # Verify that a random enemy type was chosen
            mock_choice.assert_called_once()
            # Enemy type should be set
            self.assertEqual(enemy.type, "bat")
            # Level should be set
            self.assertEqual(enemy.level, 10)
            # Location should be None initially
            self.assertIsNone(enemy.row)
            self.assertIsNone(enemy.col)

    def test_init_with_valid_type_only(self):
        """Test Enemy initialization with only a valid type."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 12
            
            enemy = Enemy(type="bat")
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 12)
            # Should use the default range for bat (0, 15)
            mock_randint.assert_called_once_with(0, 15)

    def test_init_with_type_and_level_range(self):
        """Test Enemy initialization with type and level range."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 8
            
            enemy = Enemy(type="bat", min_level=5, max_level=10)
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 8)
            # Should use the provided range
            mock_randint.assert_called_once_with(5, 10)

    def test_init_with_level_range_only(self):
        """Test Enemy initialization with only level range."""
        with patch('random.choice') as mock_choice, \
             patch('random.randint') as mock_randint:
            
            # Mock to return a type that fits in the range
            mock_choice.return_value = "minion"
            mock_randint.return_value = 15
            
            enemy = Enemy(min_level=10, max_level=20)
            
            # Should choose from types that overlap with the level range
            mock_choice.assert_called_once()
            self.assertEqual(enemy.type, "minion")
            self.assertEqual(enemy.level, 15)

    def test_init_invalid_type(self):
        """Test Enemy initialization with invalid type."""
        with self.assertRaises(ValueError) as context:
            Enemy(type="invalid_type")
        
        self.assertEqual(str(context.exception), "Invalid enemy type.")

    def test_init_only_min_level_provided(self):
        """Test that providing only min_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=10)
        
        self.assertEqual(str(context.exception), "Both min_level and max_level must be provided together.")

    def test_init_only_max_level_provided(self):
        """Test that providing only max_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(max_level=20)
        
        self.assertEqual(str(context.exception), "Both min_level and max_level must be provided together.")

    def test_init_min_level_greater_than_max_level(self):
        """Test that min_level > max_level raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=30, max_level=20)
        
        self.assertEqual(str(context.exception), "min_level argument must be smaller than or equal to max_level argument.")

    def test_init_min_level_below_zero(self):
        """Test that min_level < 0 raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=-5, max_level=10)
        
        self.assertEqual(str(context.exception), "Levels can only be between 0 and 100.")

    def test_init_max_level_above_100(self): 
        """Test that max_level > 100 raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(min_level=50, max_level=150)
        
        self.assertEqual(str(context.exception), "Levels can only be between 0 and 100.")

    def test_init_boundary_level_values(self):
        """Test Enemy initialization with boundary level values."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 0
            
            # Test with min_level = 0, max_level = 100
            enemy = Enemy(min_level=0, max_level=100)
            
            self.assertIsNotNone(enemy.type)
            self.assertEqual(enemy.level, 0)

    def test_init_equal_min_max_levels(self):
        """Test Enemy initialization with equal min and max levels."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            enemy = Enemy(type="bat", min_level=10, max_level=10)
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 10)
            mock_randint.assert_called_once_with(10, 10)

    def test_init_type_with_narrow_level_range(self):
        """Test Enemy initialization with a type and narrow level range."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 25
            
            enemy = Enemy(type="minion", min_level=20, max_level=30)
            
            self.assertEqual(enemy.type, "minion")
            self.assertEqual(enemy.level, 25)
            mock_randint.assert_called_once_with(20, 30)

    def test_init_type_with_wider_level_range(self):
        """Test Enemy initialization with a type and wider level range."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            # For "bat" (0, 15), providing range (0, 100) 
            # When type is provided with level range, it uses the provided range directly
            enemy = Enemy(type="bat", min_level=0, max_level=100)
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 10)
            # The code uses the provided range directly when type is specified
            mock_randint.assert_called_once_with(0, 100)

    def test_init_all_enemy_types_valid(self): 
        """Test that all predefined enemy types work correctly."""
        for enemy_type, (min_lvl, max_lvl) in self.enemy_types.items():
            with patch('random.randint') as mock_randint:
                mock_randint.return_value = min_lvl
                
                enemy = Enemy(type=enemy_type)
                
                self.assertEqual(enemy.type, enemy_type)
                self.assertEqual(enemy.level, min_lvl)
                mock_randint.assert_called_once_with(min_lvl, max_lvl)

    def test_enemy_loc_method(self): 
        """Test the enemy_loc method."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            enemy = Enemy(type="bat")
            
            # Initially, location should be None
            self.assertIsNone(enemy.row)
            self.assertIsNone(enemy.col)
            
            # Set location using enemy_loc method
            enemy.enemy_loc(5, 7)
            
            # Verify location is set correctly
            self.assertEqual(enemy.row, 5)
            self.assertEqual(enemy.col, 7)

    def test_enemy_loc_with_various_coordinates(self):
        """Test enemy_loc method with various coordinate values."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            enemy = Enemy(type="bat")
            
            # Test with zero coordinates
            enemy.enemy_loc(0, 0)
            self.assertEqual(enemy.row, 0)
            self.assertEqual(enemy.col, 0)
            
            # Test with negative coordinates
            enemy.enemy_loc(-1, -2)
            self.assertEqual(enemy.row, -1)
            self.assertEqual(enemy.col, -2)
            
            # Test with large coordinates
            enemy.enemy_loc(999, 1000)
            self.assertEqual(enemy.row, 999)
            self.assertEqual(enemy.col, 1000)

    def test_enemy_loc_overwrite_location(self):
        """Test that enemy_loc overwrites previous location."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            enemy = Enemy(type="bat")
            
            # Set initial location
            enemy.enemy_loc(1, 2)
            self.assertEqual(enemy.row, 1)
            self.assertEqual(enemy.col, 2)
            
            # Overwrite location
            enemy.enemy_loc(3, 4)
            self.assertEqual(enemy.row, 3)
            self.assertEqual(enemy.col, 4)

    def test_multiple_enemy_instances(self):
        """Test creating multiple Enemy instances."""
        with patch('random.choice') as mock_choice, \
             patch('random.randint') as mock_randint:
            
            # Create first enemy
            mock_choice.return_value = "bat"
            mock_randint.return_value = 5
            enemy1 = Enemy()
            
            # Create second enemy
            mock_choice.return_value = "vampire"
            mock_randint.return_value = 60
            enemy2 = Enemy()
            
            # Verify they are independent
            self.assertEqual(enemy1.type, "bat")
            self.assertEqual(enemy1.level, 5)
            self.assertEqual(enemy2.type, "vampire")
            self.assertEqual(enemy2.level, 60)
            
            # Set different locations
            enemy1.enemy_loc(1, 1)
            enemy2.enemy_loc(2, 2)
            
            self.assertEqual(enemy1.row, 1)
            self.assertEqual(enemy1.col, 1)
            self.assertEqual(enemy2.row, 2)
            self.assertEqual(enemy2.col, 2)

    def test_init_with_type_case_sensitivity(self):
        """Test that enemy type is case-sensitive."""
        with self.assertRaises(ValueError) as context:
            Enemy(type="BAT")
        
        self.assertEqual(str(context.exception), "Invalid enemy type.")
        
        with self.assertRaises(ValueError) as context:
            Enemy(type="Bat")
        
        self.assertEqual(str(context.exception), "Invalid enemy type.")

    def test_init_with_empty_string_type(self):
        """Test that empty string type raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(type="")
        
        self.assertEqual(str(context.exception), "Invalid enemy type.")

    def test_init_with_whitespace_type(self):
        """Test that whitespace type raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Enemy(type="   ")
        
        self.assertEqual(str(context.exception), "Invalid enemy type.")

    def test_level_range_intersection_edge_cases(self):
        """Test level range intersection edge cases."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 30
            
            # Test exact boundary match
            enemy = Enemy(type="sorcerer's apprentice", min_level=30, max_level=45)
            self.assertEqual(enemy.type, "sorcerer's apprentice")
            self.assertEqual(enemy.level, 30)
            mock_randint.assert_called_once_with(30, 45)

    def test_attributes_exist(self):
        """Test that all expected attributes exist after initialization."""
        enemy = Enemy(type="bat")
            
        # Check that all attributes exist
        self.assertTrue(hasattr(enemy, 'type'))
        self.assertTrue(hasattr(enemy, 'level'))
        self.assertTrue(hasattr(enemy, 'row'))
        self.assertTrue(hasattr(enemy, 'col'))

    def test_randomization_behavior(self):
        """Test that randomization works as expected without mocking."""
        # Test that creating multiple enemies without parameters gives different results
        enemies = [Enemy() for _ in range(10)]
        
        # Check that all enemies have valid types
        for enemy in enemies:
            self.assertIn(enemy.type, self.enemy_types.keys())
            
        # Check that levels are within valid ranges for their types
        for enemy in enemies:
            min_level, max_level = self.enemy_types[enemy.type]
            self.assertGreaterEqual(enemy.level, min_level)
            self.assertLessEqual(enemy.level, max_level)
            
        # Check that levels are within valid ranges for their types
        for enemy in enemies:
            min_level, max_level = self.enemy_types[enemy.type]
            self.assertGreaterEqual(enemy.level, min_level)
            self.assertLessEqual(enemy.level, max_level)

    def test_init_with_float_levels(self):
        """Test that float levels are handled correctly."""
        # The randint function expects integers, so this should work
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 10
            
            # Test with float values that can be converted to int
            enemy = Enemy(type="bat", min_level=5.0, max_level=15.0)
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 10)
            # randint should be called with the float values as-is
            mock_randint.assert_called_once_with(5.0, 15.0)

    def test_init_with_none_values(self):
        """Test behavior with explicit None values."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 8
            
            # Test with explicit None values
            enemy = Enemy(type="bat", min_level=None, max_level=None)
            
            self.assertEqual(enemy.type, "bat")
            self.assertEqual(enemy.level, 8)
            # Should use default range for bat
            mock_randint.assert_called_once_with(0, 15)

    def test_init_with_boundary_enemy_types(self):
        """Test initialization with enemy types at the boundaries of ranges."""
        # Test with enemies that have ranges touching boundaries
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 0
            
            # Test lowest level enemy
            enemy = Enemy(type="bat")
            self.assertEqual(enemy.level, 0)
            mock_randint.assert_called_once_with(0, 15)
            
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 100
            
            # Test highest level enemy
            enemy = Enemy(type="master sorcerer")
            self.assertEqual(enemy.level, 100)
            mock_randint.assert_called_once_with(80, 100)

    def test_init_overlapping_ranges(self):
        """Test initialization with overlapping enemy type ranges."""
        enemy = Enemy(None, 20, 30)
        self.assertIn(enemy.type, ["minion", "bat swarm", "sorcerer's apprentice", "lesser vampire", "werewolf"])

    def test_enemy_type_randomization(self):
        """Test that all different enemy types can be generated."""
        counts = {enemy: 0 for enemy in self.enemy_types}
        for _ in range(1000):
            result = Enemy()
            counts[result.type] += 1
        active_types = [enemy for enemy, count in counts.items() if count > 0]
        self.assertGreaterEqual(len(active_types), 7)

    def test_enemy_level_randomization(self):
        """Test that various enemy levels can be generated."""
        for enemy, (min_lvl, max_lvl) in self.enemy_types.items():
            levels_seen = set()
            for _ in range(200):
                result = Enemy(type=enemy)
                levels_seen.add(result.level)
                if len(levels_seen) > 1:
                    break
            self.assertGreater(len(levels_seen), 1)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)