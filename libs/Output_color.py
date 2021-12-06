class Color:

    def __init__(self, output, color, highlight=True, underscore=False, blink=False, backgroundcolor=None):
        self.color = color
        self.blink = blink
        self.output = output
        self.highlight = highlight
        self.underscore = underscore
        self.backgroundcolor = backgroundcolor

    def font(self):
        if self.color == 'black':
            return '30'
        elif self.color == 'red':
            return '31'
        elif self.color == 'green':
            return '32'
        elif self.color == 'yellow':
            return '33'
        elif self.color == 'blue':
            return '34'
        elif self.color == 'fuchsia':
            return '35'
        elif self.color == 'cyan':
            return '36'
        elif self.color == 'white':
            return '37'

    def background(self):
        if self.backgroundcolor == 'black':
            return '40m'
        elif self.backgroundcolor == 'red':
            return '41m'
        elif self.backgroundcolor == 'green':
            return '42m'
        elif self.backgroundcolor == 'yellow':
            return '43m'
        elif self.backgroundcolor == 'blue':
            return '44m'
        elif self.backgroundcolor == 'fuchsia':
            return '45m'
        elif self.backgroundcolor == 'cyan':
            return '46m'
        elif self.backgroundcolor == 'white':
            return '47m'

    def print(self):
        # \ 033 [显示方式;字体色;背景色m ...... [\ 033 [0m]
        data = '\033['
        try:
            if self.highlight:
                data += '1;'
            if self.blink:
                data += '5;'
            if self.underscore:
                data += '4;'
            if self.backgroundcolor:
                data += self.font()
                data += ';'
                data += self.background()
            elif self.backgroundcolor == None:
                data += self.font()
                data += 'm'
            data = data + self.output + '\033[0m'
            return data
        except Exception:
            return 'error!'