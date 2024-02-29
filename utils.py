# Импортируем необходимые для работы функции и классы

import random
import requests
from basic_word import BasicWord
from players import Players


def load_random_word():
    """
    Получает список слов с внешнего ресурса, выберает случайное слово,
    создает экземпляр класса `BasicWord`, возращает этот экземпляр.
    """
    response = requests.get('https://www.jsonkeeper.com/b/6V41')
    words_subwords = response.json()
    word_subwords = random.choice(words_subwords)
    word, subwords = word_subwords.values()
    word_play = BasicWord(word, subwords)
    return word_play


def beginning_game():
    """
    Начало игры
    """
    name = input("Введите свое имя\n").strip().capitalize()
    name_player = Players(name)
    print(f'Привет, {name_player}')
    print("""Слова должны быть не короче 3 букв.
Вводите строчными буквами.    
Чтобы закончить игру, угадайте все слова
или напишите "stop" или "стоп".
""")
    return name_player


def game_play():
    """
    Запускаем цикл, пока количество угаданных слов не сравняется с количеством слов
    В каждойй итерации получаем от пользователя слово, выполняем несколько проверок:
    Если слово короче 3 букв, если слова нет в списке допустимых, если слово уже было
    угадано пользователем. Если слово stop или стоп, то игра прекращается.
    выводим статистику игры
    """
    word_play = load_random_word()
    name_player = beginning_game()
    print(f'{word_play}\nПоехали, ваше первое слово?')
    while name_player.count_words_used() < word_play.count_subwords():
        word_input = input().strip().lower()
        if int(len(word_input)) <=2:
            print("Cлишком короткое слово")
        elif word_input =="stop" or word_input=="стоп":
            break
        elif not word_play.checking_word_in_list(word_input):
            print("Неверно")
        elif name_player.check_word(word_input):
            print(f'Уже использовано\nВы угадали {name_player.player_words_used}')
        elif word_play.checking_word_in_list(word_input):
            name_player.word_add(word_input)
            print("Верно")
        print("Введите следующее слово")
    print(f"Игра завершена, вы угадали {name_player.count_words_used()} слов(а)!")


