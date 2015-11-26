import os


# degree: number of symbols per card
# max_symbols: number of different symbols in the deck
def get_banned(cards, card):
    banned = list(card)
    for symbol in card:
        for c in cards:
            if symbol in c:
                banned += c
    return list(set(banned))


def get_number_of_occurrences(cards, symbol):
    return len([c for c in cards if symbol in c])


def get_next_possible_symbol(cards, card, degree, max_symbols):
    banned = get_banned(cards, card)
    for i in range(max_symbols):
        symbol_occurrences = get_number_of_occurrences(cards, i)
        if i not in banned and symbol_occurrences < degree:
            return i


def generate_new_card(cards, degree, max_symbols):
    # banned = [item for sublist in cards for item in sublist]
    banned = []
    joined = []
    card = []
    while len(card) < degree:
        symbol = get_next_possible_symbol(cards, card, degree, max_symbols)
        if symbol is not None:
            card.append(symbol)
        else:
            return False
    return card


def generate_deck(degree, max_symbols):
    generate = True
    cards = []
    while generate:
        card = generate_new_card(cards, degree, max_symbols)
        if card:
            cards.append(card)
        else:
            generate = False
            print("last state")
            print(cards)
    return cards

if __name__ == '__main__':
    degree = 3
    n = degree - 1
    max_symbols = n * n + n + 1
    deck = generate_deck(degree, max_symbols)
    for i, card in enumerate(deck, start=1):
        print('{:>3}: {}'.format(i, ', '.join([str(c) for c in card])))

    print('{} cards found out of {}'.format(len(deck), max_symbols))

    # print(get_banned([[1, 2, 3], [1, 4, 5], [2, 9, 8]], [1]))
