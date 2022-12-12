import matplotlib.pyplot as plt
import streamlit as st

from run import *
from states_and_params import *


if __name__ == "__main__":
    # TODO link this to state and params

    df = pd.DataFrame(run())

    st.table(df.head())

    node_count = len(df.selected_node.unique()) - 1
    fig, ax = plt.subplots()
    ax.hist(df.selected_node, bins=node_count, range=[1,6])

    st.pyplot(fig)

    # Add a slider to the sidebar:
    weight_factor = st.sidebar.slider(
        'Weight Factor', 0, 10, 10
    )

    expected_success_latency = st.sidebar.slider(
        'Weight Factor', 0, 1, .15
    )

    weight_multiplier = st.sidebar.slider(
        'Weight Factor', 0, 100, 35
    )

    sys_params['WeightFactor'] = weight_factor
    sys_params['expectedSuccessLatency'] = expected_success_latency
    sys_params['WeightMultiplier'] = weight_multiplier
