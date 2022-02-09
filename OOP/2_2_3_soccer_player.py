# Создайте класс SoccerPlayer, у которого есть:
#
# 1. конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо
# создать 2 атрибута экземпляра: goals и assists - общее количество голов и передач игрока, изначально оба
# значения должны быть 0;
# 2. метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# 3. метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное значение
# равно единице. Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# 4. метод statistics, который вывод на экран статистику игрока в виде:
#          <Фамилия> <Имя> - голы: <goals>, передачи: <assists>
#
# Пример:
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"


class SoccerPlayer:

    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, score_goals=1):
        self.goals = score_goals + self.goals

    def make_assist(self, score_assist=1):
        self.assists = score_assist + self.assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics()
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics()
#
# Messi Leo - голы: 700, передачи: 500
# Kokorin Alex - голы: 1, передачи: 0
