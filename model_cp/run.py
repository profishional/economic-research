from radcad import Model, Simulation, Experiment
from radcad.engine import Engine, Backend
from state_update_blocks import *
from states_and_params import *

from parts.utils import *

import matplotlib.pyplot as plt
import streamlit as st

def run():

    TIMESTEPS = 1000
    RUNS = 1

    model = Model(
        initial_state=initial_state,
        state_update_blocks=state_update_blocks,
        params=sys_params
        )

    simulation = Simulation(
        model=model,
        timesteps=TIMESTEPS,
        runs=RUNS)

    experiment = Experiment(simulation)

    # Select the Pathos backend to avoid issues with multiprocessing and Jupyter Notebooks
    # experiment.engine = Engine(backend=Backend.PATHOS)

    result = experiment.run()

    return result

if __name__ == "__main__":
    df = pd.DataFrame(run())

    node_count = len(df.selected_node.unique()) - 1
    fig, ax = plt.subplots()
    ax.hist(df.selected_node, bins=node_count, range=[1,6])

    st.pyplot(fig)