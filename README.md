# ndp-release-orchestrator


Phase 1 – Static UI + Release Hierarchy

Goal:
You can see your release hierarchy in a UI.

What we build:
A simple web page that shows:
    release/6.5  --->  release/6.6  --->  release/6.6  --->    release/emeraldpeak

Data source:

Store hierarchy in a config file:
repos:
  graphwriter:
    hierarchy:
      - release/6.5
      - release/6.6
      - release/6.7
      - release/emeraldpeak


STEP-1: created the config.yaml and mentioned the repos as well as it's branches heirarchy

STEP-2: Installing the dependencies

        Command: pip install streamlit pyyaml

STEP-3: Create requirements.txt

        streamlit
        pyyaml

Step 4: Create Your First UI (app.py)

Step 5: Run It

        streamlit run app.py

