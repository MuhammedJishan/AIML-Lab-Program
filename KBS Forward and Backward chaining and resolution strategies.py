# --------------------------------------------
# Knowledge Base
# --------------------------------------------

# Facts
facts = {"A"}

# Rules (IF condition THEN conclusion)
# (premises, conclusion)
rules = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D")
]

goal = "D"

# --------------------------------------------
# 1. Forward Chaining
# --------------------------------------------

def forward_chaining(facts, rules):
    inferred = set(facts)
    new_inferred = True

    print("\n--- Forward Chaining Steps ---")

    while new_inferred:
        new_inferred = False

        for premises, conclusion in rules:
            if all(p in inferred for p in premises):
                if conclusion not in inferred:
                    print(f"Inferred {conclusion} from {premises}")
                    inferred.add(conclusion)
                    new_inferred = True

    return inferred


# --------------------------------------------
# 2. Backward Chaining
# --------------------------------------------

def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    # If already a known fact
    if goal in facts:
        print(f"{goal} is a known fact.")
        return True

    # Prevent infinite loop
    if goal in visited:
        return False

    visited.add(goal)

    print(f"Checking goal: {goal}")

    for premises, conclusion in rules:
        if conclusion == goal:
            print(f"Trying rule: {premises} -> {conclusion}")

            if all(backward_chaining(p, facts, rules, visited)
                   for p in premises):
                print(f"{goal} is proven.")
                return True

    return False


# --------------------------------------------
# 3. Resolution (Propositional Logic)
# --------------------------------------------

def resolve(clause1, clause2):
    resolvents = []

    for literal in clause1:
        if ("~" + literal) in clause2:
            new_clause = (clause1 - {literal}) | \
                         (clause2 - {"~" + literal})
            resolvents.append(new_clause)

        elif literal.startswith("~") and literal[1:] in clause2:
            new_clause = (clause1 - {literal}) | \
                         (clause2 - {literal[1:]})
            resolvents.append(new_clause)

    return resolvents


def resolution(kb, query):
    clauses = list(kb)
    clauses.append({"~" + query})

    print("\n--- Resolution Steps ---")

    while True:
        new = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])

                for r in resolvents:
                    print(f"Resolving {clauses[i]} and {clauses[j]} -> {r}")

                    if len(r) == 0:
                        print("Empty clause derived. Query is TRUE.")
                        return True

                    if r not in clauses and r not in new:
                        new.append(r)

        if not new:
            print("No new clauses. Query is FALSE.")
            return False

        clauses.extend(new)


# --------------------------------------------
# RUNNING THE PROGRAM
# --------------------------------------------

# Forward Chaining
fc_result = forward_chaining(facts, rules)
print("\nForward Chaining Result:",
      sorted(list(fc_result - facts)))

# Backward Chaining
print("\n--- Backward Chaining ---")
bc_result = backward_chaining(goal, facts, rules)
print("Backward Chaining Result:", bc_result)

# Resolution Knowledge Base (CNF form)
kb = [
    {"~A", "B"},   # A → B
    {"~B", "C"},   # B → C
    {"~C", "D"},   # C → D
    {"A"}          # fact A
]

res_result = resolution(kb, "D")
print("\nResolution Result:", res_result)