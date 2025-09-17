#!/usr/bin/env python3

"""
Author             : Ms.ambari
contact            : ambari.developer@gmail.com
Github             : https://github.com/Ranginang67
my youtube channel : Ms.ambari

subcribe my youtube Channel to learn ethical Hacking ^_^
"""

import sys
import os

ntfile = ['.module', 'lib']

ubuntu = open('.module/jalurU.ms').read().strip()
termux = open('.module/jalurT.ms').read().strip()
termlb = open('.module/ngentot.ms').read().strip()
instal = open('.module/IN.ms').read().strip()


def _main_():
    if os.path.isdir(ubuntu):
        if os.getuid() != 0:
            print('[x] Failed: you must be root')
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print('[x] Failed: no directory module')
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print('[x] Failed: no directory lib')
            sys.exit()

        print(instal)

        # Run module files
        for f in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            os.system(f'python3 .module/files/{open(f".module/{f}.ms").read().strip()}')

        # Handle /usr/bin/lib
        if os.path.isdir('/usr/bin/lib'):
            os.system('rm -rf /usr/bin/lib')
        for script in ['.module/pindahU.ms', '.module/PindahU.ms']:
            os.system(open(script).read().strip())

        print(open('.module/DU.la').read().strip())
        print(open('.module/Du').read().strip())
        os.system('python3 .JM.xn')


    if os.path.isdir(termux):
        if not os.path.isdir(ntfile[0]):
            print('[x] Failed: no directory module')
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print('[x] Failed: no directory lib')
            sys.exit()

        print(instal)

        # Run module files
        for f in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            os.system(f'python3 .module/{open(f".module/{f}.ms").read().strip()}')

        if os.path.isdir(termlb):
            for script in ['.module/pacar.ms', '.module/pindahT.ms', '.module/PINDAHT.txt']:
                os.system(open(script).read().strip())
        else:
            for script in ['.module/pindahT.ms', '.module/PINDAHT.txt']:
                os.system(open(script).read().strip())

        print(open('.module/DU.la').read().strip())
        print(open('.module/Du').read().strip())
        os.system('python3 .JM.xn && cd')


if __name__ == '__main__':
    _main_()
