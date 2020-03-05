name = ''
while not name.strip():
    name = input('Please enter your name: ')
    print('Hello, {}!'.format(name))