from client import quiz, auth

# a = auth.Auth()
from helper.config import config






import sys
import argparse
from collections import OrderedDict
from helper.config import LANG_MAPPING, config

# from client.process import Process


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
        if not args.command:
            # main_entry()
            print('please enter arguments')
        else:
            # try:
            #     print(args)
            #     getattr(self, args.command)()
            # except Exception:
            #     print('\033[91m' + f"sub-command \"{args.command}\" is not supported!\n" + '\033[0m')
            #     parser.print_help()
            print(args)
            getattr(self, args.command)()
    def set(self):
        print('hello from set')
        parser = argparse.ArgumentParser(description='set configuration')
        parser.add_argument('-l', '--language', action='store', choices=LANG_MAPPING.keys(),
                            help='set programming language')
        parser.add_argument('-p', '--path', action='store', help='set programming file location')
        parser.add_argument('-e', '--ext', action='store', help='set programming file extention')
        args = parser.parse_args(sys.argv[2:])
        print(args)
        if args.language:
            config.write('language', args.language)
        elif args.ext:
            config.write('ext', args.ext)
        elif args.path:
            config.write('path', args.path)

    def submit(self):
        try:
            parser = argparse.ArgumentParser(
                description='submit your code for online judge',
                usage='leetcode submit --id [problem id]')
            parser.add_argument('--id', type=int, required=True, help='set problem id')
            args = parser.parse_args(sys.argv[2:])
            if args.id:
                process = Process()
                success, result = process.submit(args.id)
                if success:
                    self._prettify(result)
        except Exception as e:
            print(e)

    def _prettify(self, result: OrderedDict):
        for k, v in result.items():
            print(f"{k}:\t{v}")


CommandLine()
