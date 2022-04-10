from random import shuffle

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"
             ]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "jack", "queen",
              "king", "ace"
              ]

    def __init__(self, v, s):
        #создаем карту
        """ v, s - целые числа"""
        self.value = v
        self.suit = s

    def __lt__(self, card2):
        #переопределяем метод "меньше чем" для сравнения карт-объектов далее
        if self.value < card2.value:
            return True
        elif self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, card2):
        #переопределяем метод "больше чем" для сравнения карт-объектов далее
        if self.value > card2.value:
            return True
        elif self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        #переопределяем метод ПРИНТ для карты-объекта
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v
    
class Deck:
    #создаем колоду карт
    def __init__(self):
        #в этом списке будут храниться карты-объекты
        self.cards = []                         
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        #тасуем нашу колоду карт
        shuffle(self.cards)
       
    def rm_card(self):
        #удаляет последнюю карту из колоду
        #и тут же возвращает ее в переменную
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        #определяем количество выигранных раундов конкретного игрока
        self.card = None
        #карта игрока, которая у него на руках в конкретном раунде
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Введите имя первого игрока:  ")
        name2 = input("Введите имя первого игрока:  ")
        self.deck = Deck()
        #создаем колоду в классе Игра
        self.p1 = Player(name1)
        #объект 1-й игрок
        self.p2 = Player(name2)
        #объект 2-й игрок

    def wins(self, winner):
        #будет показывать кто выиграл в конкретном раунде
        #после того как игроки достали карты из колоды
        #winner в данном случае это имя игрока (но не объект)
        w = "{} забирает карты\n" \
            .format(winner)
        print(w)

    def play_game(self):
        cards = self.deck.cards
        #создали переменную для колоды deck, которую мы создали выше в классе Игра
        print("Поехали!\n")
        while len(cards) >= 2:
            #цикл для игры пока не кончатся карты или пока не будет нажата Х
            h = "Нажмите Х для выхода. Нажмите любую другую клавишу для начала игры  \n"
            response = input(h)
            if response == "X":
                break
            p1c = self.deck.rm_card()
            #последняя карта-объект из колоды достается для 1-го игрока и удаляется из колоды
            p2c = self.deck.rm_card()
            #последняя карта-объект из колоды достается для 2-го игрока и удаляется из колоды
            p1n = self.p1.name
            #имя 1-го игрока-объекта
            p2n = self.p2.name
            #имя 1-го игрока-объекта
            self.draw(p1n, p1c, p2n, p2c)
            #надпись перед раундом игры
            #здесь p1c, p2c это карты-объекты
            if p1c > p2c:
                self.p1.wins +=1
                #количество выигранных раундов для игрока-объекта
                self.wins(p1n)
            else:
                self.p2.wins +=1
                self.wins(p2n)
        win = self.winner(self.p1, self.p2)
        #переменная для определения победителя
        print("Игра окончена. {} выиграл!".format(win))

    def draw(self, p1n, p1c, p2n, p2c):
        #будет показывать какие карты вытащили игроки
        print("{} кладет {}, а {} кладет {}".format(p1n, p1c, p2n, p2c))
        #print(d)
            
    def winner(self, p1, p2):
        #p1, p1 здесь объекты-игроки
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        return "Ничья! Никто не"



game = Game()
#определяем объект Игра
game.play_game()
#запускаем метод Играть для объекта Игра
          



#deck = Deck()                                   #это первая колода кард,
                                                #в ней все карты это объекты Card
#for card in deck.cards:
#        print(card)
