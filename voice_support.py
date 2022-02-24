import pyttsx3
import speech_recognition as sr
import random 
import webbrowser as wb
import functionality as fn
import json
import PyQt5
import sys
import ytest
from Support1 import *
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets

v = sr.Recognizer()
r = pyttsx3.init()
mic = sr.Microphone(device_index=1) #определяем микрофон

#r.setProperty('rate', )
#r.setProperty('volime', 1)
voices = r.getProperty('voices')
r.setProperty('voice', 'ru')

file = open('base1.json', 'r').read()

ui = Ui_MainWindow()
for voice in voices:
    if voice.name == 'Microsoft Irina Desktop':
        r.setProperty('voice', voice.id)
def talk(word): #функция для голоса помошника
    r.say(word) #говорим слова
    r.runAndWait() #ждёт пока договорим    
talk('Здравствуйте') or fn.hitime() # скажет 'Здравствуйте' 
def record(): #функция записи
    with mic as source:
        print('Настраиваюсь...')
        v.adjust_for_ambient_noise(source, duration=2.5) #настраиваем шумоподавление
        print('Слушаю, говорите')
        audio = v.listen(source)
        print('Услышал')
        
    try:
        query = v.recognize_google(audio, language='ru-RU')
        text = query.lower()
        print(text)
        return text
    except sr.UnknownValueError:
        return record()
    except sr.RequestError:
        print('Уменя нет доступа к серверам')
    except:
        print('Error 404')

def hi():
    lst = ['Привет чувак','Сколько лет, сколько зим', 'И тебе не хворать', 'Здравствуйте', 'Привет мой разработчик']
    talk(random.choice(lst))
def quit1():
    tsil = ['Жаль что ты уходишь', 'Рада была помочь', 'Пока пока', 'Всегда к вашим услугам']
    talk(random.choice(tsil))
    exit()
def start():
    myquestions(record())

def AI(command):
    pars = json.loads(file)
    if command is pars:
        z = random.choice(pars[command])
        dlina = len(z)
        if dlina > 1:
            talk(z)
        else:
            z = pars[command]
            talk(z)
    else:
        talk('Я не знаю что сказать научите меня, пожалуйста)')
        talk('Задайте вопрос')
        a = record()
        talk('скажите как ответить')

        b = record() #значение

        pars[a] = b #ключ и значение (то чему научили)

        with open('temp/base1.json', 'w') as json_file: #открываем файл для записи

            json.dump(pars,json_file,indent=2,sort_keys=True,ensure_ascii=False) #переменную, которую будем менять, новыми значениями и вывод будет ключ значение, сортировка и стандартная кодир

def myquestions(command):
    if 'привет' in command:
        hi()
    elif 'пока' in command:
        quit1()
    elif 'моя школа' in command:
        talk('Я не знаю, не расскажете?')
    elif ('что делаешь' in command) or ('чем занимаешься' in command):
        kit = ['Общаюсь с вами', 'Ничем', 'Жду ваших указаний', 'Не скажу, секрет']
        talk(random.choice(kit))
    elif ('что ты умеешь' in command) or ('что ты можешь' in command):
        talk('Сейчас покажу...')
        talk('Я могу следующее: находить, показывать погоду, время, заходить в социальные сети и так далее)')
    elif 'погода' in command:
        talk('Сейчас открою...')
        for i in words:
            command = command.replace(i, '')
            for j in remove:
                command = command.replace(j, '')
                command.strip()
        
        ui.textEdit.load(QtCore.QUrl(f'https://yandex.ru/pogoda/rostov-na-donu?lat=47.222078&lon=39.720349'))
    elif ('ютуб' in command) or ('ютьюб' in command) or ('youtube' in command):
        talk('Слушаюсь и повинуюсь')
        wb.open('https://www.youtube.com/')

    elif 'вконтакте' in command:
        talk('Мигом!')
        wb.open('https://vk.com/')

    elif 'кто тебя создал' in command:
        talk('Меня создал Денис Мудрая Голова')
        print('Меня создал Денис Мудрая Голова')
    elif 'время' in command or 'текущее время' in command:
        fn.time()
    elif ('найти' in command) or ('найди' in command):
        words = ('найди','найти','ищи','кто такой', 'что такое', 'о том')
        remove = ['пожалуйста', 'ладно','давай', 'сейчас']
        for i in words:
            command = command.replace(i, '')
            for j in remove:
                command = command.replace(j, '')
                command.strip()
        talk('Открываю...')
        ui.textEdit.load(QtCore.QUrl(f'https://www.google.com/search?q={command}&oq={command}'
                             f'81&aqs=chrome..69i57j46i131i433j0l5.2567j0j7&sourceid=chrome&ie=UTF-8'))
    else:
        AI(command)

#while True:
#    start()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.resize(1340, 615)
ui.pushButton.clicked.connect(start)
ui.pushButton_2.clicked.connect(quit)
sys.exit(app.exec())
