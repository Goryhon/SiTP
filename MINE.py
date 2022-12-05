from grammar import Grammar as Gr
def unreachableSymbols(grammar: Gr) -> Gr:
    """Устранение недостижимых символов в грамматике"""
    V0 = set()
    V0.add(grammar.S) # Шаг 1
    V1 = V0.copy()
    wasHere = set()
    while True:
        NT = V0.intersection(grammar.N) # Шаг 2
        for nonterm in NT:
            if nonterm not in wasHere:
                rules = grammar.P.get(nonterm, None)
                if rules is not None:
                    for rule in rules:
                        V1.update(rule)
            wasHere.add(nonterm)

        if V0 == V1: # Шаг 3
            break
        else:
            V0 = V1.copy()

    newNonTerms = V1.intersection(grammar.N)
    newTerms = V1.intersection(grammar.T)
    newRules = dict()
    for nonterm in newNonTerms:
        rules = grammar.P.get(nonterm, None)
        if rules is not None:
            newRules[nonterm] = list()
            for rule in rules:
                newRules[nonterm].append(rule)
    return Gr(newNonTerms, newTerms, newRules, grammar.S)