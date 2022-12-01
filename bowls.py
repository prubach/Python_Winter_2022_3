#    * * * * * *
#     * * * * *
#      * * * *
#       * * *
#        * *
#         *


# how many bowls do we have altogether given number of rows (n)

def sum_bowls_loop(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_bowls_loop_while(rows):
    i = 1
    bowls = 0
    while i < rows:
        bowls += i
        i += 1
        if i == rows:
            bowls += i
            return bowls


def sum_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        s = n + sum_bowls_recursive(n - 1)
        return s


def sum_bowls_seq(n):
    return int(n*(n+1)/2)

# print(sum_bowls_recursive(n))
if __name__ == '__main__':
    n = 998
    print('Sum bowls using for loop for n={}: {}'.format(n, sum_bowls_loop(n)))
    print('Sum bowls using while loop for n={}: {}'.format(n, sum_bowls_loop_while(n)))
    print('Sum bowls using recursion for n={}: {}'.format(n, sum_bowls_recursive(n)))
    print('Sum bowls using sequence for n={}: {}'.format(n, sum_bowls_seq(n)))
