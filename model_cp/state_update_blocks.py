from parts.agent_cp import *
import random


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