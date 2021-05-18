# класс оргтехники
from abc import ABC, abstractmethod

class OrgTec(ABC):

    def __init__(self, power = 'OFF', soft_version = '1.0', network = 'disconnected'):
        self.power = power
        self.soft_version = soft_version
        self.network = network
    
    @abstractmethod
    def on_of():
        pass

    @abstractmethod
    def soft_update():
        pass

    @abstractmethod
    def net_connect():
        pass

class Printer (OrgTec):

    def on_of(self):
        if self.power == 'ON':
            print('Извлечение бумаги\nПарковка каретки')
            self.power = 'OFF'
            self.net_connect = 'disconnected'
        else:
            print('Проверка бумаги...\nпроверка чернил...\nпрочистка головки...')
            self.power = 'ON'

    def soft_update(self, version):
        print('Вставте флешку и одновременно нажмите кнопу питания и печати\n'
              'Загрузка обновления...\n'
              f'обновлено с {self.soft_version} до {version}')
        self.soft_version = version

    def net_connect(self):
        print('Подключи сетевой шнур\n Подключение к локальной сети...')
        self.network = 'Local'

    def print_some(self, copies):
        with open('to_print.txt', 'r') as f:
            text = (''.join(f.readlines()) + '\n') * int(copies)
            print(text.rstrip())

    def print_scan(self, copies):
        with open('scan.txt', 'r') as f:
            izo = (''.join(f.readlines()) + '\n') * int(copies)
            print(izo.rstrip())




class Skaner (OrgTec):

    def on_of(self):
        if self.power == 'ON':
            print('Паркрвка датчика')
            self.power = 'OFF'
        else:
            print('Проверка наличия документа...\n')
            self.power = 'ON'

    def soft_update(self, version):
        print('Подключись к компютеру и в сервисном приложении нажми "Обновить"\n'
              'Загрузка обновления...\n'
              f'обновлено с {self.soft_version} до {version}')
        self.soft_version = version
    def net_connect(self, version):
        print('Невозможно подключить к сети, только к компютеру')

    def scan (self, izo = ' /\__ /\ \n|  O_O  |\n \ ___ /'):
        print('Сканипую документ')
        with open('scan.txt', 'w') as f:
            f.write(izo)

class PC (OrgTec):
    def on_of(self):
        if self.power == 'ON':
            print('Сохранение данных...\nЗавершение сеанса...')
            self.power = 'OFF'
            self.net_connect = 'disconnected'
        else:
            print('Запуск ОС...\nВедите пароль')
            self.power = 'ON'

    def soft_update(self, version):
        print('Открой центр обновлений, нажми обновить, введи пароль\n'
              'Загрузка обновления...\n' 
              f'обновлено с {self.soft_version} до {version}')
        self.soft_version = version

    def go_to_print(self,text):
        with open('to_print.txt', 'w') as f:
            f.write(text)

    def net_connect(self):
        print('Подключение к локальной сети...\nПодключение к интернету...')
        self.network = 'Local and Internet'

x = PC()
x.soft_update(5.2)
x.net_connect()
x.on_of()
x.on_of()
x.go_to_print('Hello World!\nHello Python!!!')

y = Printer()
y.on_of()
y.soft_update(1.2)
y.print_some(5)
y.net_connect()
z = Skaner()
z.on_of()
z.net_connect(1.2)
z.scan()
z.soft_update(2.2)
y.print_scan(1)