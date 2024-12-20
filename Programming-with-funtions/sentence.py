import random
print('CODE TO AUTOMATICALLY CRETE A COMPLETE SENTENCE\n')

# these are determiners we are going to pick from
singular_d = {"a", "one", "the"}
plural_d = {"some", "many", "the"}
random_singular_d = random.choice(list(singular_d))
random_plural_d = random.choice(list(plural_d))

# these are verbs we are going to pick from
present_verbs = {"drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"}
pv = random.choice(list(present_verbs))

present_tense_singular = {"drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"}
pts = random.choice(list(present_tense_singular))

past_verbs = {"drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"}
past_v = random.choice(list(past_verbs))


past_verb_plural = {"drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"}
pvp = random.choice(list(past_verb_plural))


future_tense_verb = {"will drink", "will eat", "will grow", "will laugh",
                     "will think", "will run", "will sleep", "will talk",
                     "will walk", "will write"}
ftv = random.choice(list(future_tense_verb))


# get noun form this list
nouns = {"bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"}
random_noun = random.choice(list(nouns))

plural_noun = {"birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"}
plural_noun_random = random.choice(list(plural_noun))


def get_determiner(quantity):
    if quantity == 1:
        return random_singular_d.capitalize()
    else:
        return random_plural_d.capitalize()


def get_verb(quantity, tense):
    if tense == 'past':
        return past_v
    elif tense == 'present' and quantity == 1:
        return pts
    elif tense == 'present' and quantity != 1:
        return pvp
    elif tense == 'future':
        return ftv
    else:
        print('Not found')


def get_noun(quantity):
    if quantity == 1:
        return random_noun
    else:
        return plural_noun_random


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    verb = get_verb(quantity, tense)
    noun = get_noun(quantity)
    sentence = f"{determiner} {noun} {verb}."
    print(sentence)


def main(quantity, tense):
    make_sentence(quantity, tense)


print('THIS ARE THE SENTENCES WE GOT RANDOMLY\n')
main(1, 'past')
main(1, 'present')
main(1, 'future')
main(2, 'past')
main(2, 'present')
main(2, 'future')







