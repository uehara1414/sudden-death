import unicodedata


def measure_sentence_width(s):
    return sum([_width(c) for c in s])


def _width(c):
    return 2 if _is_multi_byte(c) else 1


def _is_multi_byte(c):
    return unicodedata.east_asian_width(c) in ['F', 'W', 'A']