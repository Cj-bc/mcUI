from entry import Entry
import os

# ls(path) {{{
def ls(path: str) -> list:
    """get current directory's entries and return list

       Args:
            path (str): POSIX path to serch files
       Return:
            files (list of dict): list of "path" entries.
            [ {"type": <file, dir>,
               "name": <file_name>},
               ...
            ]
    """
    ret = []
    with os.scandir(path) as it:
        ret = [Entry(ent) for ent in it]
    return ret
# }}}
