class Tilemap:
    def __init__(self, map_width: int, map_height: int):
        """
        Initializes a tilemap in the form of a 2 dimensional array. 

        Args:
            map_width (int): The width of the tilemap.
            map_height (int): The height of the tilemap.

        Returns:
            list: A 2D list representing the tilemap with the path.

        Raises:
            TypeError: If map_width or map_height are not integers.
            ValueError: If map_width or map_height are not greater than 0.
        """
        # Check if map_width and map_height are integers
        if not isinstance(map_width, int) or not isinstance(map_height, int):
            raise TypeError("map_width and map_height must be integers")
        # Check if map_width and map_height are greater than 0
        if map_width <= 0 or map_height <= 0:
            raise ValueError("map_width and map_height must be greater than 0")
        
        # Set map_width and map_height attributes for later use
        self.map_width = map_width
        self.map_height = map_height

        # Initialize the tilemap with 'X'
        self.tilemap = [['X' for _ in range(map_width)] for _ in range(map_height)]


    def path_tilemap(self, start_point: int, end_point: int):
        """
        Generate a path from a start point to an end point using only up/down/left/right movements.

        Args:
            start_point (int): The column index of the start point in the first row.
            end_point (int): The column index of the end point in the last row.

        Raises:
            TypeError: start_point or end_point are not integers.
            ValueError: If start_point or end_point are out of bounds.
        """
        # Check if start_point and end_point are integers
        if not isinstance(start_point, int) or not isinstance(end_point, int):
            raise TypeError("start_point and end_point must be integers")
        # Check if start_point and end_point are within bounds
        if start_point < 0 or start_point >= self.map_width or end_point < 0 or end_point >= self.map_width:
            raise ValueError("start_point and end_point must be within the bounds of the tilemap")

        # Iterate through tilemap's rows, converting all start_point indexes to 'P' creating a vertical line from first to last row
        for row in self.tilemap:
            row[start_point] = 'P'

        # No horizontal movement needed if start and end columns are the same
        if start_point == end_point:
            return

        # If start_point is smaller than end_point, convert all 'X's from end of vertical line to end_point into 'P's in final row 
        if start_point < end_point:
            for tile in range(start_point + 1, end_point + 1):
                self.tilemap[-1][tile] = 'P'

        # If start_point is larger than end_point, convert all 'X's from beginning of vertical line to end_point into 'P's in final row
        else:
            for tile in range(start_point - 1, end_point - 1, -1):
                self.tilemap[-1][tile] = 'P'


    def __str__(self):
        max_length = max(len(str(tile)) for row in self.tilemap for tile in row)
        return '\n'.join(' '.join(f'{tile:>{max_length}}' for tile in row) for row in self.tilemap)
    
map = Tilemap(5, 3)
map.path_tilemap(1, 2)
print(map)
# map.print_tilemap()

# print("- - - - - - - - - - - - - - - ")

# map = Tilemap(20, 20)
# map.path_tilemap(0, 19)
# map.print_tilemap()

# print("- - - - - - - - - - - - - - - ")

# map = Tilemap(7, 12)
# map.path_tilemap(6, 6)
# map.print_tilemap()




