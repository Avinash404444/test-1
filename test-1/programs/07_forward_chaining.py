facts = {"A"}
rules = [({"A"}, "B"), ({"B"}, "C"), ({"C"}, "D")]

def forward_chain(facts, rules):
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if conditions.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True
    return inferred

print("Inferred Facts:", forward_chain(facts, rules))
