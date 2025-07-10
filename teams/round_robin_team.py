from autogen_agentchat.teams import RoundRobinGroupChat
from configs.agent_config import model_client
from agents.code_summary_agent import code_summary_agent
from agents.parser_agent import parser_agent
from agents.writer_agent import writer_agent

# Create the round robin group chat
# This ensures each agent gets a turn in a predictable order:
# 1. ParserAgent (analyzes and extracts code structure)
# 2. CodeSummaryAgent (creates comprehensive summaries) 
# 3. WriterAgent (saves the final output)

round_robin_team = RoundRobinGroupChat(
    participants=[parser_agent, code_summary_agent, writer_agent],
    max_turns=12,
) 