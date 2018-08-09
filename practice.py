import requests
import os

def translate_it(text, file_language, translate_language = "ru"):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180809T165827Z.b692203e070b578c.fc51d087de7b69e1f761b5e39547b99922db8372'

    params = {
        'key': key,
        'lang': file_language + '-' + translate_language,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

def read_file(file_name):

    with open(file_name, "r") as file_read:
        file_for_translate = file_read.read()

    return file_for_translate

def write_file(file_name, text_translate):

    with open(file_name, "a") as file_write:
        file_write.write(text_translate)

current_dir = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(current_dir):
    if file.endswith(".txt") and not file.startswith("translate_"):
        text = read_file(file)
        text_translate = translate_it(text, file[:2].lower())
        write_file(os.path.join(current_dir, "translate_" + file), text_translate)
        print("Файл {} был переведен.".format(file))