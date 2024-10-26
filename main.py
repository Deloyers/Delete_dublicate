import os
import hashlib

def calculate_file_hash(file_path, chunk_size=8192):
    """Вычисляет хеш файла для проверки на дубликаты."""
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def find_and_remove_duplicates(directory):
    """Ищет и удаляет дубликаты файлов, оставляя только один оригинал."""
    hash_map = {}
    
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash in hash_map:
                print(f"Удаляю дубликат: {file_path}")
                os.remove(file_path)
            else:
                hash_map[file_hash] = file_path

# Укажите путь к директории, которую хотите проверить
directory_path = "/path/to/your/directory"
find_and_remove_duplicates(directory_path)
