
SCREEN_WIDTH = 100


def print_center(s):
    xpos = SCREEN_WIDTH//2
    print((" "*xpos), s)


def print_bar():
    print("="*100)


def print_bar_ln():
    print_bar()
    print()


def input_center(s):
    xpos = SCREEN_WIDTH // 2
    print((" " * xpos), s, end='')
    return input()