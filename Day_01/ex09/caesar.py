from cgitb import reset
import sys

def check_symbols(text):
    try:
        text.encode('ascii')
    except:
        raise Exception('The script does not support your language yet')

def check_args(argv):
    if len(sys.argv) == 4:
        check_symbols(argv[2])
        caesar_cipher(argv)
    else:
        raise Exception('Wrong arguments. Usage: command(encode/decode), \'text\', shift(number)')

def caesar_cipher(argv):
    if argv[1] == 'decode':
        shift = -int(argv[3])
    elif argv[1] == 'encode':
        shift = int(argv[3])
    else:
        raise Exception('Wrong command. Usage: command(encode/decode), \'text\', shift(number)')
    abc = list('abcdefghijklmnopqrstuvwxyz')
    ABC = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = ''
    for c in argv[2]:
        if c in abc:
            result += abc[(abc.index(c) + shift) % 26]
        elif c in ABC:
            result += ABC[(ABC.index(c) + shift) % 26]
        else:
            result += c
    print(result)



if __name__ == '__main__':
    try:
        check_args(sys.argv)
    except Exception as e:
        print(e, file=sys.stderr)

# $ python3 caesar.py encode 'ssh -i private.key user@school21.ru' 12
# eet -u bduhmfq.wqk geqd@eotaax21.dg
# $ python3 caesar.py decode 'eet -u bduhmfq.wqk geqd@eotaax21.dg' 12
# ssh -i private.key user@school21.ru