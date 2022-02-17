from scripts import config

LAB_DIR = '../Final-Lab_4'
SOL_PATH = 'solutions/lab4_sol'
CONFIG_DICT = {
    'toyland.ToyLand': [
        'actionfigure-1.txt',
        'actionfigure-5.txt',
        'all.txt',
        'doll-1.txt',
        'doll-5.txt',
        'playdough-1.txt',
        'playdough-5.txt',
        'rccar-1.txt',
        'rccar-5.txt',
        'robot-1.txt',
        'robot-5.txt'
    ]
}


def main():
    config.execute(LAB_DIR, SOL_PATH, CONFIG_DICT)


if __name__ == '__main__':
    main()