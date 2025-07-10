async def save_to_file(content: str, file_path: str, mode: str = 'w') -> str:
    """Save content to a file.
    
    Args:
        content: Content to save
        file_path: Path where to save the markdown file
        mode: Mode to open the file in (default: 'w')
        
    Returns:
        Success message or error message
    """
    try:
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(content)
        return f"✅ Successfully saved content to {file_path}"
    except Exception as e:
        return f"❌ Error saving to {file_path}: {str(e)}"