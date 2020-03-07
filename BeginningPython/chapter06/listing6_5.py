def story(**kwds):
    return ('Once upon a time, there was a {job} called {name}.'.format_map(kwds))

def power(x, y, *others):
    if others: #收到冗余参数
        print('Received redundant parameters:', others)
    print('power====x={}, y={}'.format(x, y))
    return pow(x, y)

def interval(start, stop = None, step = 1):
    'Imitates range() for step > 0' #这是什么意思？ 注释
    if stop is None:
        start, stop = 0, start
    result = []
    print('interval====start={}, stop={}'.format(start, stop))
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


if __name__ == "__main__":
    print(story(job = 'king', name = 'Gumby'))
    print(story(name = 'Sir Robin', job = 'brave knight'))
    params = {'job': 'language', 'name': 'Python'}
    print(story(**params))
    del params['job'] #删除job参数
    print(story(job = 'stroke of genius', **params))
    print(power(2, 3))
    print(power(3, 2))
    params = (5,) * 2
    print(params)
    print(power(*params))#一个*号表示传的是一个元组
    print(power(3, 3, 'Hello, world'))
    print(interval(10))
    print(interval(1, 5))
    print(interval(3, 12, 4))
    print(power(*interval(3, 7))) #*interval(3, 7)的值为 [3,4, 5,6] power函数执行的是3的4次方
