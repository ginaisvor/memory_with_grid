# implementation of card game - Memory with grid

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
turns = 0

# helper function to initialize globals
def new_game():
    global deck, turns, flips, flip1, flip2, grid, exposed_grid
    flips = 0
    turns = 0
    flip1 = None
    flip2 = None
    deck = 2 * range(1, 9)
    random.shuffle(deck)

    grid = [[] for num in range(4)]
    i = 0
    while i < len(deck):
        for num in range(4):
            grid[num].append(deck[i])
            i += 1
    exposed_grid = [[False for num in range(len(grid))]for cell in range(len(grid[num]))]
          
def mouseclick(pos):
    global turns, flips, flip1, flip2, exposed_grid
    if not exposed_grid[pos[1]//100][pos[0]//50]:
        if flips == None or flips == 0:
            exposed_grid[pos[1]//100][pos[0]//50] = True
            flip1 = (pos[1] // 100, pos[0]//50)
            flips = 1
        elif flips == 1: 
            exposed_grid[pos[1]//100][pos[0]//50] = True
            flip2 = (pos[1] // 100, pos[0]//50)
            flips = 2
            turns += 1
        else:
            if grid[flip1[0]][flip1[1]] != grid[flip2[0]][flip2[1]]:
                exposed_grid[flip1[0]][flip1[1]] = False
                exposed_grid[flip2[0]][flip2[1]] = False              
            exposed_grid[pos[1]//100][pos[0]//50] = True
            flips = 1
            flip1 = (pos[1] // 100, pos[0]//50)
            flip2 = None
    return turns
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global turns
    height = 50    
    for num in range(len(grid)):
        width = 25        
        for cell in range(len(grid[num])):            
            if exposed_grid[num][cell]:
                canvas.draw_text(str(grid[num][cell]), (width-15, height + 20), 50, 'blue')
            else:
                canvas.draw_image(image, (413 / 2, 620 / 2), (413, 620), (width, height), (50, 100))
            width += 50
        height += 100    
        
    label.set_text("Turns = " + str(turns))    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 200, 400)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
image = simplegui.load_image('https://image.shutterstock.com/image-vector/playing-card-back-side-600w-90984266.jpg')
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
