from turing_machine.dtm import DTM 
dtm = DTM(
states = {'q0', 'q1', 'qacc', 'q2', 'q4', 'q3', 'qrej'},
input_symbols = {'1', '0'},
tape_symbols = {'1', '0', 'y', '>', '.', 'x'},
left_end = '>',
transitions = {'q0': {'>': ('q1', '>', 'R')}, 'q1': {'0': ('q2', 'x', 'R'), '1': ('qrej', '1', 'R'), 'y': ('q4', 'y', 'R')}, 'q2': {'0': ('q2', '0', 'R'), '1': ('q3', 'y', 'L'), 'y': ('q2', 'y', 'R')}, 'q3': {'0': ('q3', '0', 'L'), 'x': ('q1', 'x', 'R'), 'y': ('q3', 'y', 'L')}, 'q4': {'y': ('q4', 'y', 'R'), '1': ('qrej', '1', 'R'), '.': ('qacc', '.', 'R')}},
initial_state = 'q0',
blank_symbol = '.',
reject_state = 'qrej', 
final_states = 'qacc' 
)