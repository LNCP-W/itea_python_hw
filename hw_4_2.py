# класс оргтехники
from abc import ABC, abstractmethod

class OrgTec(ABC):

    def __init__(self, power = 'OFF', soft_version = '1.0', network = 'disconnected'):
        self.power=power
        self.soft_version=soft_version
        self.network=network
    
    @abstractmethod
    def OnOf():
        pass

    @abstractmethod
    def soft_update():
        pass

    @abstractmethod
    def net_connect():
        pass




class Printer (OrgTec):

    def OnOf(self):
        if self.power == 'ON':
            print('Извлечение бумаги\nПарковка каретки')
            self.power='OFF'
            self.net_connect = 'disconnected'
        else:
            print('Проверка бумаги...\nпроверка чернил...\nпрочистка головки...')
            self.power='ON'

    def soft_update(self, version):
        print('Вставте флешку и одновременно нажмите кнопу питания и печати\n'
              'Загрузка обновления...\n'
              f'обновлено с {self.soft_version} до {version}')
        self.soft_version=version

    def net_connect():
        print('Подключи сетевой шнур\n Подключение к локальной сети...')
        self.network='Local'

    def print_some():

class Skaner (OrgTec):

    def OnOf(self):
        if self.power == 'ON':
            print('Паркрвка датчика')
            self.power='OFF'
        else:
            print('Проверка наличия документа...\n')
            self.power='ON'

    def soft_update(self, version):
        print('Подключись к компютеру и в сервисном приложении нажми "Обновить"\n'
              'Загрузка обновления...\n'
              f'обновлено с {self.soft_version} до {version}')
        self.soft_version=version
    def net_connect():
        print('Невозможно подключить к сети, только к компютеру')





class PC (OrgTec):
    def OnOf(self):
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
        self.soft_version=version

    def net_connect():
        print('Подключение к локальной сети...\nПодключение к интернету...')
        self.network='Local and Internet'
x=PC()
x.soft_update(5.2)
x.soft_update(6.8)
