txt = 'ab'
# char = 'a'
current_state = 'A'
valid_char = ['a', 'b', 'c']

transition = [['A', 'a', 'B'], ['A', 'b', 'B'], ['A', 'c', 'B'], ['B', 'a', 'A'], ['B', 'b', 'A'], ['B', 'c', 'A']]

char, txt = (txt[0], txt[1:]) if len(txt) > 1 else (txt, '')
print(char,txt)

for initial_state, transition_input, next_state in transition:
    print(initial_state,transition_input, next_state)

    if initial_state == current_state and char == transition_input:
        current_state = next_state
        break

    elif char not in valid_char:
        current_state = 'false'


print(current_state)