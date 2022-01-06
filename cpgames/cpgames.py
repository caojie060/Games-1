'''
Function:
    Python小游戏合集
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import sys
import warnings
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    from modules import *
    from __init__ import __version__
else:
    from .modules import *
    from .__init__ import __version__
warnings.filterwarnings('ignore')


'''basic info'''
BASICINFO = '''************************************************************
Function: Python小游戏合集 V%s
Author: Charles
微信公众号: Charles的皮卡丘
************************************************************''' % (__version__)


'''Python实用工具集'''
class CPGames():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): setattr(self, key, value)
        self.supported_games = self.initialize()
    '''执行对应的小程序'''
    def execute(self, game_type=None, config={}):
        assert game_type in self.supported_games, 'unsupport game_type %s...' % game_type
        qt_games = []
        if game_type in qt_games:
            app = QApplication(sys.argv)
            client = self.supported_games[game_type](**config)
            client.show()
            sys.exit(app.exec_())
        else:
            client = self.supported_games[game_type](**config)
            client.run()
    '''初始化'''
    def initialize(self):
        supported_games = {
            'bunnybadger': BunnyBadgerGame,
            'voicecontrolpikachu': VoiceControlPikachuGame,
        }
        return supported_games
    '''获得所有支持的游戏信息'''
    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_games.items():
            all_supports[value.game_type] = key
        return all_supports
    '''repr'''
    def __repr__(self):
        return BASICINFO


'''run'''
if __name__ == '__main__':
    import random
    games_client = CPGames()
    all_supports = games_client.getallsupported()
    games_client.execute(random.choice(list(all_supports.values())))