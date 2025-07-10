from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.agents import AssistantAgent
from configs.agent_config import model_client
from agents.code_summary_agent import code_summary_agent
from agents.parser_agent import parser_agent
from agents.writer_agent import writer_agent

def selector_func(messages):
    """
    Simple selector function that chooses the appropriate agent based on keywords in the last message.
    Returns the name of the agent that should respond next.
    """
    if not messages:
        return "ParserAgent"  # Default to parser agent
        
    last_message = str(messages[-1]).lower()
    
    # Check for keywords to determine which agent should respond
    if any(keyword in last_message for keyword in ["summary", "summarize", "explain", "understand", "what does"]):
        return "CodeSummaryAgent"
    elif any(keyword in last_message for keyword in ["extract", "parse", "ast", "definitions", "analyze"]):
        return "ParserAgent"
    elif any(keyword in last_message for keyword in ["write", "create", "save"]):
        return "WriterAgent"
    else:
        # Default to parser agent for general code analysis
        return "ParserAgent"

# Create the selector group chat
selector_team = SelectorGroupChat(
    participants=[code_summary_agent, parser_agent, writer_agent],
    model_client=model_client,
    selector_func=selector_func,
    max_turns=10,  # Prevent infinite loops
)
    
