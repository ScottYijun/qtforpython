def search(sequence, number, lower = 0, upper = None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

if __name__ == "__main__":
    seq = [34, 67, 9, 4, 200, 100, 98, 23, 65, 37, 83]
    seq.sort()
    print(seq)
    print(search(seq, 34))
    print(search(seq, 100))

   