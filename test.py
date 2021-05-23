import sys
import argparse



class CommandLine(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='A terminal Leetcode client',
            usage='''
leetcode
or
leetcode <command> [<args>]

The most commonly used commands are:
set     set configuration
submit  submit your code
            ''')
        parser.add_argument('command', nargs="?", help='sub command')
        args = parser.parse_args(sys.argv[1:2])
        print(args)
        # if not args.command:
        #     main_entry()
        # else:
        #     try:
        #         getattr(self, args.command)()
        #     except Exception:
        #         print('\033[91m' + f"sub-command \"{args.command}\" is not supported!\n" + '\033[0m')
        #         parser.print_help()

CommandLine()