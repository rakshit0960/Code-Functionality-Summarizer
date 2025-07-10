async def save_to_file(content: str, file_path: str) -> None:
    """Save content to a markdown file.
    
    Args:
        content: Content to save
        file_path: Path where to save the markdown file
    """
    with open(file_path, 'w') as f:
        f.write(content)