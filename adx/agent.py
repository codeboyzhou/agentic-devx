from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from adx.common import llms
from adx.tools import pydev, files


pydev_agent = Agent(
    name="PyDevAgent",
    model=LiteLlm(model=llms.MODEL_DEEPSEEK_CHAT),
    description="PyDevAgent: A helpful AI assistant who can empower developers with AI agents.",
    instruction="You are a helpful AI assistant who can empower developers with AI agents.",
    tools=[pydev.pip_list_outdated_packages, pydev.pip_upgrade_outdated_packages],
)

files_agent = Agent(
    name="FilesAgent",
    model=LiteLlm(model=llms.MODEL_DEEPSEEK_CHAT),
    description="FilesAgent: A helpful AI assistant who can empower developers with AI agents.",
    instruction="You are a helpful AI assistant who can empower developers with AI agents.",
    tools=[files.find, files.read],
)

root_agent = Agent(
    name="AgenticDevX",
    model=LiteLlm(model=llms.MODEL_DEEPSEEK_CHAT),
    description="Agentic-DevX: From Language to Action, Empowering Developers with AI Agents.",
    instruction="You are a helpful AI assistant who can empower developers with AI agents.",
    sub_agents=[pydev_agent, files_agent],
)
