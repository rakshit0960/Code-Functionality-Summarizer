from autogen_agentchat.agents import AssistantAgent
from configs.agent_config import model_client

code_summary_prompt="""
You are a code summary agent that can provide clear, concise summaries of Python code including functions and classes.
You analyze the code structure and explain its purpose and functionality in plain language. When asked to save summaries,
tell when the summary should be saved to a file.
"""

code_summary_agent = AssistantAgent(
    name="CodeSummaryAgent",
    model_client=model_client,
    system_message=code_summary_prompt,
)

