""" opentracing and functions """

import logging
from random import randint
from time import sleep

logging.getLogger('').handlers = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# configure opentracing

def function1():
    """function1"""
    logging.info("function1")

    delay = randint(25, 50)
    sleep(delay / 1000.0)
    function2()

def function2():
    """function2"""

    logging.info("function2")

    delay = randint(25, 50)
    sleep(delay / 1000.0)

def main():
    """main function"""
    function1()

if __name__ == '__main__':
    main()
