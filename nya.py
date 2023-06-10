import time
import pyautogui
import random
import sys
import re

chars = {
'й':'q',
'ц':'w',
'у':'e',
'к':'r',
'е':'t',
'н':'y',
'г':'u',
'ш':'i',
'щ':'o',
'з':'p',
'х':'[',
'ъ':']',
'ф':'a',
'ы':'s',
'в':'d',
'а':'f',
'п':'g',
'р':'h',
'о':'j',
'л':'k',
'д':'l',
'ж':';',
"э":"'",
'\\':'\\',
'я':'z',
'ч':'x',
'с':'c',
'м':'v',
'и':'b',
'т':'n',
'ь':'m',
'б':',',
'ю':'.',
'ё':'`',

'Й':'Q',
'Ц':'W',
'У':'E',
'К':'R',
'Е':'T',
'Н':'Y',
'Г':'U',
'Ш':'I',
'Щ':'O',
'З':'P',
'Х':'{',
'Ъ':'}',
'Ф':'A',
'Ы':'S',
'В':'D',
'А':'F',
'П':'G',
'Р':'H',
'О':'J',
'Л':'K',
'Д':'L',
'Ж':':',
"Э":'"',
'/':'|',
'Я':'Z',
'Ч':'X',
'С':'C',
'М':'V',
'И':'B',
'Т':'N',
'Ь':'M',
'Б':'<',
'Ю':'>',
'Ё':'~'
}

specials = ": ; , . / ? [ ]{ } < > | ' \"".split(' ')

def translate_to_en(char):
    return chars[char]

def get_language(char):
    code = ord(char)
    isspecial = char in specials
    check = code > 0xA69D or code < 0x410 or isspecial
    return "en" if check else "ru"

def change_lang(lang):
    if lang == "en":
        pyautogui.hotkey('shift','altleft', '1')
    elif lang == "ru":
        pyautogui.hotkey('shift','altleft', '2')
        

def simulate_typing(text, startTabs, prevTabs):
    text = text.replace('\t', '')
    diff = startTabs - prevTabs
    if diff != 0:
        for tab in range(abs(diff)):
            if diff > 0:
                pyautogui.press("tab")
            else:
                pyautogui.hotkey("shift", "tab")
    
    prev_lang = 'en'
    for char in text:
        lang = get_language(char)
        if prev_lang != lang:
            change_lang(lang)
            prev_lang = lang
        if lang == 'ru':
            pyautogui.press(translate_to_en(char))
            print(translate_to_en(char), end='')
        else:
            pyautogui.press(char)
            print(char, end='')
        # Задержка между символами
        time.sleep(random.uniform(0.005, 0.05))
    change_lang("en")

def main():
    change_lang('en')
    time.sleep(1)
    file_path = "owo.txt"
    with open(file_path, "r", encoding="UTF-16 BE") as file:
        tabs = 0
        for f in file:
            if random.randint(0, 10) == 5:
                time.sleep(random.randint(2, 6))
            text = f
            text = re.sub('( ){2,4}', '\t', text)
            ntabs = text.count('\t')
            time.sleep(random.uniform(0.01,0.5)) 
            simulate_typing(text, ntabs, tabs)
            tabs = ntabs
            if bool(re.match('.*:$', text) or text.count(' {')) and (not re.match(".*:.*'", text)):
                print("@ auto tab detected @")
                tabs += 1

if __name__ == "__main__":
    main()
    