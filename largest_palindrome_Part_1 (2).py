def largest_palindrome(s):
    pass
    largest = ''
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(largest) >= j-i:
                break
            elif s[i:j] == s[i:j][::-1]:
                largest = s[i:j]
                break
    return largest

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

