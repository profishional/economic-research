from .utils import *

# policies/ calculations
def policyCherryPicker(params, substep, state_history, prev_state, **kwargs):
    picked_node = get_node(weightFactor=params['weightFactor'])
    node_id = int(picked_node.id)
    return {"new_node_id" : node_id}

# mechanics/ state updates
def stateLeadNode(params, substep, state_history, prev_state, policy_input, **kwargs):
    new_node = policy_input['new_node_id']
    return ('selected_node', new_node)