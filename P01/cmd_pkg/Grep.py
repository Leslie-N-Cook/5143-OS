#!/usr/bin/env python3
import sys
import os
import re 
from .TockenizeFlags import tockenizeFlags
from .InvalidFlagsMsg import invalidFlagsMsg
from rich import print

grep_flags:set[str] = {
    "--help", "-c", "-i", "-v", "-l",
}
def grep(**kwargs)-> str:
    # print(kwargs)
    """
    NAME
        grep
        
    DESCRIPTION
        grep                    : prints out the lines in a file that match a given pattern
            --help              : displays how to use the grep command
            -c                  : prints the number of lines in a file that match a given pattern
            -i                  : ignores upper and lower case when searching for a pattern
            -v                  : prints lines that do not match the pattern
            -l                  : prints only the names of files that contain at least one matching line
    
    EXAMPLE
        `grep python README.md' : prints out the lines in README.md that contain the word "python"
            
    """
    flags:set[str] = tockenizeFlags(kwargs.get("flags", []))
    params:list[str] = kwargs.get("params", [])
    stdin:bool = kwargs.get("stdin", True)
    result:str = ""
    
    # Check if invalid flags are present
    if not flags.issubset(grep_flags):
        result = invalidFlagsMsg(grep, grep_flags, flags)
    # Provide help info if --help flag present
    if "--help" in flags:
        result = "".join(grep.__doc__)
       
    
    elif stdin:
        ignore_case:bool = "-i" in flags
        count_only:bool = "-c" in flags
        invert_match:bool = "-v" in flags
        list_file:bool = "-l" in flags
        
        contents:list[list[str]] = []
        count:int = 0
        # print(kwargs)
        try:
            for param in params:
                if len(params)>1:
                    pattern = params[0]
                    path = params[1::]
                    # print(path)
                    # for file in path:
                    if os.path.isfile(param):
                            with open(param, 'r') as file:
                                line_number = 1
                                for line in file:
                                    line = line.strip()
                                    match = False
                                
                                    
                                    if ignore_case:
                                        pattern = re.escape(pattern)
                                        # ignore upper and lower cases
                                        if re.search(pattern, line, re.IGNORECASE):
                                            match = True
                                            
                                    elif pattern in line:
                                        match = True
                                        
                                    if match and not invert_match:
                                        if not count_only and not list_file:
                                            contents.append(f'{os.getcwd()}/{file}: {line_number}: {line}')
                                        count+=1
                                    
                                    elif not match and invert_match:
                                        if not count_only:
                                            contents.append(f'{os.getcwd()}/{file}: {line_number}: {line}')
                                    
                                    for file in path:
                                        if match and list_file:
                                            contents.append(f'{file}')
                                            result = "\n".join(contents)
                                            return result
            
                                    line_number += 1  
                                    
                                if count_only:
                                    return count
                                        
                                result = "\n".join(contents)
                                return result
                            
            
        except FileNotFoundError:
            result = f"Error: '{file}' not found."
        
    
     
    return result
    
if __name__ == "__main__":


    # if len(sys.argv) != 3:
    #     print(grep.__doc__)
    #     sys.exit(1)
    # grep(pattern=sys.argv[1], path=sys.argv[2])
    print(grep(params=["Angel","README.md"]))