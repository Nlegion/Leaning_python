import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
    "alias": ('компьютер'),
    "tbr": ('привет', 'скажи', 'озвучь', 'сколько', 'расскажи',),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'включи радио', 'воспроизведи'),
        "stupid": ('расскажи анекдот', 'рассмеши меня', 'пошути'),
        "fuck_alice": ('пошли ее')
    }
}


# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    if speak_engine._inLoop:
        speak_engine.endLoop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak('Сейчас дохуя минут')
    elif cmd == "radio":
        speak('Сейчас не работает')
    elif cmd == "stupid":
        speak('Тоже мне... Нашел Петросяна')
    elif cmd == "fuck_alice":
        speak('Алиса!')
        time.sleep(0.1)
        speak('Пошла ты, Алиса!')
    else:
        speak('Команда не распознана')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=0)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
# speak_engine.setProperty('voice', voices[0].id)

speak('Добрый день!')
speak('Компьютер на связи!')

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)
