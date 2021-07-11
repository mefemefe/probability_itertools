import itertools

n = 2 # amount of indices to pick at once

string = 'aabhda' # any iterable

char = 'a' # element to find probability of

combinations = [x for x in itertools.combinations(range(len(string)), n)] # all combinations of n indices from the string

indices = [x for x in range(len(string)) if string[x] == char] # indices that contain the element

# amount of combinations that contain the element
def find_matches(indices, combinations):
    result = 0
    for x in combinations:
        for i in indices:
            if i in x:
                result += 1
                break
    return result

matches = find_matches(indices, combinations)

# determine proportion over total
print(matches / len(combinations))