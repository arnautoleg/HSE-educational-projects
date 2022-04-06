import math


def find_percentile(a, b, p):

    total_lenght = len(a) + len(b)
    half = (total_lenght * p) // 100

    if len(b) < len(a):
        a, b = b, a

    l, r = 0, len(a) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = a[i] if i >= 0 else float("-infinity")
        Aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
        Bleft = b[j] if j >= 0 else float("-infinity")
        Bright = b[j + 1] if (j + 1) < len(b) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total_lenght % 2:
                return min(Aright, Bright)
            return min(max(Aleft, Bleft), min(Aright, Bright))
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
