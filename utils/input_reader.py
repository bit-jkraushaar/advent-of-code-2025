"""Utilities for reading puzzle input files."""

def read_input(filename):
    """
    Read lines from a file, stripping whitespace and empty lines.
    
    Args:
        filename: Path to the input file
        
    Returns:
        List of non-empty lines with whitespace stripped
    """
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def read_input_raw(filename):
    """
    Read raw content from a file without any processing.
    
    Args:
        filename: Path to the input file
        
    Returns:
        Raw file content as string
    """
    with open(filename, 'r') as f:
        return f.read()


def read_input_lines(filename, strip=True):
    """
    Read all lines from a file, including empty lines.
    
    Args:
        filename: Path to the input file
        strip: Whether to strip whitespace from lines (default True)
        
    Returns:
        List of all lines
    """
    with open(filename, 'r') as f:
        if strip:
            return [line.strip() for line in f]
        return [line.rstrip('\n') for line in f]


def read_input_groups(filename):
    """
    Read input separated by blank lines into groups.
    
    Args:
        filename: Path to the input file
        
    Returns:
        List of groups, where each group is a list of lines
    """
    with open(filename, 'r') as f:
        content = f.read()
    
    groups = []
    for group in content.split('\n\n'):
        lines = [line.strip() for line in group.split('\n') if line.strip()]
        if lines:
            groups.append(lines)
    
    return groups
