from pathlib import Path

import streamlit as st
import yaml

from algolib.interfaces import __all__ as available_dependencies
from algolib.specs.schema import AlgorithmSpec, Complexity, Parameter, Returns

st.set_page_config(page_title="AlgoLib Spec Builder", layout="wide")

st.title("Algorithm Specification Builder")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Spec Builder", "Algorithm Playground"])

if page == "Spec Builder":
    with st.form("spec_form"):
        st.header("Algorithm Metadata")
        name = st.text_input("Algorithm Name")
        description = st.text_area("Description")
        category = st.text_input("Category (e.g., Sorting, Searching)")

        st.header("Complexity")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            time_worst = st.text_input("Time Worst", "O(n^2)")
        with col2:
            time_average = st.text_input("Time Average", "O(n^2)")
        with col3:
            time_best = st.text_input("Time Best", "O(n)")
        with col4:
            space_worst = st.text_input("Space Worst", "O(1)")

        st.header("Parameters")
        num_params = st.number_input("Number of Parameters", min_value=1, value=1)
        parameters = []
        for i in range(num_params):
            st.subheader(f"Parameter {i + 1}")
            p_col1, p_col2, p_col3 = st.columns(3)
            with p_col1:
                p_name = st.text_input("Name", key=f"p_name_{i}")
            with p_col2:
                p_type = st.text_input("Type", key=f"p_type_{i}")
            with p_col3:
                p_desc = st.text_input("Description", key=f"p_desc_{i}")
            parameters.append({"name": p_name, "type": p_type, "description": p_desc})

        st.header("Returns")
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            r_type = st.text_input("Return Type")
        with r_col2:
            r_desc = st.text_input("Return Description")

        st.header("Dependencies")
        dependencies = st.multiselect(
            "Select algorithm dependencies",
            options=available_dependencies,
        )

        submitted = st.form_submit_button("Generate Spec File")
        if submitted:
            try:
                spec = AlgorithmSpec(
                    name=name,
                    description=description,
                    category=category,
                    complexity=Complexity(
                        time_worst=time_worst,
                        time_average=time_average,
                        time_best=time_best,
                        space_worst=space_worst,
                    ),
                    parameters=[Parameter(**p) for p in parameters],
                    returns=Returns(type=r_type, description=r_desc),
                    dependencies=dependencies,
                )
                file_name = f"{name.replace(' ', '_')}.yml"
                file_path = Path("specs") / file_name
                with open(file_path, "w") as f:
                    yaml.dump(spec.model_dump(), f, sort_keys=False)
                st.success(f"Successfully created spec file: `{file_path}`")
                st.code(spec.model_dump_json(indent=2), language="json")
            except Exception as e:
                st.error(f"Error validating or creating spec file: {e}")

elif page == "Algorithm Playground":
    st.title("Algorithm Playground")
    st.write("Visualizations for algorithms will be available here.")
