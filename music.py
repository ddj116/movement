#!/usr/bin/python
import sys
import time
import pygame


def test(filename):
    pygame.mixer.init()
    pygame.video.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    print 'test'

#    while pygame.mixer.music.get_busy() == True:
#        continue

    print 'vol:', pygame.mixer.music.get_volume()
    while True:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
           print("w is pressed")
        if pressed[pygame.K_s]:
           print("s is pressed")
        time.sleep(0.01)

    print 'done'

    pygame.mixer.quit()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception ('music.py filename')

    test(sys.argv[1])
