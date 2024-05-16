import sys
import os
import time

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('a.txt')

print(path)
print(os.path.dirname(__file__))
print('------------------')

for i in range(5, 10):
    print("this is the %d times" % i)
    time.sleep(2)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))