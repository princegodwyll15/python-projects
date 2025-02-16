import random
print('CODE TO AUTOMATICALLY CRETE A COMPLETE SENTENCE\n')


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    elif tense == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == 'past' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
                 "will talk", "will walk", "will write"]
    else:
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"
                 "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"
                 "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"
                 "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
                 "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb


def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun


def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    prep = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{prep} {determiner} {noun}"
    return prepositional_phrase


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    verb = get_verb(quantity, tense)
    noun = get_noun(quantity)
    prep_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prep_phrase}."
    return sentence


def main(quantity, tense):
    sentence = make_sentence(quantity, tense)
    print(sentence)


print('YOUR AUTOMATICALLY GENERATED SENTENCES ARE;\n')
main(1, 'past')
main(1, 'present')
main(1, 'future')
main(2, 'past')
main(2, 'present')
main(2, 'future')







