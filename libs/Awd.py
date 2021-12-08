from libs.Help import Help
from libs.Models import Flag, Cache, Targets, WebShell

class Awd:

    def __init__(self):
        self.Help = Help()
        self.Flag = Flag()
        self.Cache = Cache()
        self.Targets = Targets()
        self.WebShell = WebShell()