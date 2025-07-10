import ast
from typing import Tuple, List

async def extract_definitions(code: str) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]]]:
    """Extract function and class definitions from Python code.
    
    Args:
        code: Python code as a string

    Returns:
        A tuple containing two lists:
        - List of tuples, each containing the name and source code of a function
        - List of tuples, each containing the name and source code of a class
    """
    tree = ast.parse(code)
    functions = []  
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append((node.name, ast.get_source_segment(code, node)))
        elif isinstance(node, ast.ClassDef):
            classes.append((node.name, ast.get_source_segment(code, node)))
            
    return functions, classes 