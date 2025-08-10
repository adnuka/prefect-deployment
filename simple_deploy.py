#!/usr/bin/env python3
"""
Simple deployment script that pulls fresh code from GitHub
"""

import os
from prefect import flow
from prefect_github.repository import GitHubRepository

# Set API URL for Docker Prefect server
os.environ["PREFECT_API_URL"] = "http://localhost:4200/api"

def deploy_flow():
    """Deploy flow from GitHub with fresh pull every time"""
    
    print("🚀 Creating deployment that pulls fresh code from GitHub...")
    
    # Load the GitHub repository block
    github_repo = GitHubRepository.load("github-repo")
    
    # Create deployment using flow.from_source (modern Prefect API)
    flow_from_source = flow.from_source(
        source=github_repo,
        entrypoint="test-flow-from-github.py:hello_world_flow"
    )
    
    # Deploy using the modern API
    deployment_id = flow_from_source.deploy(
        name="fresh-github-deployment",
        work_pool_name="my-pool",
        parameters={},  # Use defaults from GitHub code
        push=False
    )
    
    print("✅ Deployment created successfully!")
    print("   Name: hello-world-flow/fresh-github-deployment")
    print("   This deployment will pull fresh code from GitHub on every run")
    print("")
    print("🔧 To run: prefect deployment run 'hello-world-flow/fresh-github-deployment'")

if __name__ == "__main__":
    deploy_flow()
