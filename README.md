# Velocity 2017: Python AppTracing Exercise

To fetch the source:

`git clone git@github.com/bryanl/apptracing-py`

## Getting started

1. Create docker environment: `docker-compose up -d`
1. Create database: `make create-db`
1. Import test data: `make import-people`
1. Install python dependencies: `pip install -r requirements.txt`

Exercises:

* [Tracing Functions](functions)
* [Exploring a bigger app](app)

## Initializing Jaeger in Python

```python
from jaeger_client import Config

config = Config(
    config={ # usually read from some yaml config
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name='service',
)
tracer = config.initialize_tracer()
```