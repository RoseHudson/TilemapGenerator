import random

enemy_list = [
    {'type': 'sorcerer', 'level': 18},
    {'type': 'minion', 'level': 20},
    {'type': 'sorcerer', 'level': 74},
    {'type': 'werewolf', 'level': 47}
]

given_map = [
    ['X', 'X', 'P', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'P', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'P', 'P', 'P', 'P', 'P', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'P', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'P', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'P', 'X', 'X'],
    ['X', 'P', 'P', 'P', 'P', 'P', 'P', 'X', 'X'],
    ['X', 'P', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'P', 'P', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'P', 'X', 'X', 'X', 'X', 'X', 'X']
]

def find_nth_p(grid, n):
    ##UNUSED
    # arr = 0
    # ind = 0
    # p_count = 0
    # prev = None
    # while arr < len(grid):
    #     while ind < len(grid[arr]):
    #         if grid[arr][ind] == 'P':
    #             p_count += 1
    #             prev = [arr, ind]
    #             if p_count == n:
    #                 return [arr, ind]
    #         ind += 1
    #     # if new 
    #     arr += 1
    #     ind = 0


    prev = None
    all_indices = []
    # find P in first row
    for i in range(len(grid[0])):
        if grid[0][i] == 'P':
            # assign it to the variable prev
            prev = [0, i]
            # add its index to the list
            all_indices.append(prev)
            break
    print(all_indices)
    ## MY IMPLEMENTATION
    # path_continues = True
    # while path_continues:   
    #     # check grid[prev[0] + 1][prev[1]] if prev[0] + 1 viable
    #     if prev[0] + 1 < len(grid) and [prev[0] + 1, prev[1]] not in all_indices:
    #         if grid[prev[0] + 1][prev[1]] == 'P':
    #             # if it's a P, assign it to the variable prev
    #             prev = [prev[0] + 1, prev[1]]
    #             # add its index to the list 
    #             all_indices.append(prev)
    #             print(all_indices)

    #     # check grid[prev[0] - 1][prev[1]] if prev[0] - 1 viable
    #     elif prev[0] >= 1 and [prev[0] - 1, prev[1]] not in all_indices:
    #         print('hello1')
    #         if grid[prev[0] - 1][prev[1]] == 'P':
    #             # if it's a P assign it to the variable prev
    #             prev = [prev[0] - 1, prev[1]]
    #             # add its index to the list
    #             all_indices.append(prev)
    #             print(all_indices)

    #     # check grid[prev[0]][prev[1] + 1] if prev[1] + 1 viable
    #     elif prev[1] + 1 < len(grid[0]) and [prev[0], prev[1] + 1] not in all_indices:
    #         print('hello2')
    #         if grid[prev[0]][prev[1] + 1] == 'P':
    #             # if it's a P assign it to the variable prev
    #             prev = [prev[0], prev[1] + 1]
    #             # add its index to the list
    #             all_indices.append(prev)
    #             print(all_indices)

    #     # check grid[prev[0]][prev[1] - 1] if prev[1] - 1 viable
    #     elif prev[1] >= 1 and [prev[0], prev[1] - 1] not in all_indices:
    #         print('hello3')
    #         if grid[prev[0]][prev[1] - 1] == 'P':
    #             # if it's a P assign it to the variable prev
    #             prev = [prev[0], prev[1] - 1]
    #             # add its index to the list
    #             all_indices.append(prev)
    #             print(all_indices)

    #     #else, return None
    #     else:
    #         path_continues = False
        
    # print(all_indices)
    ## AI IMPLEMENTATION
    path_continues = True
    while path_continues:
        path_continues = False
        # Define the possible directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Check all adjacent cells
        for direction in directions:
            new_row, new_col = prev[0] + direction[0], prev[1] + direction[1]
            if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and [new_row, new_col] not in all_indices:
                if grid[new_row][new_col] == 'P':
                    # Update prev and all_indices
                    prev = [new_row, new_col]
                    all_indices.append(prev)
                    print(all_indices)
                    path_continues = True
                    break


### enemy function perfectly suited to just run prev enemy func if anything missing. 
### should I just add the index of the monster to the monster's dict? not edit map?
def add_enemies(enemies_list, tilemap):
    ## handle if level is missing
    # Sort the list in ascending order by 'level'
    sorted_list = sorted(enemies_list, key=lambda x: x['level'])
    # Assign numbers to the enemies
    organized_list = {}
    count = 1
    for enemy in sorted_list:
        organized_list[count] = enemy
        count += 1


    # Count the number of characters in designated path
    path_len = sum(row.count('P') for row in tilemap)

    
    space_per_enemy = path_len // len(sorted_list)
    # print(space_per_enemy)
    last_enemy = 0
    enemy_count = 1
    for enemy in sorted_list:
        # Randomly choose the position of the enemy 
        tile = random.randint(last_enemy + 1, (enemy_count) * space_per_enemy)
        # Figure out the index of the chosen tile in the map
        print(tile)
        # print(path_len)
        pos = find_nth_p(tilemap, tile)
        print(pos)
        # Add the enemy to the map
        tilemap[pos[0]][pos[1]] = "E"
        last_enemy = tile
        enemy_count += 1


    return tilemap

for line in add_enemies(enemy_list, given_map):
    print(line)
