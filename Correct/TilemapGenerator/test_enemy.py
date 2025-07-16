import pytest
import sys
import random
from unittest.mock import patch
import os

# Add the parent directory to sys.path
sys.path.insert(0, '/tmp/inputs/TilemapGenerator')

# Import the Enemy class
from Enemy import Enemy

class TestEnemy:
    """
    Test suite for the Enemy class
    """
    
    # Test cases for the __init__ method
    
    def test_init_with_no_args(self):
        """Test creating an enemy with no arguments"""
        # Mock the random.choice to return a specific enemy type
        with patch('random.choice', return_value="bat"):
            # Mock random.randint to return a specific level
            with patch('random.randint', return_value=10):
                enemy = Enemy()
                assert enemy.type == "bat"
                assert enemy.level == 10
                assert enemy.row is None
                assert enemy.col is None
    
    def test_init_with_type_only(self):
        """Test creating an enemy with only type specified"""
        # Mock random.randint to return a specific level
        with patch('random.randint', return_value=65):
            enemy = Enemy(type="vampire")
            assert enemy.type == "vampire"
            assert enemy.level == 65
            assert enemy.row is None
            assert enemy.col is None
    
    def test_init_with_levels_only(self):
        """Test creating an enemy with only min and max levels specified"""
        # Mock random.choice to return a specific enemy type
        with patch('random.choice', return_value="minion"):
            # Mock random.randint to return a specific level
            with patch('random.randint', return_value=15):
                enemy = Enemy(min_level=10, max_level=20)
                assert enemy.type == "minion"
                assert enemy.level == 15
                assert enemy.row is None
                assert enemy.col is None
    
    def test_init_with_all_args(self):
        """Test creating an enemy with type, min_level, and max_level specified"""
        # Mock random.randint to return a specific level
        with patch('random.randint', return_value=25):
            enemy = Enemy(type="werewolf", min_level=20, max_level=30)
            assert enemy.type == "werewolf"
            assert enemy.level == 25
            assert enemy.row is None
            assert enemy.col is None
    
    # Error case tests
    
    def test_init_with_invalid_type(self):
        """Test creating an enemy with an invalid type"""
        with pytest.raises(ValueError) as excinfo:
            Enemy(type="invalid_type")
        assert "Invalid enemy type." in str(excinfo.value)
    
    def test_init_with_only_min_level(self):
        """Test creating an enemy with only min_level specified"""
        with pytest.raises(ValueError) as excinfo:
            Enemy(min_level=10)
        assert "Both min_level and max_level must be provided together." in str(excinfo.value)
    
    def test_init_with_only_max_level(self):
        """Test creating an enemy with only max_level specified"""
        with pytest.raises(ValueError) as excinfo:
            Enemy(max_level=20)
        assert "Both min_level and max_level must be provided together." in str(excinfo.value)
    
    def test_init_with_min_greater_than_max(self):
        """Test creating an enemy with min_level > max_level"""
        with pytest.raises(ValueError) as excinfo:
            Enemy(min_level=30, max_level=20)
        assert "min_level argument must be smaller than or equal to max_level argument." in str(excinfo.value)
    
    def test_init_with_no_valid_enemy_types(self):
        """Test creating an enemy with level range where no enemy types exist"""
        with pytest.raises(ValueError) as excinfo:
            Enemy(min_level=200, max_level=300)
        assert "No enemy type found within the given level range." in str(excinfo.value)
    
    # Test cases for level range calculation
    
    def test_level_within_bounds(self):
        """Test that the level is always within the specified bounds"""
        for _ in range(100):  # Run multiple times to catch potential random issues
            enemy = Enemy(type="sorcerer", min_level=70, max_level=80)
            assert 70 <= enemy.level <= 80
    
    def test_level_adjustment_based_on_type(self):
        """Test level adjustment based on type's default range"""
        # "bat" has default range (0, 15)
        enemy = Enemy(type="bat", min_level=10, max_level=50)
        assert enemy.level >= 10
        assert enemy.level <= 15  # Should be capped by the default max
    
    # Test cases for enemy_loc method
    
    def test_enemy_loc(self):
        """Test setting the enemy location"""
        enemy = Enemy(type="bat")
        enemy.enemy_loc(5, 10)
        assert enemy.row == 5
        assert enemy.col == 10
    
    def test_enemy_loc_update(self):
        """Test updating the enemy location"""
        enemy = Enemy(type="bat")
        enemy.enemy_loc(5, 10)
        # Update the location
        enemy.enemy_loc(8, 15)
        assert enemy.row == 8
        assert enemy.col == 15


if __name__ == "__main__":
    pytest.main(['-v', 'test_enemy.py'])
