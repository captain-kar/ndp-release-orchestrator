import streamlit as st
import yaml

st.set_page_config(page_title="Release Backport Orchestrator", layout="wide")

st.title("🚀 Release Backport Orchestrator")
st.caption("Visualize release hierarchy and manage backports")

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

repos = list(config["repos"].keys())

selected_repo = st.selectbox("Select Repository", repos)

hierarchy = config["repos"][selected_repo]["hierarchy"]

st.subheader(f"Release Hierarchy for {selected_repo}")

cols = st.columns(len(hierarchy))

for i, (col, branch) in enumerate(zip(cols, hierarchy)):
    with col:
        st.markdown(f"### {branch}")
        if i < len(hierarchy) - 1:
            st.markdown("⬇️")

st.info("Next step: Show merged PRs and missing backports across this hierarchy.")
