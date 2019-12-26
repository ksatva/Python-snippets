#! /usr/bin/pyhton3

#++++++++++++discard=====updated to FUNCTIONS.py
#block
def appopen(filepath):
    import subprocess
    subprocess.call(["xdg-open",filepath])
