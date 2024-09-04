class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction = 0  
        obstacle_set = set(map(tuple, obstacles))
        max_distance_sq = 0
        for command in commands:
            if command == -2: 
                direction = (direction - 1) % 4
            elif command == -1:  
                direction = (direction + 1) % 4
            else:  
                for _ in range(command):
                    next_x = x + directions[direction][0]
                    next_y = y + directions[direction][1]
                    
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y  
                        max_distance_sq = max(max_distance_sq, x**2 + y**2)
        
        return max_distance_sq