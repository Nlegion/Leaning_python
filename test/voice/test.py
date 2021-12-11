import pyttsx3
import time

engine = pyttsx3.init()
engine.say('Алиса!')
time.sleep(1)
engine.say('Пошла ты, Алиса!')
engine.runAndWait()

# import speech_recognition as sr
#
# # for index, name in enumerate(sr.Microphone.list_microphone_names()):
# #     print('Микрофон с именем',index,name)
#
# r = sr.Recognizer()
# with sr.Microphone(device_index=0) as source:
#     print('начало теста')
#     audio = r.listen(source)
#
# query = r.recognize_google(audio, language='ru-RU')
# print(' Сказано: ' + query.lower())
