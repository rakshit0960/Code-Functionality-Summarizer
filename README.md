# AutoGen Multi-Agent Code Analysis System

A powerful multi-agent system built with Microsoft AutoGen that provides intelligent code analysis, parsing, and documentation generation through specialized AI agents.

## 🚀 Features

- **Intelligent Agent Selection**: Automatically routes tasks to the most appropriate agent based on context
- **Real-time Streaming**: Watch agents work in real-time with streaming console output
- **Specialized Agents**: Three focused agents for different code analysis tasks
- **Easy Integration**: Simple API for adding code analysis to your workflows

## 🤖 Available Agents

### 📖 CodeSummaryAgent
- **Purpose**: Provides clear, concise summaries of Python code
- **Use Cases**: Understanding code structure, explaining functionality, code documentation
- **Triggers**: "summary", "summarize", "explain", "understand", "what does"

### 🔍 ParserAgent  
- **Purpose**: Extracts definitions and analyzes AST structures
- **Tools**: `extract_definitions`, `summarize_ast_tree`
- **Use Cases**: Code parsing, definition extraction, structural analysis
- **Triggers**: "extract", "parse", "ast", "definitions", "analyze"

### ✍️ WriterAgent
- **Purpose**: Creates new code and documentation
- **Tools**: `save_to_file`
- **Use Cases**: Code generation, documentation creation, file operations
- **Triggers**: "write", "create", "save"

## 📁 Project Structure

```
autogen/
├── agents/
│   ├── code_summary_agent.py    # Code summarization agent
│   ├── parser_agent.py          # AST parsing and analysis agent
│   └── writer_agent.py          # Code and documentation writer
├── configs/
│   └── agent_config.py          # Model configuration (Gemini 2.5 Flash)
├── teams/
│   └── selector_group_chat.py   # Smart agent selection system
├── tools/
│   ├── extract_definitions.py   # Function/class extraction tool
│   ├── summarize_ast.py         # AST analysis tool
│   └── save_to_file.py          # File saving utility
├── prompts/
│   └── selector_prompt.py       # Selection prompts
├── main.py                      # Demo: Python file summarizer
└── README.md                    # This file
```

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd autogen
   ```

2. **Install dependencies**
   ```bash
   pip install autogen-agentchat autogen-ext python-dotenv
   ```

3. **Configure environment**
   Create a `.env` file with your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🎯 Quick Start

### Basic Usage

1. **Create a test.py file** with some Python code you want to analyze

2. **Run the demo**:
   ```bash
   python main.py
   ```

   This will automatically:
   - Read your `test.py` file
   - Route the task to the appropriate agent (CodeSummaryAgent for summaries)
   - Stream the analysis results in real-time

### Example Output
```
🔄 Streaming response...

📝 [CodeSummaryAgent]: This Python file contains a factorial calculation function...
----------------------------------------
📝 [CodeSummaryAgent]: The main components include:
1. factorial(n) function - calculates factorial recursively
2. Input validation for negative numbers
3. Simple test cases at the bottom
----------------------------------------

✅ Summary complete!
```

## 💻 Programmatic Usage

```python
import asyncio
from teams.selector_group_chat import selector_team

async def analyze_code():
    # The selector automatically chooses the right agent
    task = "Please summarize this Python function and explain what it does"
    
    # Stream responses in real-time
    async for message in selector_team.run_stream(task=task):
        print(f"Agent: {message}")
    
    # Or get complete response
    response = await selector_team.run(task=task)
    return response

# Run the analysis
asyncio.run(analyze_code())
```

## 🎛️ Customization

### Adding New Agents

1. Create your agent in the `agents/` directory:
   ```python
   from autogen_agentchat.agents import AssistantAgent
   from configs.agent_config import model_client
   
   my_agent = AssistantAgent(
       name="MyAgent",
       model_client=model_client,
       system_message="Your agent's role and instructions"
   )
   ```

2. Add it to the selector group chat in `teams/selector_group_chat.py`

### Modifying Selection Logic

Update the `selector_func` in `teams/selector_group_chat.py` to add new keywords or routing logic:

```python
def selector_func(messages):
    last_message = str(messages[-1]).lower()
    
    if "your_keyword" in last_message:
        return "YourAgent"
    # ... existing logic
```

## 🔧 Configuration

### Model Settings
Edit `configs/agent_config.py` to change the underlying model:

```python
model_client = OpenAIChatCompletionClient(
    model="gemini-2.5-flash",  # or other compatible models
    api_key=gemini_api_key,
)
```

### Agent Behavior
Modify individual agent system messages in their respective files to customize behavior.

## 🛠️ Tools

The system includes several built-in tools:

- **extract_definitions**: Extracts function and class definitions from Python code
- **summarize_ast_tree**: Provides structural analysis of Python AST
- **save_to_file**: Saves generated content to files

## 📚 Example Use Cases

1. **Code Review**: "Summarize this module and identify potential issues"
2. **Documentation**: "Extract all function definitions and create documentation"
3. **Learning**: "Explain how this algorithm works step by step"
4. **Refactoring**: "Analyze this code structure and suggest improvements"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- Check the [AutoGen Documentation](https://microsoft.github.io/autogen/stable/)
- Create an issue for bugs or feature requests
- Review existing examples in the codebase

---

**Built with ❤️ using Microsoft AutoGen** 