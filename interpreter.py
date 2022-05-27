from linecache import getline
import sys

def interpret(program, args):
    l = [0 for i in range (10)]
    prog_index = 0
    buff_index = 0
    args_index = 0
    loop_index = 0
    while program[prog_index] != '@':
        if program[prog_index] == '#': print("\ncell at index ", buff_index, "is ", l[buff_index])
        if program[prog_index] == '+': l[buff_index] += 1
        if program[prog_index] == '-':
            if l[buff_index] > 0: l[buff_index] -= 1
        if program[prog_index] == '>': buff_index += 1
        if program[prog_index] == '<': buff_index -= 1
        if program[prog_index] == '[': loop_index = prog_index
        if program[prog_index] == ']':
            if l[buff_index] == 0:
                pass
            else:
                prog_index = loop_index
        if program[prog_index] == ',':
            try :
                args[args_index]
                l[buff_index] = ord(args[args_index])
                args_index += 1
            except IndexError:
                args_index = 0
                try :
                    args = input() + '\n'
                except KeyboardInterrupt:
                    return 0
                except EOFError:
                    return 0
                l[buff_index] = ord(args[args_index])
                args_index += 1
        if program[prog_index] == '.':
            print(chr(l[buff_index]), end='')
        prog_index += 1

program = open(sys.argv[1], 'r').read()
try:
    args = sys.argv[2]
    interpret(program, args)
except IndexError:
    interpret(program, [])


