# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input
# will be a non-negative integer.

def digital_root(n):
    # res = 0
    # for i in str(n):
    #     res += int(i)
    # if res > 9:
    #     res = digital_root(res)
    #     print(n)
    # return res

    # Clever code
    return n if n < 10 else digital_root(sum(map(int, str(n))))

n = int(16589)
res = digital_root(n)
print(res)
