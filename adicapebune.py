from gtts import gTTS
import pygame
from io import BytesIO
from playsound import playsound
from sys import argv


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


playsound('C:\\Users\Victor\PycharmProjects\\twilight-scene-de-sarutat\\part2.mp3')
say(argv[1])
# playsound('part2.mp3')