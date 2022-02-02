from scripts import config

LAB_DIR = '../Final-Lab_3'
SOL_PATH = 'solutions/lab3_sol'
CONFIG_DICT = {
    'rit.stu.Mint': {
        'test_input.txt': '',
    }
}


def main():
    config.execute(LAB_DIR, SOL_PATH, CONFIG_DICT)


if __name__ == '__main__':
    main()