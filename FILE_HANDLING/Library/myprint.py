
SCREEN_WIDTH = 100


def printcenter(s):
    xpos = SCREEN_WIDTH//2
    print((" "*xpos), s)


def printbar():
    print("="*100)


def printbarln():
    printbar()
    print()


def inputcenter(s):
    xpos = SCREEN_WIDTH // 2
    print((" " * xpos), s, end='')
    return input()