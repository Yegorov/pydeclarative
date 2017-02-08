PyDeclarative
=============

Declarative style in Python.

## Install

```
git clone git@github.com:Yegorov/pydeclarative.git
cd pydeclarative
py 3.5 setup.py install
```

## Use

```python
from pydeclarative import for_

for_(0, lambda i: i < 10, lambda i: i + 1, 
    lambda i, arg: print('Hello {} #'.format(arg), i), 'world!'
)

# Output:
"""
Hello world! # 0
Hello world! # 1
Hello world! # 2
Hello world! # 3
Hello world! # 4
Hello world! # 5
Hello world! # 6
Hello world! # 7
Hello world! # 8
Hello world! # 9
"""
```

## API

```
def body_loop_function(current_value, *args_to_body_function, *kwargs_to_body_function):
    pass

for_(start_value, termination, increment, body_loop_function, *args_to_body_function, *kwargs_to_body_function)
```

## Test

* Install `pytest`
* Run tests: `$ pytest tests/`

## Contributing

Feel free to send pull requests or write issue.