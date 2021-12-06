from libs.Help import Help
from libs.Model import Cache
from libs.Model import Targets
from libs.Model import WebShell

class Awd:

    def __init__(self):
        self.Targets = Targets()
        self.WebShell = WebShell()
        self.Cache = Cache()
        self.Help = Help()

