def equivalent(state1, state2):
    if (state1 in final_states and state2 not in final_states) or (state1 not in final_states and state2 in final_states):
        return False
    for symbol in alphabet:
        next_state1 = transitions[state1][symbol]
        next_state2 = transitions[state2][symbol]
        if next_state1 != next_state2:
            return False
    return True

# Définition de l'automate
states = ['A', 'B', 'C', 'D']
alphabet = ['0', '1']
transitions = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'D', '1': 'A'},
    'C': {'0': 'A', '1': 'D'},
    'D': {'0': 'C', '1': 'B'}
}
final_states = ['A', 'B']

states = ['1', '2','3','4']
alphabet = ['a', 'b']
transitions = {
    '1': {'a': '2', 'b': '3'},
    '2': {'a': '3','b':'4'},
    '3': {'a': '2', 'b': '3'},
    '4': {'a': '4', 'b': '4'},
    }
final_states = ['1', '3']


groups = [[state for state in states if state not in final_states], final_states]
while True:
    new_groups = []
    for group in groups:
        subgroups = []
        for state in group:
            found = False
            for subgroup in subgroups:
                if equivalent(state, subgroup[0]):
                    subgroup.append(state)
                    found = True
                    break
            if not found:
                subgroups.append([state])
        new_groups += subgroups
    if new_groups == groups:
        break
    groups = new_groups

# Création du nouvel automate avec les nouveaux groupes d'états
new_states = ["".join(sorted(group)) for group in groups]
new_transitions = {}
new_final_states = []
for group in groups:
    name = "".join(sorted(group))
    for symbol in alphabet:
        next_state_name = "".join(sorted(set([transitions[state][symbol] for state in group])))
        next_group_name = "".join(sorted([s for s in new_states if s.startswith(next_state_name)]))
        new_transitions[name] = {symbol: next_group_name}
    if any(state in final_states for state in group):
        new_final_states.append(name)

print(new_states)
print(new_transitions)
print(new_final_states)