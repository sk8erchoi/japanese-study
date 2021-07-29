import random
import time

import speech_recognition as sr

f = open('hiragana_words.csv', encoding='utf-8')
lines = f.readlines()
random.shuffle(lines)

r = sr.Recognizer()
mic = sr.Microphone()

for line in lines:
    if line.startswith('#'):
        continue

    hiragana, kanji, pronunciation = line.rstrip().split(',')

    correct = None
    while not correct:
        if correct is None:
            print('Read this word!:')
        else:
            print('Let\'s try again:')

        print(hiragana)
        input('Press Enter when you ready and then read it ...')

        ans = None
        while not ans:
            with mic as source:
                audio = r.listen(source)
            try:
                print('I think you said ...', end=' ')
                ans = r.recognize_google(audio, language='ja')
            except sr.UnknownValueError:
                input('nothing. Please press Enter and say it again ...')

        print(ans)

        if kanji == ans:
            correct = True
            print('You\'re right!')
        else:
            correct = False
            print(f'Actually, {hiragana} is pronounced \'{pronunciation}\'.')

    print('-' * 20)
    time.sleep(2)
