from bs4 import BeautifulSoup  # Импортируем библиотеку BeautifulSoup для парсинга HTML
import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов
from googletrans import Translator  # Импортируем Translator для перевода текста

def fetch_random_word():
    """Получает случайное слово и его определение с сайта randomword.com."""
    url = "https://randomword.com/"  # URL сайта, где будем получать слово
    response = requests.get(url)  # Выполняем GET-запрос
    soup = BeautifulSoup(response.text, "html.parser")  # Парсим HTML-ответ
    # Извлекаем слово и его определение по ID
    english_word = soup.find("div", id="random_word").text.strip()
    word_definition = soup.find("div", id="random_word_definition").text.strip()
    return english_word, word_definition  # Возвращаем слово и определение

def translate_texts(texts, dest="ru"):
    """Переводит список текстов на указанный язык."""
    translator = Translator()  # Инициализируем переводчик
    translations = translator.translate(texts, dest=dest)  # Выполняем перевод
    return [translation.text for translation in translations]  # Возвращаем переводы

def get_russian_word():
    """Получает случайное слово с сайта и переводит его на русский язык, также переводит определение слова."""
    try:
        # Получаем случайное слово и его определение
        english_word, word_definition = fetch_random_word()
        # Переводим слово и определение
        russian_word, russian_word_definition = translate_texts([english_word, word_definition])
        # Возвращаем переведенные данные в виде словаря
        return {
            "russian_word": russian_word,
            "russian_word_definition": russian_word_definition
        }
    except Exception as e:
        # Обрабатываем исключения и выводим сообщение об ошибке
        print(f"Ошибка: {e}")
        return None

def word_game():
    """Запускает игру, где игроку нужно угадать случайное русское слово по его определению."""
    print("Добро пожаловать в игру!")  # Приветствие
    while True:
        # Получаем случайное слово с переводом
        word_dict = get_russian_word()
        if word_dict is None:  # Проверяем, удалось ли получить данные
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        # Извлекаем слово и его определение
        word = word_dict["russian_word"]
        word_definition = word_dict["russian_word_definition"]

        # Выводим определение и запрашиваем у пользователя ответ
        print(f"Значение слова: {word_definition}")
        user_answer = input("Что это за слово? - ")
        if user_answer == word:  # Проверяем ответ пользователя
            print("Всё верно!")
        else:
            print(f"Неправильно. Правильное значение: {word}")

        # Спрашиваем, хочет ли пользователь сыграть ещё раз
        if input("Хотите сыграть еще раз? (да/нет) ").lower() != "да":
            print("Спасибо за игру!")
            break  # Выход из цикла, если пользователь не хочет продолжать

if __name__ == "__main__":
    word_game()  # Запускаем игру, если скрипт выполнен напрямую
