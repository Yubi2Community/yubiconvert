"""Word2Number Library that supports indian currency standards
"""

import re

import nltk

num_names = {
    "zero": 0,
    "naught": 0,
    "nil": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "niner": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

common_place_abbrev = {"k": 1_000}
indian_place_abbrev = {"l": 1_00_000, "c": 1_00_00_000, "cr": 1_00_00_000}
us_place_abbrev = {"m": 1_000_000, "b": 1_000_000_000}
place_abbrev = {**common_place_abbrev, **indian_place_abbrev, **us_place_abbrev}

common_place_names = {
    "dozen": 12,
    "score": 20,
    "hundred": 100,
    "gross": 144,
    "thousand": 1_000,
}

indian_place_names = {"lakh": 1_00_000, "lac": 1_00_000, "crore": 1_00_00_000}
us_place_names = {
    "million": 1_000_000,
    "billion": 1_000_000_000,
    "trillion": 1_000_000_000_000,
    "quadrillion": 1_000_000_000_000_000,
    "quintillion": 1_000_000_000_000_000_000,
    "sextillion": 1_000_000_000_000_000_000_000,
    "septillion": 1_000_000_000_000_000_000_000_000,
    "octillion": 1_000_000_000_000_000_000_000_000_000,
    "nonillion": 1_000_000_000_000_000_000_000_000_000_000,
    "decillion": 1_000_000_000_000_000_000_000_000_000_000_000,
}
place_names = {
    **common_place_names,
    **indian_place_names,
    **us_place_names,
    **place_abbrev,
}

dec_names = {
    "point": ".",
    "decimal": ".",
    ".": ".",
}

neg_names = {
    "minus": "-",
    "negative": "-",
    "-": "-",
}

ignore_chars = ["$", ";", ","]
ignore_words = ["a", "and", "&", "", "rs", "rupee", "rupees"]

word_to_number = {**num_names, **place_names, **dec_names, **neg_names}
number_to_word = {str(j): i for i, j in word_to_number.items()}


def num_generator(phrase):
    """Generator to return numeric value for a given string

    Args:
        phrase (str): input string

    Raises:
        ValueError

    Yields:
        int: numeric value of input string
    """
    # remove dirty characters - commonly put in numbers but not "part of" the number
    cleanphrase = "".join(char for char in phrase if char not in ignore_chars)
    # make . its own word so we can treat it like the other decimal words
    splitphrase = cleanphrase.replace(".", " . ").lower()

    words = []
    # remove dirty words - commonly put in number words but not "part of" the number
    for word in (word for word in splitphrase.split(" ") if word not in ignore_words):
        # separate suffixes (e.g. 150k -> 150 k)
        if word[:-1].isdigit() and word[-1] in place_abbrev:
            words.append(word[:-1])
            words.append(word[-1])
        # - is confusing, since it can be a separator (sixty-six) or a negative (-10)
        # fortunately, to be a negative it must be at the start of a word
        elif "-" in word:
            i = word.index("-")
            if i == 0:
                words.append("-")
                words.append(word[1:])
            else:
                words.append(word[:i])
                words.append(word[i + 1 :])
        else:
            words.append(word)

    if len(words) == 0:
        raise ValueError("No valid words provided")

    # Check if there are any valid number words
    if len(words) == (sum(words.count(dec) for dec in dec_names)) + (
        sum(words.count(neg) for neg in neg_names)
    ):
        raise ValueError("No valid number words provided")

    # Check if there are any illegal duplicates
    if 1 < (sum(words.count(dec) for dec in dec_names)):
        jls_extract_var = "At most one of the following allowed: {}"
        raise ValueError(jls_extract_var.format(dec_names))

    if 1 < (sum(words.count(neg) for neg in neg_names)):
        jls_extract_var = "At most one of the following allowed: {}"
        raise ValueError(
            jls_extract_var.format(sum(words.count(neg) for neg in neg_names))
        )

    # Iterate over the words, yielding them consecutively as numbers
    for word in words:
        if word in word_to_number:
            yield word_to_number[word]
        else:
            try:
                yield int(word)
            except ValueError:
                try:
                    yield float(word)
                except Exception as exc:
                    jls_extract_var = "Please check your spelling for: {}"
                    raise ValueError(jls_extract_var.format(word)) from exc


def _word_to_num(phrase):
    """function to convert string to it's numeric value

    Args:
        phrase (str): input string

    Raises:
        ValueError

    Returns:
        int/float: numeric value of input string
    """
    if not isinstance(phrase, str):
        raise ValueError(
            "Type of input is not string! Please enter a valid number word (eg. 'two million twenty three thousand and forty nine')"
        )
    phrase = phrase.lower()
    phrase = phrase.replace("rupees", "rupee")
    count_indian_standards = 0
    count_us_standards = 0
    for i in phrase.split():
        if i in indian_place_abbrev or i in indian_place_names:
            count_indian_standards += 1
        elif i in us_place_abbrev or i in us_place_names:
            count_us_standards += 1
    if all([count_indian_standards > 0, count_us_standards > 0]):
        raise ValueError("Input has multiple currency standards")
    paisa_number = 0
    ## Handling paisa values in indian currency standards similar to cents in US
    if " and" in phrase and "paisa" in phrase:
        and_index = phrase.find(" and")
        paisa_index = phrase.find("paisa")
        sub_phrase = phrase[and_index + len(" and") : paisa_index]
        phrase = phrase[:and_index]
        paisa_number += _word_to_num(sub_phrase)

    elif " rupee" in phrase and "paisa" in phrase:
        and_index = phrase.find(" rupee")
        paisa_index = phrase.find("paisa")
        sub_phrase = phrase[and_index + len(" rupee") : paisa_index]
        phrase = phrase[:and_index]
        paisa_number += _word_to_num(sub_phrase)

    elif " and" in phrase and "cent" in phrase:
        and_index = phrase.find(" and")
        paisa_index = phrase.find("cent")
        sub_phrase = phrase[and_index + len(" and") : paisa_index]
        phrase = phrase[:and_index]
        paisa_number += _word_to_num(sub_phrase)
    running_total = [0]
    post_decimal_count = 0
    sign = 1

    for num in num_generator(phrase):
        if num == ".":
            post_decimal_count = -1

        elif num == "-":
            if running_total[0] != 0:
                raise ValueError("Negating word must be first word")
            sign = -1

        elif num in place_names.values():
            # Get the next index which is smaller than the current item
            index = next((i for i, x in enumerate(running_total) if x < num), -1)

            # Sum all the smaller parts
            # e.g. if we are parsing 'one million four hundred thirty six thousand', we'll have
            # [ 1000000, 400, 36 ] when handling 1000; since 400 and 36 are both smaller than
            # 1000 but 1000000 is not, we'll sum the smaller stuff to give [ 1000000, 436 ].
            # We'll later multiply the last item by this place name
            running_total = running_total[:index] + [sum(running_total[index:])]

            # Special case if someone starts with a place name, e.g. 'hundred twenty' rather than
            # 'one hundred twenty'
            if running_total[-1] == 0:
                running_total[-1] = 1

            running_total[-1] *= num

            # Append a new item after this - we've just handled a place name, and need to separate
            # the remaining content in case we have another place name coming
            running_total.append(0)
            post_decimal_count = 0

        elif len(str(num)) != len(str(running_total[-1])) or post_decimal_count:
            # Special case to pre-adjust the decimal value, in case someone puts something like
            # 'point nineteen'
            if post_decimal_count:
                post_decimal_count -= len(str(num)) - 1
            running_total[-1] += num * 10**post_decimal_count
            if post_decimal_count:
                post_decimal_count -= 1
        else:
            running_total.append(0)
            running_total[-1] = num
    if all(num < 10 for num in running_total):
        final_value = sign * sum(
            num * 10**i for i, num in enumerate(reversed(running_total))
        )
    else:
        final_value = sign * sum(running_total)
    return final_value + paisa_number / 100 if paisa_number else final_value


def word_to_num(text):
    if not isinstance(text, str):
        raise ValueError("Only String format is supported")
    text = " ".join([number_to_word.get(i, i) for i in text.lower().strip().split(" ")])
    if text.find("-") not in [-1, 0]:
        text = text.replace("-", " ")
    tagged_number_words = " ".join([f"{i}/CD" for i in word_to_number])
    tagged_number_words += (
        " a/CD and/CD &/CD rs/CD rupee/CD rupees/CD paisa/CD cent/CD cents/CD"
    )
    tagged_number_words_tuples = [
        nltk.tag.str2tuple(t) for t in tagged_number_words.split()
    ]
    my_tagger = nltk.UnigramTagger(
        [tagged_number_words_tuples], backoff=nltk.DefaultTagger("IGNORE")
    )

    my_grammar = "NumberWord: {<CD>+}"
    parser = nltk.RegexpParser(my_grammar)
    parsed = parser.parse(my_tagger.tag(nltk.word_tokenize(text.lower())))
    for tag in [
        tree.leaves() for tree in parsed.subtrees() if tree.label() == "NumberWord"
    ]:
        try:
            ut = nltk.untag(tag)
            if len(ut) == 1 and any(
                [True for u in ignore_chars + ignore_words if u in ut]
            ):
                continue

            num = _word_to_num(" ".join(ut))
            regex = re.compile(re.escape(" ".join(ut)), re.IGNORECASE)
            text = regex.sub(str(num), text, 1)
        except Exception as exp:
            raise exp
    return text


# print(
#     word_to_num(
#         """nine hundred ninety nine decillion nine hundred ninety nine nonillion nine hundred ninety nine octillion nine hundred ninety nine septillion nine hundred ninety nine sextillion nine hundred ninety nine quintillion nine hundred ninety nine quadrillion nine hundred ninety nine trillion nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine"""
#     )
# )
##TODO
# f = re.findall("(\d+)\s(\d+)", "325 110115")[0]
# f[0] + f[1][1:]
