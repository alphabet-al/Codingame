class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name

    def run(self, cargo, current_state):
        try:
            handler = self.handlers[self.startState]
        except:
            raise KeyError("must call .set_start() before .run()")
        if not self.endStates:
            raise  KeyError("at least one state must be an end_state")

        while True:
            (newState, cargo) = handler(cargo, current_state)
            if cargo == '' and newState in self.endStates:
                print('true')
                break 
            elif cargo == '' and newState not in self.endStates:
                print('false')
                break
            elif newState == 'false':
                print('false')
                break
            else:
                handler = self.handlers[newState]  
                current_state = newState

def state_transitions(txt, current_state):
    char, txt = (txt[0], txt[1:]) if len(txt) > 1 else (txt, '')
    
    for initial_state, transition_input, next_state in transition:

        if initial_state == current_state and char == transition_input:
            current_state = next_state
            return current_state, txt

        elif char not in valid_char:
            current_state = 'false'
            return current_state, txt
    
    return current_state, txt


if __name__ == "__main__":
    
    valid_char = ['a', 'b', 'c', 'd'] # input().split()
    states = ['A', 'B', 'C'] # input().split()
    number_of_transitions = 6 # int(input())

    transition = [['A', 'a', 'B'], ['B', 'c', 'C'], ['C', 'a', 'C'], ['C', 'b', 'C'], ['C', 'c', 'C'], ['C', 'd', 'C']] # [input().split() for i in range(number_of_transitions)]
        
    start_state = 'A' # input()
    end_states = 'C' # input().split()
    number_of_words = 7 # int(input())
    words = ['ac', 'ab', 'acabcd', 'acabcde', 'a', 'acaaacca', 'cafds'] # [input() for i in range(number_of_words)]

    sm = StateMachine()
    
    for i in states:
        if i in end_states:
            sm.add_state(i, state_transitions, end_state = 1)
        else:
            sm.add_state(i, state_transitions)
    
    sm.set_start(start_state)
    
    for i in words:
        current_state = start_state
        sm.run(i, current_state)


