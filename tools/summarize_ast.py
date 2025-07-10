import ast
from ast import dump

async def summarize_ast_tree(code: str) -> str:
    """Get a structural overview of the AST for Python code.
    
    Args:
        code: Python code as a string

    Returns:
        A string containing an indented dump of the code's AST structure
    """
    tree = ast.parse(code)
    return dump(tree, indent=4) 