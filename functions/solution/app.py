""" opentracing and functions """

import logging
from random import randint
from time import sleep
from jaeger_client import Config

logging.getLogger('').handlers = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': '1',
        },
        'logging': True,
        'metrics': True,
    },
    service_name='pythonFunc',

)

tracer = config.initialize_tracer()

def function1():
    """function1"""
    span = tracer.start_span('function1')
    try:
        logging.info("function1")
        span.set_baggage_item("token", "token")


        delay = randint(25, 50)
        span.log_event("delay", delay)
        sleep(delay / 1000.0)
        function2(span)

    finally:
        span.finish()

def function2(parent_span):
    """function2"""
    span = tracer.start_span('function2', child_of=parent_span)
    try:
        logging.info("function2")
        token = span.get_baggage_item("token")
        logging.info("token=%s", token)

        delay = randint(25, 50)
        span.log_event("delay", delay)
        sleep(delay / 1000.0)
    finally:
        span.finish()

def main():
    """main function"""
    function1()

if __name__ == '__main__':
    main()
    logging.info("giving tracer time to report")
    sleep(2)
    tracer.close()
