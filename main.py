from libs import Awd
from libs import Print_help
from libs import Output_color
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

def error():
    output = Output_color.Color('Can\'t press Ctrl+C!', 'red').print()
    print(output)

def main():
    inputHistory = InMemoryHistory()
    inputCommand = WordCompleter(
        ['help',
         'exit',
         'save',
         'load',
         'clean',
         'add_attack_target',
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

    awd = Awd.Awd()
    help = Print_help.help()

    while True:
        try:
            inputData = prompt('[+]> ', history=inputHistory, completer=inputCommand, auto_suggest=AutoSuggestFromHistory())
            inputData = inputData.strip()
            if inputData == '':
                pass
            elif inputData == 'exit':
                break
            elif inputData == 'help':
                help.put()
            elif inputData == 'save':
                pass
            elif inputData == 'load':
                pass
            elif inputData == 'clean':
                pass
            elif inputData == 'add_attack_target':
                awd.add_attack_target()
            elif inputData == 'show_attack_targets':
                pass
            elif inputData == 'delete_attack_target':
                pass
            elif inputData == 'add_attack_shell':
                pass
            elif inputData == 'show_attack_shells':
                pass
            elif inputData == 'delete_attack_shell':
                pass
            elif inputData == 'operate_attack_shell':
                pass
            elif inputData == 'show_flags':
                pass
            elif inputData == 'submit_flags':
                pass
            elif inputData == 'set_attack_time':
                pass
            else:
                output = Output_color.Color('Can\'t find the corresponding operation! please input again!', 'red').print()
                print(output)

        except KeyboardInterrupt:
            error()

if __name__ == '__main__':
    main()