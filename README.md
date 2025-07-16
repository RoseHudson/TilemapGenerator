# Tilemap Module
## Overview

The Tilemap module is designed to create a tilemap for a videogame. The tilemap is represented by a 2D array and includes a path from a designated start point to a designated endpoint. Enemies are placed on the path, which the player must fight to traverse the tilemap.

## Classes

### Enemy

The `Enemy` class represents an enemy in the game. It has the following attributes:

* `type`: The type of enemy (one of the 9 predefined types)
* `level`: The level of the enemy
* `row`: The row index of the enemy's location on the tilemap
* `col`: The column index of the enemy's location on the tilemap

The `Enemy` class has the following methods:

* `__init__(type: str = None, min_level: int = None, max_level: int = None)`: Initializes an `Enemy` instance with a random type and level.
* `enemy_loc(row: int, col: int)`: Sets the location of the enemy on the tilemap.

### Tilemap

The `Tilemap` class represents the tilemap. It has the following attributes:

* `map_width`: The width of the tilemap
* `map_height`: The height of the tilemap
* `tilemap`: A 2D list representing the tilemap

The `Tilemap` class has the following methods:

* `__init__(map_width: int, map_height: int)`: Initializes a tilemap with the specified width and height.
* `path_tilemap(start_point: int, end_point: int)`: Generates a path from the start point to the end point on the tilemap.
* `__str__()`: Returns a string representation of the tilemap.

## Usage

To use the Tilemap module, create an instance of the `Tilemap` class and specify the width and height of the tilemap. Then, use the `path_tilemap` method to generate a path from a start point to an end point.

```python
tilemap = Tilemap(10, 10)
tilemap.path_tilemap(0, 9)
print(tilemap)
```

To create an enemy, instantiate the `Enemy` class and specify the type and level range. Then, use the `enemy_loc` method to set the enemy's location on the tilemap.

```python
enemy = Enemy()
enemy.enemy_loc(5, 5)
```

## Example Use Case

```python
# Create a tilemap with a width and height of 10
tilemap = Tilemap(10, 10)

# Generate a path from the start point (0) to the end point (9)
tilemap.path_tilemap(0, 9)

# Print the tilemap
print(tilemap)

# Create an enemy with a random type and level
enemy = Enemy()

# Set the enemy's location on the tilemap
enemy.enemy_loc(5, 5)

# Print the enemy's details
print(f"Enemy type: {enemy.type}, level: {enemy.level}, location: ({enemy.row}, {enemy.col})")
```

## Installation

To install the Tilemap module, simply copy the module into your project directory.

## Requirements

* Python 3.x

## Notes

* The `Enemy` class uses a predefined list of enemy types and their corresponding level ranges.
* The `Tilemap` class uses a 2D list to represent the tilemap, where 'X' represents an empty tile and 'P' represents a tile on the path.
* The `path_tilemap` method generates a path from the start point to the end point using only up/down/left/right movements.