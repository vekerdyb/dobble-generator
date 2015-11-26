"""
http://math.stackexchange.com/a/36806

Assuming the following variables:

S = total number of symbols
C = total number of cards
N = number of symbols per card

The celebrated Ray-Chaudhuri–Wilson theorem states that C≤S.

An almost matching construction is as follows.

Pick some prime number n.

Our universe, of size n^2+n+1, consists of

pairs of numbers in {0,…,n−1}
n+1 singletons {0,1,…,n−1, n} ("points at infinity").

For each 0≤a≤n−1 and 0≤b≤n−1 we will have a card of size n+1 containing the pairs {(x, ax+b mod n)} and the singleton a.

There are also n special cards, for each 0≤c≤n−1, containing the pairs {(c,x)} and the singleton n.

One super special card contains all n+1 singletons.

Clearly two cards with the same aa intersect only at the singleton. Two cards with different as intersect at the unique solution to a1x+b1=a2x+b2(modn).
Two special cards intersect only at the singleton, and a normal and a special card intersect at (c,ac+b).
Finally, the super special card intersects the rest at a singleton.

In total, we have n^2+n+1 cards and symbols, each card containing n+1 symbols, and two cards intersecting at exactly one symbol.

In your case n=7 and so the number of cards and symbols should be 7^2+7+1=57.





http://math.stackexchange.com/a/930381
Let N = number of symbols per card
C = N^2 - N + 1
Generate a matrix with N columns and C rows

Column 1: Symbol 1 for N rows Symbol 2 for N-1 rows . . . Symbol N for N-1 rows
Column 2:
    Row 1 = Symbol (Column #)
    Row 2 = Symbol N+1
    Row 3 = Symbol 2N
    Row 4 = Symbol 3N-1
    Row 5 = Symbol 4N-2
    Etc. through row 2N-1
    Repeat above rows N-2 times
Column 3:
    Row 1: Symbol (Column #)
    Row 2: Previous column Row 2 plus 1
    Row 3: Previous column Row 3 plus 1
    Etc. through row 2N-1
    Repeat above rows N-2 times
Column 4:
    Same as Column 3 . . . Column N


"""

n = 3
deck = []
num_rows = n * n - n + 1
print(num_rows)
matrix = []

column1 = []
for r in range(n):
    for s in range(n-r):
        column1.append(s)

matrix.append(column1)

column2 = []
column2.append(2)
for i, m in enumerate(range(num_rows-2)):
    column2.append(m * n - (m-1))

matrix.append(column2)
# for

# for c in range(columns):

deck = matrix


for i, card in enumerate(deck, start=1):
    print('{:>3}: {}'.format(i, ', '.join([str(c) for c in card])))
