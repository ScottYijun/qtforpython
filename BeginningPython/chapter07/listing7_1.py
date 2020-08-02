def add(x, y):
    return (x+y)

def length_message(x):
    print("The length of", repr(x), "is", len(x))

if __name__ == "__main__":
    print("add(5, 8)=", add(5, 8))
    print("add(25, 38)=", add(25, 38))

    length_message('Fnord')
    length_message([1, 2, 3])