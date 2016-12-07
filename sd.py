import sys
import argparse
import pyperclip
from msw import measure_sentence_width


def generator(reactant):
    left_top = '＿人'
    right_top = '人＿'
    left = '＞　'
    right = '　＜'
    left_bottom = '￣Y^'
    right_bottom = 'Y￣'

    multi_byte_width = measure_sentence_width(reactant) // 2

    content = left_top + ''.join(['人' for _ in range(multi_byte_width)]) + right_top + '\n'

    content += left + reactant + right + '\n'

    content += left_bottom + ''.join(['Y^' for _ in range(multi_byte_width)]) + right_bottom

    return content


def parse(args):
    parser = argparse.ArgumentParser('sudden-death generator')
    parser.add_argument('sentence', nargs='*',
                        help='')
    parser.add_argument('-c', '--copy', action='store_true', default=False,
                        help='Copy the generated string to clipboard.')
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help='Quiet mode')

    args = parser.parse_args(args)
    if args.sentence:
        args.sentence = ' '.join(args.sentence)
    else:
        args.sentence = ''

    return args


def main():

    args = sys.argv[1:]

    parsed = parse(args)

    while not parsed.sentence:
        parsed.sentence = input('Please input some sentence:')

    content = generator(parsed.sentence)

    if parsed.copy:
        pyperclip.copy(content)

    if not parsed.quiet:
        print(content)


if __name__ == '__main__':
    main()
