import matplotlib.pyplot as plt
import streamlit as st

from run import *


if __name__ == "__main__":
    # TODO link this to state and params

    df = pd.DataFrame(run())

    st.table(df.head())

    node_count = len(df.selected_node.unique()) - 1
    fig, ax = plt.subplots()
    ax.hist(df.selected_node, bins=node_count, range=[1,6])

    st.pyplot(fig)

    # slider input
    # x = st.slider('x')
    # st.write(x, 'test', x*x)


    # # Add a slider to the sidebar:
    # add_slider = st.sidebar.slider(
    #     'Select a range of values',
    #     0, 100
    # )

