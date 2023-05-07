#1.Створюємо функцію normalize(name), для нормалізації назв файлів.\
#2. Транслітеруєо кирилицю за допомогою цикла for
#3. Замінюємо усі літери окрім букв латинського алфавіту та цифр, на символ "_"
#4. Потім пишемо функцію яка буде сортирувати файли за умової задачі використаємо  import os, def_sort_files(path): images [] video []
import os
import sys
import shutil
from pathlib import Path
#Перевірка на розширення.
def category(extension):
    if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
        return 'images'
    elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
        return 'video'
    elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
        return 'documents'
    elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
        return 'audio'
    elif extension in ['ZIP', 'GZ', 'TAR']:
        return 'archives'
    else:
        return 'Unknown extensions'

#Тут я використав код який ми робили для транслітерації у 4 чи 5 модулі. Та додав заміну через replace
def normalize(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    
    return name.translate(TRANS, '_').replace('_', '').replace(' ', '_')
        
          
def sort_files(path):
    # files = os.listdir(path)
    # known_ext = []
    # unkown_ext = []
    # for file in files:
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        # Якщо це папка, рекурсивно викликаємо sort_files для неї
        if os.path.isdir(item_path):
            sort_files(item_path)
            # Якщо папка стала пустою, видаляємо її
            if not os.listdir(item_path):
                os.rmdir(item_path)
        
        # Якщо це файл
        elif os.path.isfile(item_path):
            # Отримуємо розширення файлу
            extension = item.split('.')[-1].upper()
            
            # Якщо розширення відоме, переміщуємо файл
            if extension in ['JPEG', 'PNG', 'JPG', 'SVG', 'AVI', 'MP4', 'MOV', 'MKV', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'MP3', 'OGG', 'WAV', 'AMR']:
                category_folder = category(extension)
                category_path = os.path.join(path, category_folder)
                
                if not os.path.exists(category_path):
                    os.mkdir(category_path)
                
                src_path = os.path.join(path, item)
                dst_path = os.path.join(category_path, item)
                shutil.move(src_path, dst_path)
            
            # Якщо розширення невідоме, не робимо нічого
            else:
                pass
                
# sort_files(Path(sys.argv[1]))
sort_files(Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.'))

# sort_files(Path(path))

# Метод 1 ручного ввода через інпут.
# path = Path(input("Введіть шлях до папки: "))
# sort_files(Path(path))
