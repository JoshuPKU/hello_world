import time
import sys


class Hi(object):
    def __init__(self):
        self.say()

    def say(self):
        print('%s,hello world!' % time.ctime())
        return 0


if __name__ == '__main__':
    h = Hi()
    sys.exit()

