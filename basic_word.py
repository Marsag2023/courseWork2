class BasicWord:
    """
    Создаем класс для обработки вопросов и ответов игрока
    **Поля:**
    - исходное слово,
    - набор допустимых подслов.
    **Методы:**
    - проверку введенного слова в списке допустимых подслов (вернет bool),
    - подсчет количества подслов (вернет int).
       """

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def checking_word_in_list(self, word_input):
        """
        Проверкa введенного слова в списке допустимых подслов
        """
        if word_input in self.subwords:
            return True
        else:
            return False

    def count_subwords(self):
        """
        Подсчет количества подслов
        """
        counts = self.subwords
        return int(len(counts))

    def __repr__(self):
        """

        """
        return f'Составьте {len(self.subwords)} слов из слова {self.word.upper()}'
