## Linux Shell commands implemented in Python
### Authors: 
### - Leslie Cook 
### - Angel Badillo
 

|        Command        |                  Description                  |             Flags             |            Parameters            |
| :--------------------: | :-------------------------------------------: |  :---------------------------: | :-------------------------------: |
|   [cat](cmd_pkg/Cat.py)   |               concatenate files               |                              |          `<file name>`          |
|    [cd](cmd_pkg/Cd.py)    |               change directory               |                             | `~` or `..` or `<dir name>` |
| [chmod](cmd_pkg/Chmod.py) |  changes read, write, executable permissions  |                                |  `<octal number> <file name>`  |
| [clear](cmd_pkg/Clear.py) |               clears the screen               |                                |                                  |
|    [cp](cmd_pkg/Cp.py)    |           copy file/dir to new path           |                                 |     `<file/dir> <new path>`     |
| [exit](cmd_pkg/Exit.py)   |               exits the shell               |                                |                                  |
|  [grep](cmd_pkg/Grep.py)  | searches for a specific pattern of characters |  `-c` `-i` `-v ` `-l` |     `<pattern> <file path>`     |
|  [head](cmd_pkg/Head.py)  | writes to stdout the first 10 lines of a file |         `-n, n is int`       |        `<path to file>`        |
| [InvalidFlagMsg](cmd_pkg/InvalidFlagMsg.py) | prints invalid flag message |        |       |
|  [less](cmd_pkg/Less.py)  |      shows files contents on one screen      |                               |        ` <path to file>`        |
|    [ls](cmd_pkg/Ls.py)    |               directory listing               | `-l` `-a` `-h` `-lah` |          `<dir name>`          |
| [mdkir](cmd_pkg/Mkdir.py) |             makes a new directory             |                               |          `<dir name>`       |
|    [mv](cmd_pkg/Mv.py)    |           move file/dir to new path           |                              |     `<file/dir> <new path>`     |
|   [pwd](cmd_pkg/Pwd.py)   |            print working directory            |                             |                                  |
|    [rm](cmd_pkg/Rm.py)    |           remove file / directories           |             `-r`            | `<dir name>` or `<file name>` |
|  [rmdir](cmd_pkg/Rmdir)  |            remove empty directory            |                                |          `<dir name>`          |
|  [sort](cmd_pkg/Sort.py)  |                   sort data                   |                              |          `<file name>`          |
|  [tail](cmd_pkg/Tail.py)  | writes to stdout the last 10 lines of a file |         `-n, n is int`       |        `<path to file>`        |
| [TokenizeFlags](cmd_pkg/TokenizeFlags.py) | tokenizes flags |  |  |
| [touch](cmd_pkg/Touch.py) |             creates an empty file             |                                 |        `<new file name>`        |
|    [wc](cmd_pkg/Wc.py)    |   show line, word, and byte count of files   |       `-l` `-m` `-w`     |          `<file name>`          |
|   [who](cmd_pkg/Who.py)   |             show users logged in             |                                |                                  |




