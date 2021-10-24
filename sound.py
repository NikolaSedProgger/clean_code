import pygame
from alive_progress import alive_bar

FREQ = 44100
BITSIZE = -16
CHANNELS = 2
BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}


def playsound(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def _play_morse_sound(code):
    print()
    with alive_bar(len(code), bar = 'brackets', spinner = 'dots_waves2') as bar:
        for dip in code:
            sound = pygame.mixer.Sound(MORSE_SOUND[dip])
            playsound(sound)
            bar() 
    print()

def play_morse_sound(morz):
    print()
    with alive_bar(len(morz), bar = 'brackets', spinner = 'dots_waves2') as bar:
        if morz[0] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[0] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[0] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[1] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[1] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[1] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[2] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[2] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[2] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[3] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[3] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[3] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[4] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[4] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[4] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[5] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[5] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[5] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()  
        if morz[6] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[6] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[6] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[7] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[7] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[7] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[8] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[8] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[8] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[9] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[9] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[9] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[10] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[10] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[10] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[11] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[11] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[11] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[12] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[12] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[12] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[13] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[13] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[13] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[14] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[14] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[14] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[15] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[15] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[15] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[16] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[16] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[16] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[17] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[17] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[17] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[18] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[18] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[18] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[19] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[19] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[19] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[20] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[20] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[20] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[21] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[21] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[21] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[22] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[22] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[22] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[23] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[23] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[23] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[24] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[24] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[24] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[25] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[25] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[25] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[26] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[26] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[26] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[27] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[27] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[27] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[28] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[28] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[28] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
    print()
