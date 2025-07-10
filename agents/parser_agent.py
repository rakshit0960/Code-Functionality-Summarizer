from autogen_agentchat.agents import AssistantAgent
from configs.agent_config import model_client
from tools.extract_definitions import extract_definitions
from tools.summarize_ast import summarize_ast_tree

parser_prompt="""
You are a parser agent that can extract definitions and summarize the AST tree of a Python file.
"""

parser_agent = AssistantAgent(
    name="ParserAgent",
    model_client=model_client,
    tools=[extract_definitions, summarize_ast_tree],
    
)
