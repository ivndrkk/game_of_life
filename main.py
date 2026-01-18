import random
import os
import time

# ANSI colors - subtle blue tones
RESET = "\033[0m"
AQUA_NEW = "\033[96m█\033[0m"      
BLUE_OLD = "\033[94m█\033[0m"       
DARK_BLUE_DIE = "\033[34m█\033[0m" 
DEAD_LONG = " "                    

# Core board functions
def dead_state(width, height):
    board_state = []
    for i in range(height):
        row = [0] * width
        board_state.append(row)
    return board_state

def random_state(width, height):
    board_state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            board_state[i][j] = random.randint(0, 1)
    return board_state

# Game logic - classic version (no walrus)
def next_board_state(current_state, revive_chance=0):
    next_state = dead_state(len(current_state[0]), len(current_state))
    height = len(current_state)
    width = len(current_state[0])
    
    for row in range(height):
        for col in range(width):
            # count live neighbors
            live_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    r, c = row + i, col + j
                    if 0 <= r < height and 0 <= c < width:
                        live_neighbors += current_state[r][c]
            
            curr = current_state[row][col]
            if curr == 1:
                next_state[row][col] = 1 if 2 <= live_neighbors <= 3 else 0
            else:
                next_state[row][col] = 1 if live_neighbors == 3 or random.random() < revive_chance else 0
    
    return next_state

# Color render - shows transitions
def render_board(current_state, next_state):
    height = len(current_state)
    width = len(current_state[0])
    for row in range(height):
        colored_row = []
        for col in range(width):
            curr = current_state[row][col]
            nxt = next_state[row][col]
            
            if nxt == 1 and curr == 0:
                colored_row.append(AQUA_NEW)      # new birth
            elif nxt == 1:
                colored_row.append(BLUE_OLD)      # survived
            elif curr == 1:
                colored_row.append(DARK_BLUE_DIE) # just died
            else:
                colored_row.append(DEAD_LONG)     # long dead
        
        print(''.join(colored_row))

# Config menu
def get_user_config():
    print("\n=== Conway's Game of Life - Config ===")
    
    width = int(input("Field width [40-120, default 70]: ") or "70")
    width = max(40, min(120, width))
    
    height = int(input("Field height [20-60, default 35]: ") or "35")
    height = max(20, min(60, height))
    
    delay = float(input("Speed (delay/sec) [0.05-0.5, default 0.12]: ") or "0.12")
    delay = max(0.05, min(0.5, delay))
    
    revive = input("Revive dead cells? (y/n): ").lower().startswith('y')
    revive_chance = 0.02 if revive else 0
    
    print(f"\nConfig: {width}x{height}, delay={delay}s, revive={revive_chance>0}")
    input("Press Enter to start...")
    
    return width, height, delay, revive_chance

# Main game loop
if __name__ == "__main__":
    while True:
        width, height, delay, revive_chance = get_user_config()
        state = random_state(width, height)
        generation = 0
        
        print("\n=== Starting Game ===")
        print("Ctrl+C to stop and reconfigure")
        
        try:
            while True:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"=== Life | {width}x{height} | gen:{generation} | revive:{revive_chance>0} ===")
                
                next_state = next_board_state(state, revive_chance)
                render_board(state, next_state)
                
                time.sleep(delay)
                state = next_state
                generation += 1
                
        except KeyboardInterrupt:
            print("\n--- Stopped. New config... ---")
            continue
