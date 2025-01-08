from gtts import gTTS
import pygame
from io import BytesIO
from sys import argv    
import os



def say(text):
    tts = gTTS(text=text, lang='ro')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


os.system('afplay -v 10 part1.mp3 ')
say(argv[1])
os.system('afplay -v 10 part2.mp3 ')