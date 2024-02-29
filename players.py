class Players:
    """
    Создаем класс для обработки вопросов и ответов игрока
    **Поля:**
    - имя пользователя,
    - использованные слова пользователя.
    **Методы:**
    - получение количества использованных слов (возвращает int);
    - добавление слова в использованные слова (ничего не возвращает);
    - проверка использования данного слова до этого (возвращает bool).
       """

    def __init__(self, name_player):
        self.name_player = name_player
        self.player_words_used = []
        # self.player_words_used = player_words_used

    def check_word(self, word_good):
        """
        Проверка использования данного слова до этого
        """
        if word_good in self.player_words_used:
            return True
        else:
            return False

    def word_add(self, word_good):
        """
        Добавление слова в использованные слова
        Печатает угаданные слова
        """
        self.player_words_used.append(word_good)
        print(self.player_words_used)

    def count_words_used(self):
        """
        Получение количества использованных слов (возвращает int);
        :return:
        """
        return int(len(self.player_words_used))

    def __repr__(self):
        """

        """
        return f'{self.name_player}'
