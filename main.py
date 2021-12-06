from libs import Awd
from libs import Help
from libs.OutputColor import Color
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

def error():
    print(Color('Can\'t press Ctrl+C!', 'red').print())

def logo():
    file_object = open("./logo.log")
    try:
        logo_tip = file_object.read()
    finally:
        file_object.close()
    print(Color(logo_tip, 'green').print())

def main():
    inputHistory = InMemoryHistory()
    inputCommand = WordCompleter(
        ['help',
         'exit',
         'save',
         'load',
         'clean',
         'add_attack_target',
         'scan_attack_targets',
         'show_attack_targets',
         'delete_attack_target',
         'add_attack_shell',
         'show_attack_shells',
         'delete_attack_shell',
         'operate_attack_shell',
         'show_flags',
         'submit_flags',
         'set_attack_time']
    )
    logo()
    awd = Awd.Awd()
    while True:
        try:
            inputData = prompt('[+]> ', history=inputHistory, completer=inputCommand, auto_suggest=AutoSuggestFromHistory())
            inputData = inputData.strip()
            if inputData == '':
                pass
            elif inputData == 'exit':
                break
            elif inputData == 'help':
                awd.Help.put()
            elif inputData == 'save':
                awd.Cache.save(awd.Targets, awd.WebShell)
            elif inputData == 'load':
                awd.Cache.save(awd.Targets, awd.WebShell)
            elif inputData == 'clean':
                awd.Cache.clean()
            elif inputData == 'add_attack_target':
                awd.Targets.add()
            elif inputData == 'scan_attack_targets':
                awd.Targets.scan()
            elif inputData == 'show_attack_targets':
                awd.Targets.show()
            elif inputData == 'delete_attack_target':
                awd.Targets.delete()
            elif inputData == 'add_attack_shell':
                awd.WebShell.add()
            elif inputData == 'show_attack_shells':
                awd.WebShell.show()
            elif inputData == 'delete_attack_shell':
                awd.WebShell.delete()
            elif inputData == 'operate_attack_shell':
                pass
            elif inputData == 'show_flags':
                pass
            elif inputData == 'submit_flags':
                pass
            elif inputData == 'set_attack_time':
                pass
            else:
                print(Color('Can\'t find the corresponding operation! please input again!', 'red').print())

        except KeyboardInterrupt:
            error()

if __name__ == '__main__':
    main()