def build_transition_function(needle):
    m = len(needle)
    alphabet = set(needle)
    transition = [{} for _ in range(m + 1)]

    for q in range(m + 1):
        for a in alphabet:
            k = min(m, q + 1)
            while k > 0 and not (needle[:k] == (needle[:q] + a)[-k:]):
                k -= 1
            transition[q][a] = k
    return transition

def finite_automaton_search(haystack, needle):
    transition = build_transition_function(needle)
    m = len(needle)
    q = 0
    result = []

    for i, char in enumerate(haystack):
        if char in transition[q]:
            q = transition[q][char]
        else:
            q = 0
        if q == m:
            result.append(i - m + 1)
    return result

haystack = "qwerwerqwer"
needle = "qwer"
indices = finite_automaton_search(haystack, needle)
print("Індекси входжень:", indices)