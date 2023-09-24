## Linux Shell commands implemented in Python
### Authors: 
### - Leslie Cook 
### - Angel Badillo
 
# List of commands

|        Command        |                  Description                  |             Flags             |            Parameters            |
| :--------------------: | :-------------------------------------------: |  :---------------------------: | :-------------------------------: |
|   [cat](Cat.py)   |               concatenate files               |                              |          `<file name>`          |
|    [cd](Cd.py)    |               change directory               |                             | `~` or `..` or `<dir name>` |
| [chmod](Chmod.py) |  changes read, write, executable permissions  |                                |  `<octal number> <file name>`  |
| [clear](Clear.py) |               clears the screen               |                                |                                  |
|    [cp](Cp.py)    |           copy file/dir to new path           |                                 |     `<file/dir> <new path>`     |
| [exit](Exit.py)   |               exits the shell               |                                |                                  |
|  [grep](Grep.py)  | searches for a specific pattern of characters |  `-c` `-i` `-v ` `-l` |     `<pattern> <file path>`     |
|  [head](Head.py)  | writes to stdout the first 10 lines of a file |         `-n, n is int`       |        `<path to file>`        |
| [history](../shell.py) | shows history of commands entered by the user |                             |             `<num>`             |
| [!x](../shell.py) | retrieves the line from command  history and excutes it |                          |             `<num>`             |
|  [less](Less.py)  |      shows files contents on one screen      |                               |        ` <path to file>`        |
|    [ls](Ls.py)    |               directory listing               | `-l` `-a` `-h` `-lah` |          `<dir name>`          |
| [mdkir](Mkdir.py) |             makes a new directory             |                               |          `<dir name>`       |
|    [mv](Mv.py)    |           move file/dir to new path           |                              |     `<file/dir> <new path>`     |
|   [pwd](Pwd.py)   |            print working directory            |                             |                                  |
|    [rm](Rm.py)    |           remove file / directories           |             `-r`            | `<dir name>` or `<file name>` |
|  [rmdir](Rmdir)  |            remove empty directory            |                                |          `<dir name>`          |
|  [sort](Sort.py)  |                   sort data                   |                              |          `<file name>`          |
|  [tail](Tail.py)  | writes to stdout the last 10 lines of a file |         `-n, n is int`       |        `<path to file>`        |
| [touch](Touch.py) |             creates an empty file             |                                 |        `<new file name>`        |
|    [wc](Wc.py)    |   show line, word, and byte count of files   |       `-l` `-m` `-w`     |          `<file name>`          |
|   [who](Who.py)   |             show users logged in             |                                |                                  |



# List of support functions
|        Function        |                  Description                  |
| :--------------------: | :-------------------------------------------: |
| [init](__init__.py) | initializes the commands in a package for the shell to use | 
| [InvalidFlagMsg](InvalidFlagMsg.py) | creates error message when flag not recognized |        
| [TokenizeFlags](TokenizeFlags.py) | checks for flags to directs command behavior |  



