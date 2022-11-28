from parts.agent_cp import *
import random


def initialize_seed(params, substep, state_history, prev_state):
    if prev_state['timestep'] == 0:
        random.seed(a=f'{prev_state["simulation"]}/{prev_state["subset"]}/{prev_state["run"]}')
    return {}

state_update_blocks = [
    {
        'policies': {
            'cherry_picker' : policyCherryPicker,
        },
        'variables': {
            'selected_node' : stateLeadNode,
        }
    }
]