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


def generate_new_card(cards, degree, max_symbols):
    # banned = [item for sublist in cards for item in sublist]
    banned = []
    joined = []
    card = []
    first_symbol = 0
    while len(card) < degree:
        for symbol in range(max_symbols):
            if symbol not in banned:
                card.append(symbol)
                banned = get_banned(cards, card)
                break
            else:
                print('symbol {} banned for card {} with cards {}'.format(symbol, card, cards))
                first_symbol += 1
        if first_symbol > max_symbols:
            return None
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
    for card in cards:
        print(', '.join([str(c) for c in card]))


if __name__ == '__main__':
    generate_deck(3, 7)
    # print(get_banned([[1, 2, 3], [1, 4, 5], [2, 9, 8]], [1]))
