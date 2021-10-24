from re import S
import pygame
import os
import requests
from alive_progress import alive_bar
import time


BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}

pygame.init()

os.system('cls||clear')
pygame.mixer.init(BUFFER)
morse_code = {
     'а': '.-',
     'б': '-...',
     'в': '.--',
     'г': '--.',
     'д': '-..',
     'е': '.',
     'ж': '...-',
     'з': '--..',
     'и': '..',
     'й': '.---',
     'к': '-.-',
     'л': '.-..',
     'м': '--',
     'н': '-.',
     'о': '---',
     'п': '.--.',
     'р': '.-.',
     'с': '...',
     'т': '-',
     'у': '..-',
     'ф': '..-.',
     'х': '....',
     'ц': '-.-.',
     'ч': '---.',
     'ш': '----',
     'щ': '--.-',
     'ъ': '.--.-.',
     'ы': '-.--',
     'ь': '-..-',
     'э': '..-..',
     'ю': '..--',
     'я': '.-.-',
     '1': '.----',
     '0': '-----',
     '2': '..---',
     '3': '...--',
     '4': '....-',
     '5': '.....',
     '6': '-....',
     '7': '--...',
     '8': '---..',
     '9': '----.',
     ',': '--..--',
     '.': '.-.-.-',
     '?': '..--..',
     ';': '-.-.-.',
     ':': '---...',
     "'": '.----.',
     '-': '-....-',
     '/': '-..-.',
     '(': '-.--.-',
     ')': '-.--.-',
     ' ': '|',
     '_': '..--.-'
}
message = os.getenv('komanda', default='По-умолчанию')
message = message.lower()
adress = 'http://195.161.68.58'
for letter in message:
    message = message.replace(letter, morse_code[letter])


def connect_to_robot(adress):
    otvet = requests.get(adress)
    message = 'Проверка связи с роботом...'
    print(message)
    with alive_bar(len(message), bar='brackets', spinner='radioactive') as bar:
        for _ in range(len(message)):
            time.sleep(0.06)
            bar()
    os.system('cls||clear')
    if otvet.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')
    print()
connect_to_robot(adress)


def play_music(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def play_morze_music(morz):
    print()
    with alive_bar(len(morz), bar='brackets', spinner='dots_waves2') as bar:
        for i in range(len(morz)):
            if morz[i] == '.':
                play_music(pygame.mixer.Sound('dot.ogg'))
            elif morz[i] == '-':
                play_music(pygame.mixer.Sound('dash.ogg'))
            elif morz[i] == '|':
                play_music(pygame.mixer.Sound('long_silence.ogg'))
            bar()
    print()


def send_message_to_robot(adress, message):
    print('Отправка сообщения роботу...')
    otvet = requests.post(adress, message.encode('utf-8'))
    play_morze_music(message)
    if otvet.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    elif otvet.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')

send_message_to_robot(adress, message)
