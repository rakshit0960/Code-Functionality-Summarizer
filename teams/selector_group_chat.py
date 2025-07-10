from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.agents import AssistantAgent
from configs.agent_config import model_client
from agents.code_summary_agent import code_summary_agent
from agents.parser_agent import parser_agent
from agents.writer_agent import writer_agent

def selector_func(messages):
    """
    Enhanced selector function that chooses the appropriate agent based on:
    1. Workflow keywords from previous agent responses
    2. Keywords in the user's initial message
    3. Default routing logic
    """
    if not messages:
        return "ParserAgent"  # Default to parser agent to start
        
    last_message = str(messages[-1]).lower()
    
    # Check for workflow keywords from agents (highest priority)
    if "workflow: save to file" in last_message or "workflow: write" in last_message:
        return "WriterAgent"
    elif "workflow: summarize code" in last_message or "workflow: summarize" in last_message:
        return "CodeSummaryAgent"
    elif "workflow: parse" in last_message or "workflow: analyze further" in last_message:
        return "ParserAgent"
    elif "workflow: task complete" in last_message:
        return None  # End the conversation
    
    # Check for user keywords (medium priority)
    elif any(keyword in last_message for keyword in ["summary", "summarize", "explain", "understand", "what does"]):
        return "CodeSummaryAgent"
    elif any(keyword in last_message for keyword in ["extract", "parse", "ast", "definitions", "analyze"]):
        return "ParserAgent"
    elif any(keyword in last_message for keyword in ["write", "create", "save"]):
        return "WriterAgent"
    else:
        # Default logic - start with parsing for code analysis
        return "ParserAgent"

# Create the selector group chat
selector_team = SelectorGroupChat(
    participants=[code_summary_agent, parser_agent, writer_agent],
    model_client=model_client,
    selector_func=selector_func,
    max_turns=10,  # Prevent infinite loops
)
    
