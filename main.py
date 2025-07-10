import asyncio
import os
from teams.round_robin_team import round_robin_team
from teams.selector_group_chat import selector_team
from autogen_agentchat.ui import Console


async def main():
    """
    Summarize a test.py Python file using the enhanced selector group chat.
    The workflow will be: Parse -> Summarize -> Save, guided by keyword hints.
    """
    
    # Check if test.py exists
    test_file_path = "test.py"
    
    with open(test_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    

    # Create the analysis task - start with parsing to analyze ALL code components
    task = f"""Please analyze this Python file completely. Extract and analyze ALL classes and functions, then provide a comprehensive summary covering every component, and save the final summary to summer.md:

File: {test_file_path}
Content:
```python
{file_content}
```

Requirements:
1. parse the code and extract all classes and functions
2. Analyze ALL classes
3. Analyze ALL functions including the main() function  
4. Provide detailed explanations for each component
5. Save a comprehensive summary covering everything
"""
    
    await Console(round_robin_team.run_stream(task=task), output_stats=True)
    
    print("✅ Analysis complete!")


if __name__ == "__main__":
    asyncio.run(main())
