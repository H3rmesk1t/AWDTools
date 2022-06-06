from libs import OutputColor

class Help:

    def __init__(self):
        self.put()

    @staticmethod
    def put():
        output = OutputColor.Color
        print(output('Usage: Command\n', 'green').print())
        print(output(output='   help', color='cyan').print().ljust(40, ' '), output(output='Display all functions.', color='white').print())
        print(output(output='   exit', color='cyan').print().ljust(40, ' '), output(output='Exit the program.', color='white').print())
        print(output(output='   save', color='cyan').print().ljust(40, ' '), output(output='Save attack_targets and attack_webshell to file.', color='white').print())
        print(output(output='   load', color='cyan').print().ljust(40, ' '), output(output='Load attack_targets and attack_webshell from file.', color='white').print())
        print(output(output='   clean', color='cyan').print().ljust(40, ' '), output(output='Clean the data of the saved file.', color='white').print())
        print(output(output='   add_attack_target', color='cyan').print().ljust(40, ' '), output(output='Add attack_target.', color='white').print())
        print(output(output='   scan_attack_targets', color='cyan').print().ljust(40, ' '), output(output='scan attack_targets.', color='white').print())
        print(output(output='   show_attack_targets', color='cyan').print().ljust(40, ' '), output(output='Show all attack_targets.', color='white').print())
        print(output(output='   delete_attack_target', color='cyan').print().ljust(40, ' '), output(output='Delete the attack_target.', color='white').print())
        print(output(output='   add_attack_shell', color='cyan').print().ljust(40, ' '), output(output='Add attack_shell.', color='white').print())
        print(output(output='   show_attack_shells', color='cyan').print().ljust(40, ' '), output(output='Show all attack_shells.', color='white').print())
        print(output(output='   delete_attack_shell', color='cyan').print().ljust(40, ' '), output(output='Delete the attack_shell.', color='white').print())
        print(output(output='   operate_attack_shell', color='cyan').print().ljust(40, ' '), output(output='Operate the attack_shell.', color='white').print())
        print(output(output='   show_flags', color='cyan').print().ljust(40, ' '), output(output='Show flags.', color='white').print())
        print(output(output='   submit_flags', color='cyan').print().ljust(40, ' '), output(output='Submit flags.', color='white').print())
        print(output(output='   set_attack_time', color='cyan').print().ljust(40, ' '), output(output='Set attack_time.', color='white').print())
        print(output(output='   scan_port_by_ip', color='cyan').print().ljust(40, ' '), output(output='scan address\'s ports.\n', color='white').print())