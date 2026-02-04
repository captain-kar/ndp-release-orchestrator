import streamlit as st
import yaml

from services.github_client import get_merged_prs

ORG = "captain-kar"

import os
from services.backport_detector import is_commit_in_branch


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




st.subheader("Merged PRs (last 10 per branch)")

pr_cols = st.columns(len(hierarchy))

for i, (col, branch) in enumerate(zip(pr_cols, hierarchy)):
    with col:
        st.markdown(f"### {branch}")

        try:
            prs = get_merged_prs(ORG, selected_repo, branch, limit=5)
            if not prs:
                st.caption("No merged PRs found")
            for pr in prs:
                st.markdown(f"- [#{pr['number']}]({pr['url']}) {pr['title']}")
        except Exception as e:
            st.error(f"Error fetching PRs: {e}")


st.divider()
st.subheader("Backport Status (hierarchy-wise)")

token = os.getenv("GITHUB_TOKEN")

if not token:
    st.error("GITHUB_TOKEN is not set. Backport status cannot be determined.")
else:
    for i, base_branch in enumerate(hierarchy[:-1]):  # skip the last (latest)
        st.markdown(f"## PRs merged in {base_branch}")

        prs = get_merged_prs(ORG, selected_repo, base_branch, limit=5)

        if not prs:
            st.caption(f"No merged PRs found in {base_branch}")
            continue

        for pr in prs:
            st.markdown(f"### #{pr['number']} – {pr['title']}")

            for higher_branch in hierarchy[i+1:]:
                try:
                    exists = is_commit_in_branch(
                        ORG,
                        selected_repo,
                        higher_branch,
                        pr["merge_commit_sha"],
                        token
                    )

                    if exists:
                        st.success(f"{higher_branch} → already contains this fix")
                    else:
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.warning(f"{higher_branch} → missing backport")
                        with col2:
                            st.button(
                                f"Backport → {higher_branch}",
                                key=f"{pr['number']}-{base_branch}-{higher_branch}"
                            )

                except Exception as e:
                    st.error(f"Error checking {higher_branch}: {e}")
