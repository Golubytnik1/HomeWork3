# class SuperHero:
#     people = 'people'
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#
#     def realname(self):
#          return f'{self.name}'
#
#     def hpx2(self):
#         return f'{self.health_points * 2}'
#
#     def __str__(self):
#         return  f'{self.nickname, self.superpower, self.health_points}'
#
#     def __int__(self):
#         return len(self.catchphrase)
#
# Hero = SuperHero('Ben', 'Batman', 'деньги', 200, 'все хотят от меня шоу')
# Hero.realname()
# Hero.hpx2()
#
# print(Hero.realname())
# print(Hero.hpx2())
#
# class Earth(SuperHero):
#     sign = True
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.damage = damage
#         self.fly = fly
#
#     def hpx2(self):
#         return f'{self.health_points ** 2}'
#
#     def fly_h(self):
#         self.fly = True
#
#     def phrase(self):
#         print('fly in the True_phrase')
#
#
# Earth_h = Earth('Bob', 'Stebel', 'laser', 100, 'babushka boi')
# Earth_h.hpx2()
# Earth_h.phrase()
# print(Earth_h.hpx2())
#
#
# class Air(SuperHero):
#     cape = True
#
#     def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
#         SuperHero.__init__(self,name,nickname,superpower,health_points,catchphrase)
#         self.damage = damage
#         self.fly = fly
#
#     def hpx2(self):
#         return f'{self.health_points **2}'
#
#     def fly_h(self):
#         self.fly = True
#
#     def phrase(self):
#          print('fly in the True_phrase')
#
# Air_h = Air('carl', 'invisy', 'invisible', 30, 'where am i')
# Air_h.hpx2()
# Air_h.phrase()
# print(Air_h.hpx2())


# class Villain(Air):
#     people = 'monster'
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
#         super().__init__(name, nickname, superpower, health_points, catchphrase, damage=False, fly=False)
#
#     def gen_x(self):...
#
#     def crit(self):
#         print(f'{self ** 2}')
#
# evil = Villain('Ivan', 'kuvalda', 'strength', 300, 'я бью 2 раза')
# Villain.crit(Air_h.damage)


"""14.12.2022 - dz"""

class Bank:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        cash = int(input('Пополнить баланс на сумму:'))
        self._balance += cash

    def _kill(self):
        self._balance *= 0

    def __jackpot(self):
        self._balance *= 10

    def _copy(self):
        aiperi._balance += amir._balance
        print(f'Ваш баланс: {amir._balance}\n'
              f'Баланс друга: {aiperi._balance}')

    """extra task"""
    def _extra(self):
        aiperi._balance += amir._balance
        amir._balance *= 0
        print(f'Ваш баланс: {amir._balance}\n'
              f'Баланс друга: {aiperi._balance}')

amir = Bank('Amir', 2000)
aiperi = Bank('Aiperi', 4000)

# amir.moneyX()
# amir._kill()
# amir._Bank__jackpot()
amir._copy()
# amir._extra()