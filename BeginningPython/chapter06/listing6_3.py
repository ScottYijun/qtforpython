def store(patient='Mr.Brainsample', hour = 10, minute = 20, day = 13, month = 5):
    print('{}::{}-{}:{}:{}'.format(patient, month, day, hour, minute))

def hello_3(greeting = 'Hello', name = 'world'):
    print('{}, {}'.format(greeting, name))

if __name__ == "__main__":
    print("====================")
    store('Mr. Brainsample', 10, 20, 13, 5)
    hello_3()
    hello_3('Greetings')
    hello_3('Greetings', 'universe')
    hello_3(name = 'Gumby')

