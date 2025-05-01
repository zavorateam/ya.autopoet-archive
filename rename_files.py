import os
import re

def find_next_available_number(directory):
    # Получаем список всех файлов в директории
    files = os.listdir(directory)
    
    # Создаем множество для хранения существующих номеров
    existing_numbers = set()
    
    # Регулярное выражение для поиска файлов с числовыми именами
    pattern = r'^(\d+)(?:\s*\(2\))?$'
    
    for file in files:
        match = re.match(pattern, file)
        if match:
            number = int(match.group(1))
            existing_numbers.add(number)
    
    # Находим первый свободный номер
    next_number = 1
    while next_number in existing_numbers:
        next_number += 1
    
    return next_number

def rename_files():
    # Получаем текущую директорию
    current_dir = os.getcwd()
    
    # Получаем список всех файлов
    files = os.listdir(current_dir)
    
    # Регулярное выражение для поиска файлов с суффиксом (2)
    pattern = r'^(\d+)\s*\(2\)$'
    
    for file in files:
        match = re.match(pattern, file)
        if match:
            # Находим следующий доступный номер
            next_number = find_next_available_number(current_dir)
            
            # Формируем новое имя файла
            new_name = str(next_number)
            
            # Переименовываем файл
            try:
                os.rename(file, new_name)
                print(f'Переименован файл {file} в {new_name}')
            except Exception as e:
                print(f'Ошибка при переименовании файла {file}: {str(e)}')

if __name__ == '__main__':
    rename_files() 