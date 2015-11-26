def matching_items(card1, card2):
    """
    Return the matching items in two cards
    """
    return list(set(card1).intersection(set(card2)))


def match(card1, card2):
    """
    Return true if two cards have a matching item
    """
    return len(set(card1) - set(card2)) > 0


def get_matches(card, deck):
    """
    Return all cards that match the given card (by index), under the key of the symbol they match on.
    """
    matches = {}
    for i, c in enumerate(deck):
        for m in matching_items(c, card):
            try:
                matches[m].append(i)
            except KeyError:
                matches[m] = [i]
    return matches


def get_matching_cards(card, deck):
    return tuple([c for c in deck if match(card, c) and card != c])
