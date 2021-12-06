import re
import os
import pickle
from libs.Tips import Remove
from libs.OutputColor import Color

class Targets:
    """目标功能模块"""

    # User-Agent
    # header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Connection':'close'}

    def __init__(self):
        self.targets = []

    @staticmethod
    def check_input(target):
        if ":" in target:
            try:
                ip = target.split(":")[0]
                port = int(target.split(":")[1])
            except Exception:
                return False
        else:
            ip = target
            port = 80
        if (port < 0 or port > 65536):
            return False
        # 匹配IP正则: ^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$
        if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', ip):
            return False
        return ip, str(port)

    def add(self):
        print(Color('eg. 127.0.0.1 == 127.0.0.1:80', 'yellow').print())
        print(Color('eg. 127.0.0.1:8888 == 127.0.0.1:8888', 'yellow').print())
        print(Color('Please input exit to end adding.', 'yellow').print())

        while True:
            target = input('[+] add_target_ip> ').strip()
            if target == 'exit':
                break
            if not self.check_input(target):
                print(Color('IP Format Error!', 'red').print())
            else:
                ip, port = self.check_input(target)
                target = {'ip' : ip, 'port' : port}
                self.targets.append(target)
                print(Color('Successfully Add Target!', 'blue').print())
            self.targets = Remove(self.targets).list_remove_repeat()
        print(Color('Now Total targets: {}\n'.format(len(self.targets)), 'blue').print())

    def scan(self):
        # selfIP = input('Please input yourself ip\n> ')
        # if not self.check_input(selfIP):
        #     print(Color('IP Format Error!', 'red').print())
        # print('The module has not yet been developed!')
        print(Color('The module has not yet been developed!', 'red').print())


    def show(self):
        if len(self.targets) == 0:
            print(Color('No data added yet!', 'red').print())
        else:
            for target in self.targets:
                target = target['ip'] + ':' + target['port']
                print(Color(target, 'fuchsia').print())
            print(Color('Now Total targets: {}\n'.format(len(self.targets)), 'blue').print())

    def delete(self):
        self.show()
        print(Color('Please select the ipIndex(1~n) to be deleted.\nIf you want to delete all targets, please input all.\nIf you want to end deleting, please input exit.\n', 'yellow').print())

        while True:
            delIPIndex = input('> ')
            if delIPIndex == 'exit':
                break
            elif delIPIndex == 'all':
                self.targets.clear()
            else:
                del self.targets[int(delIPIndex) - 1]
        print(Color('Now Total targets: {}\n'.format(len(self.targets)), 'blue').print())


class WebShell:
    """WebShell功能模块"""

    def __init__(self):
        self.webshells = []
        self.Targets = Targets()

    @staticmethod
    def upload_horse(type):



    @staticmethod
    def handle_webshell(input_webshell):
        tempList = []
        for shell in input_webshell.split(' '):
            if shell != '':
                tempList.append(shell)
        if len(tempList) != 4:
            print(Color('Input WebShell is error, please input again!', 'red').print())
        webshell = {
            "WebShell_path" : tempList[0],
            "WebShell_passwd" : tempList[1],
            "WebShell_Request" : tempList[2].upper(),
            "WebShell_type" : tempList[3].lower()
        }
        if webshell['WebShell_Request'] not in ['GET', 'POST', 'REQUEST', 'GLOBAL']:
            print(Color('Input WebShell_Request is error, please input again!', 'red').print())
        if webshell['WebShell_type'] not in ['eval', 'assert', 'system', 'popen', 'exec', 'shell exec', 'passthru', 'readfile', 'include', 'require', 'file_get_contents']:
            print(Color('Input WebShell_type is error, please input again!', 'red').print())
        return webshell

    def add(self):
        print(Color('eg. [WebShell_path] [WebShell_passwd] [WebShell_Request] [WebShell_type]', 'yellow').print())
        print(Color('eg. WebShell_path: /var/www/html/.lndex.php...', 'yellow').print())
        print(Color('eg. WebShell_passwd: h3rmesk1t...', 'yellow').print())
        print(Color('eg. WebShell_Request: GET, POST, REQUEST, GLOBAL...', 'yellow').print())
        print(Color('eg. WebShell_type: eval, assert, system, popen, exec, shell exec, passthru, readfile, include, require, file_get_contents...', 'yellow').print())

        webshell = input('[+] add_webshell> ').strip()
        if self.handle_webshell(webshell):
            self.webshells.append(webshell)
            self.webshells = Remove(self.webshells).list_remove_repeat()
            print(Color('Successfully Add WebShell!', 'blue').print())

    def show(self):
        if len(self.webshells) == 0:
            print(Color('No data added yet!', 'red').print())
        for i in range(len(self.webshells)):
            print(Color('[' + str(i+1) + '] ' + str(self.webshells[i]), 'fuchsia').print())

        print(Color('Now Total WebShells: {}\n'.format(len(self.webshells)), 'blue').print())

    def delete(self):
        self.show()
        print(Color('Please select the WebShellIndex(1~n) to be deleted.\nIf you want to delete all WebShells, please input all.\nIf you want to end deleting, please input exit.\n','yellow').print())

        while True:
            WebShellIndex = input('> ')
            if WebShellIndex == 'exit':
                break
            elif WebShellIndex == 'all':
                self.webshells.clear()
            else:
                del self.webshells[int(WebShellIndex) - 1]
        print(Color('Now Total WebShells: {}\n'.format(len(self.webshells)), 'blue').print())

    def operate(self):
        uploadHorse = False
        if len(self.Targets.targets) == 0:
            print(Color('No target_ip data added yet!\nPlease use \'add_attack_target\' to add target_ip.', 'red').print())
        if len(self.webshells) == 0:
            print(Color('No WebShell data added yet!\nPlease use \'add_attack_shell\' to add WebShell.', 'red').print())
        shellIndex = 0
        if len(self.webshells) > 1:
            self.show()
            print(Color('Please choose a WebShell to do command. Input exit to end operate.', 'yellow').print())
            while True:
                try:
                    shellIndex = input('[+] WebShellIndex> ')
                    if shellIndex == 'exit':
                        break
                    shellIndex = int(shellIndex) - 1
                    if shellIndex not in range(len(self.webshells)):
                        raise Exception()
                    else:
                        break
                except:
                    print(Color('Please input WebShellIndex(1~n)', 'red').print())
        print(Color('If you want to upload WebShell-Horse, please input \'yes\'\n', 'yellow').print())
        if input('> ').strip().lower() == 'yes':
            uploadHorse = True

        webshell_type = self.webshells[shellIndex]['type']

        if uploadHorse:
            self.upload_horse(webshell_type)



class Cache:
    """数据存储功能模块"""

    flag_dat = r'cache/flag.dat'
    flag_txt = r'cache/flag.txt'
    targets_dat = r'cache/target_ip.dat'
    targets_txt = r'cache/target_ip.txt'
    webshell_dat = r'cache/webshell.dat'
    webshell_txt = r'cache/webshell.txt'

    def __init__(self):
        if not os.path.exists('cache'):
            os.mkdir('cache')

    def save(self, target, webshell):
        if len(target.targets) == 0:
            print(Color('No target_ip data added yet!', 'red').print())
        if len(webshell.webshells) == 0:
            print(Color('No webshell data added yet!', 'red').print())

        try:
            with open(self.targets_dat, 'wb') as f:
                pickle.dump(target.targets, f)
            with open(self.targets_txt, 'wb') as f:
                pickle.dump(target.targets, f)
            with open(self.webshell_dat, 'wb') as f:
                pickle.dump(webshell.webshells, f)
            with open(self.webshell_txt, 'wb') as f:
                pickle.dump(webshell.webshells, f)
        except Exception as e:
            print(Color(e, 'red').print())

    def load(self, target, webshell):
        if not os.path.exists(self.targets_dat):
            print(Color('Load target_ip data failed, please save data first!', 'red').print())
        if not os.path.exists(self.webshell_dat):
            print(Color('Load webshell data failed, please save data first!', 'red').print())

        try:
            """加载存储的目标IP"""
            if os.path.exists(self.targets_dat):
                with open(self.targets_dat, 'rb') as f:
                    target_cache = pickle.load(f)
                target.targets.extend(target_cache)
                target.targets = Remove(target.targets).list_remove_repeat()
            """加载存储的WebShell"""
            if os.path.exists(self.webshell_dat):
                with open(self.webshell_dat, 'rb') as f:
                    shell_cache = pickle.load(f)
                webshell.webshells.extend(shell_cache)
                webshell.webshells = Remove(webshell.webshells).list_remove_repeat()
            """加载存储的FLAG"""
            print(Color('Load successfully!', 'blue').print())
        except Exception as e:
            print(Color(e, 'red').print())

    def clean(self):
        if not os.path.exists(self.targets_dat):
            print(Color('No target_ip data added yet!', 'red').print())
        if not os.path.exists(self.webshell_dat):
            print(Color('No webshell data added yet!', 'red').print())

        try:
            if os.path.exists(self.targets_dat):
                os.remove(self.targets_dat)
            if os.path.exists(self.webshell_dat):
                os.remove(self.webshell_dat)
            if os.path.exists(self.flag_dat):
                os.remove(self.flag_dat)
            print(Color('Clean successfully!', 'blue').print())
        except Exception as e:
            print(Color(e, 'red').print())