print('Hello from repository!')
import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()
    
    # Читаем значение переменной AUTHOR
    author = os.getenv("AUTHOR")
    
    # Печатаем результат
    print(f"Автор проекта: {author}")

# Вызов функции (для проверки)
if __name__ == "__main__":
    print_author()
