#!/usr/bin/python
import pygame, sys



# Handle args
if len(sys.argv) < 2:
    raise Exception ('./record_song_data.py audio.mp3')
audioFile = sys.argv[1]
outputFile = audioFile.replace("mp3", "txt")


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
# Set the width and height of the screen [width, height]
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Billy Bass Motion Recorder")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class FishState:
    def __init__(self):
        self.isMouthOpen = 0
        self.isHeadOut = 0
        self.isTailOut = 0
        self.state = ""
        self.time = 0.0
    def buildState(self):
        #  Format:  time: mouth, head, tail
        self.state = "%d   %d   %d " % (self.isMouthOpen, self.isHeadOut, self.isTailOut)
        return (self.state)
    def report(self):
        print self.state + "\n"

def writeOutput(inList):
    f = open(outputFile, 'w')
    for line in inList:
        f.write(line + '\n')

def playSong(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print 'playing song: ' + filename + " at volume " + str(pygame.mixer.music.get_volume())


# -------- Main Program Loop -----------

fish = FishState()
eventList = []
eventList.append("# " + audioFile)
currentTime = 0.0
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            writeOutput(eventList)
        elif event.type == pygame.KEYDOWN:
            fish.time = float(pygame.mixer.music.get_pos()) / 1000.0
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_TAB:
                print 'Tab down!'
                fish.isHeadOut = 1
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))
            elif event.key == pygame.K_SPACE:
                fish.isMouthOpen = 1
                print 'Space bar down!'
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))
            elif event.key == pygame.K_RETURN:
                print 'Enter down!'
                fish.isTailOut = 1
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))
            elif event.key == pygame.K_s:
                print 'Starting song!'
                playSong(audioFile)
            elif event.key == pygame.K_ESCAPE:
                print 'Quitting... !'
                done = True
                writeOutput(eventList)
        elif event.type == pygame.KEYUP:
            fish.time = float(pygame.mixer.music.get_pos()) / 1000.0
            if event.key == pygame.K_TAB:
                print 'Tab up!'
                fish.isHeadOut = 0
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))
            elif event.key == pygame.K_SPACE:
                print 'Space bar up!'
                fish.isMouthOpen = 0
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))
            elif event.key == pygame.K_RETURN:
                print 'Enter up!'
                fish.isTailOut = 0
                eventList.append("%-7.1f : %s" % (fish.time, fish.buildState()))

    # --- Game logic should go here
    currentStateString ="%-7.1f : %s" % (fish.time, fish.buildState())

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Courier', 16, True, False)
    instructions = []
    instructions.append("=============== Press 's' to start ================== ")
    instructions.append("=============== Press 'ESC' to quit ================= ")
    instructions.append("")
    instructions.append("=================== CONTROLS ======================== ")
    instructions.append("Control head with  Tab:   down=head out, up=head in ")
    instructions.append("Control mouth with Space: down=talking,  up=not ")
    instructions.append("Control tail with  Enter: down=tail out, up=tail in ")
    instructions.append("")
    instructions.append("============== fish.state (on event) ================ ")
    instructions.append(" time :  mouth, head, tail ")
    instructions.append(currentStateString)
    height = 10
    for text in instructions:
        # Render the text. "True" means anti-aliased text.
        # Black is the color. This creates an image of the
        # letters, but does not put it on the screen
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




