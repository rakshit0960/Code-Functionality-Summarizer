from autogen_agentchat.agents import AssistantAgent
from configs.agent_config import model_client
from tools.save_to_file import save_to_file

writer_agent = AssistantAgent(
    name="WriterAgent", 
    model_client=model_client,
    tools=[save_to_file],
    system_message="""You are a writer agent that can:
    1. Write code in a given language
    2. Generate code documentation in markdown format with the following structure:
        # Module/Class/Function Name
        ## Description
        Brief description of the code
        ## Parameters
        - param1: description
        - param2: description
        ## Returns
        Description of return value
        ## Examples
        ```python
        # Example code
        ```
    3. Save documentation to markdown files""",
)
