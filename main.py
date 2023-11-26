import platform
from gtts import gTTS
import os
import playsound
import pygame


def speaker(token):
    tts = gTTS(token, lang="en")
    filename = "speach.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def speaker_pygame(token):
    pygame.init()
    tts = gTTS(token, lang="en")
    filename = "speach.mp3"
    # os.remove(filename)
    tts.save(filename)
    pygame.mixer.music.load(filename)
    end_event = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(end_event)
    pygame.mixer.music.play()
    pygame.event.wait()
    os.remove(filename)


if platform.system() == "Darwin":
    while True:
        token = input("Please tell me what to say : ")
        command = f"say {token}"
        os.system(command)
else:
    while True:
        token = input("Please tell me what to say : ")
        # speaker(token)
        speaker_pygame(token)
