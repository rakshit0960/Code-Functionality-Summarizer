import asyncio
import os
from teams.selector_group_chat import selector_team


async def main():
    """
    Summarize a test.py Python file using the selector group chat.
    The selector will automatically route this to the CodeSummaryAgent.
    """
    
    # Check if test.py exists
    test_file_path = "test.py"
    
    
    with open(test_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    

    # Create the summarization task
    task = f"""Please summarize this Python file and explain what it does, and save the summary to summary.md:

File: {test_file_path}
Content:
```python
{file_content}
```

Provide a clear summary including:
1. Main purpose of the code
2. Key functions/classes and their roles
3. Overall structure and logic flow
"""
    
    # Send the task to the selector team and stream the response
    # The "summarize" keyword will route this to CodeSummaryAgent
    print("🔄 Streaming response...\n")
    
    async for message in selector_team.run_stream(task=task):
        # Print each message as it comes in
        print(f"📝 {message}")
        print("-" * 40)
    
    print("\n✅ Summary complete!")


if __name__ == "__main__":
    print("Starting Python File Summarizer...")
    asyncio.run(main())
