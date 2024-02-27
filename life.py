# Imports
import time
import pygame
import numpy as np

# Define colors for the background, grid, and next state of cells
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (170, 170, 170)

# Set the window caption
pygame.display.set_caption('Game of Life (Paused)')

def update(screen, cells, size, with_progress=False):
    """
    Update the state of the cells based on the rules of Conway's Game of Life.
    
    Args:
    - screen: Pygame surface object representing the display window
    - cells: 2D NumPy array representing the current state of the cells
    - size: size of each cell in pixels
    - with_progress: flag to indicate whether to show progression colors
    
    Returns:
    - updated_cells: 2D NumPy array representing the updated state of the cells
    """
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    # Iterate over each cell in the grid
    for row, col in np.ndindex(cells.shape):
        
        # Count the number of alive neighbors
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        
        # Apply the rules of the game
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
                
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
                    
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
                    
        # Draw the cell on the screen
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

def main():
    """
    Main function to initialize the game and handle user input.
    """
    pygame.init()
    screen = pygame.display.set_mode((1800, 1000))
    
    # Initialize the grid of cells
    cells = np.zeros((100, 180))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()
    
    running = False
        
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
                    
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    return
                    
                elif event.key == pygame.K_c:
                    cells = np.zeros((100, 180))
                    screen.fill(COLOR_GRID)
                    update(screen, cells, 10)
                    pygame.display.update()
                    
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, pos[0] // 10] = 0
                    update(screen, cells, 10)
                    pygame.display.update()
                        
        # Update the screen
        screen.fill(COLOR_GRID)
        
        if running:
            pygame.display.set_caption('Game of Life (Active)')
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()
        else:
            pygame.display.set_caption('Game of Life (Paused)')
            
        time.sleep(0.01)
            
if __name__ == '__main__':
    main()