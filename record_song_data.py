#!/usr/bin/python
import pygame, sys
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Billy Bass Motion Recorder")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()




def playSong(filename):
    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    print 'playing song: ' + filename

    print 'vol:', pygame.mixer.music.get_volume()


# -------- Main Program Loop -----------

playSong(sys.argv[1])
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_TAB:
                print 'Tab down!'
            elif event.key == pygame.K_RIGHT:
                print 'Right arrow down!'
            elif event.key == pygame.K_SPACE:
                print 'Space bar down!'
            elif event.key == pygame.K_RETURN:
                print 'Enter bar down!'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                print 'Tab up!'
            elif event.key == pygame.K_RIGHT:
                print 'Right arrow up!'
            elif event.key == pygame.K_SPACE:
                print 'Space bar up!'
            elif event.key == pygame.K_RETURN:
                print 'Enter bar up!'

    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Courier', 16, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    instructions = []
    instructions.append("=================== CONTROLS ======================== ")
    instructions.append("Control head with  Tab:   down=head out, up=head in ")
    instructions.append("Control mouth with Space: down=talking,  up=not ")
    instructions.append("Control tail with  Enter: down=tail out, up=tail in ")
    height = 10
    for text in instructions:
        text = font.render(text, True, BLACK)
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [25, height])
        height = height + 25



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()




