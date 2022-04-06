def largest_palindrome(s):
    pass
    maximal, start, low, high = 1, 0, 0, 0
    length = len(s)
    for i in range(1, length):
        low, high = i - 1, i
        while low >= 0 and high < length and s[low] == s[high]:
            low, high = low - 1, high + 1
        low, high = low + 1, high - 1
        if s[low] == s[high] and high - low + 1 > maximal:
            start = low
            maximal = high - low + 1
        low, high = i - 1, i + 1
        while low >= 0 and high < length and s[low] == s[high]:
            low, high = low - 1, high + 1
        low, high = low + 1, high - 1
        if s[low] == s[high] and high - low + 1 > maximal:
            start = low
            maximal = high - low + 1
    return s[start:start + maximal]

# some test code
if __name__ == "__main__":
    test_s = 'ABBCB'
    # should print BCB
    print(largest_palindrome(test_s))

    test_s = 'ABACABAD'
    # should print ABACABA
    print(largest_palindrome(test_s))

    test_s = 'ABCDE'
    # should print A
    print(largest_palindrome(test_s))

