import json
from libs.OutputColor import Color

class Config:
    """配置属性模块"""

    proxy = {}
    # flag{[0-9a-fA-F]{32}}
    # flag{[0-9a-f-]{36}}
    # [0-9a-zA-Z]{32}
    flag_format = None
    shellBase64Encode = True

    @staticmethod
    def config():
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                json_data = ''
                for con in f.readlines():
                    if con.strip() and '//' != con.strip()[:2]:
                        json_data += con
                data = json.loads(json_data)

                Config.proxy = data['proxy']
                Config.flag_format = r'{}'.format(data['flag_format']) if data['flag_format'] else None
                Config.shellBase64Encode = data['shellBase64Encode']
        except Exception as e:
            errorMessage = 'Config error! {}'.format(e)
            print(Color(errorMessage, 'red').print())