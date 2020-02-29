# 检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User name:')
pin = input('PIN code: ')

if[username, pin] in database:
    print('Access granted')
    