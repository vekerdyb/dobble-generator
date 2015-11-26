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





http://math.stackexchange.com/a/1314362

// N*N first cards
for I = 0 to N-1
   for J = 0 to N-1
      for K = 0 to N-1
         print ((I*K + J) modulus N)*N + K
      end for
      print N*N + I
      new line
   end for
end for

// N following cards
for I = 0 to N-1
   for J = 0 to N-1
      print J*N + I
   end for
   print N*N + N
   new line
end for

// Last card
for I = 0 to N-1
   print N*N + I
end for
new line


"""


def get_maximum_deck_size_for_degree(degree):
    n = degree - 1
    return n * n + n + 1


def generate_deck(degree):
    n = degree - 1
    deck = []

    # N*N first cards
    for i in range(n):
        for j in range(n):
            card = []
            for k in range(n):
                card.append(((i * k + j) % n) * n + k)
            card.append(n * n + i)
            deck.append(card)

    # N following cards
    for i in range(n):
        card = []
        for j in range(n):
            card.append(j * n + i)
        card.append(n * n + n)
        deck.append(card)

    # Last card
    card = []
    for i in range(n + 1):
        card.append(n * n + i)
    deck.append(card)

    return tuple([tuple(card) for card in deck])


def pretty_print_deck(deck):
    for i, card in enumerate(deck, start=1):
        print('{:>3}: {}'.format(i, ', '.join([str(c) for c in card])))
