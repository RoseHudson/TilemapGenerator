import random

class Enemy:
    def __init__(self, type: str = None, min_level: int = None, max_level: int = None):
        """
        Initializes an Enemy instance with a random type and level.

        Args:
            type (str, optional): The type of enemy. Defaults to None.
            min_level (int, optional): The minimum level of the enemy. Defaults to None.
            max_level (int, optional): The maximum level of the enemy. Defaults to None.

        Returns:
            dict: A dictionary containing the type and level of the enemy.

        Raises:
            ValueError: If only one of min_level or max_level is provided, min_level is greater 
            than max_level, min_level or max_level are not between 1 and 100, if there are no
            enemy types within the provided min_level and max_level, or if type is not one of
            the valid options or None. 
        """

        # Define the enemy types and their default level ranges
        enemy_types = {
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

        # Check if only one of min_level or max_level is provided
        if (min_level is not None and max_level is None) or (min_level is None and max_level is not None):
            raise ValueError("Both min_level and max_level must be provided together.")
        
        # Ensure min_level is not greater than max_level
        if (min_level is not None and max_level is not None) and (min_level > max_level):
            raise ValueError("min_level argument must be smaller than or equal to max_level argument.")
        
        # Ensure min_level and max_level are in range
        if min_level < 0 or max_level > 100:
            raise ValueError("Levels can only be between 0 and 100.")

        if type is None:
            # Behavior if no arguments are given
            if min_level is None and max_level is None:
                # Randomly choose an enemy type and set min_level and max_level to that type's default range
                self.type = random.choice(list(enemy_types.keys()))
                min_level, max_level = enemy_types[self.type]
            # Behavior if only min_level and max_level are provided
            else:
                # Filter enemy types based on the provided level range
                possible_types = [enemy_type for enemy_type, (default_min, default_max) in enemy_types.items() 
                                if max(min_level, default_min) <= min(max_level, default_max)]
                # Check if there are any enemies that fit into the provided level range
                if not possible_types:
                    raise ValueError("No enemy type found within the given level range.")
                # Randomly choose an enemy within the provided level range
                self.type = random.choice(possible_types)
                # Set min_level and max_level to be within both the provided level range and that type's default range
                default_min, default_max = enemy_types[self.type]
                min_level = max(min_level, default_min)
                max_level = min(max_level, default_max)
        else:
            # Check if the provided type is valid
            if type not in enemy_types:
                raise ValueError("Invalid enemy type.")
            
            # Behavior if the type is provided but min_level and max_level are not
            self.type = type
            if min_level is None and max_level is None:
                min_level, max_level = enemy_types[self.type]

        # Generate a random level within the determined range
        self.level = random.randint(min_level, max_level)

        # Add additional attributes for later use
        self.row = None
        self.col = None

    def enemy_loc(self, row: int, col: int):
        """
        Sets the location of the enemy on a tilemap.

        Args:
            row (int): The row of the enemy's location.
            col (int): The column of the enemy's location.
        """
        self.row = row
        self.col = col


