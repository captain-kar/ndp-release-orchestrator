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

======================================================================================================

Phase-2 - Discover merged PRs on older branches.

Step 1: Create GitHub Token (One-time setup)

You’ll need a GitHub PAT

1. Go to GitHub → Settings → Developer Settings → Personal Access Tokens
2. Create token with:
    ✅ repo
    ✅ read:org
3. Save it somewhere safe
Then export it:
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxx


Step 2: Add Dependency
    pip install requests

Update requirements.txt:

    streamlit
    pyyaml
    requests

Step 3: Add GitHub API Client
    Create file: services/github_client.py

Step 4: Update app.py to Show Merged PRs
