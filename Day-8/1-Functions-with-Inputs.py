## Simple function
def greet():
    print('hello')
    print('how do you do')
    print('ask me somn\n')
greet()

## Functions with inputs
def greet(name):
    print(f'hello {name}')
    print(f'how do you do {name}')
    print(f'i come from {name}')
greet('psycho')

## Positional arguements
def greet(name,place):
    print(f'hello {name}')
    print(f'how do you do {name}')
    print(f'i come from {place}')
greet('psycho', 'lusaka')

## Keyword arguements
def greet(name,place):
    print(f'hello {name}')
    print(f'how do you do {name}')
    print(f'i come from {place}')
greet(name='psycho', place='lusaka')