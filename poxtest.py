import os
import time
import subprocess

def average ():
    with open('pox/performanceFileOriginal', 'r') as f:
        data = [float(line.rstrip()) for line in f]
    average = sum(data) / len(data)
    print("average is: " + str(average))
    f.close()

# def command ():
#     subprocess.run(["cd", "pox"])
#     subprocess.run(["./pox.py", "skeleton", "--foo=3", "--bar=4"])
#     subprocess.run(["./pox.py", "skeleton", "--foo=3", "--bar=4"])
#     subprocess.run(["./pox.py", "skeleton", "--foo=3", "--bar=4"])
#     subprocess.run("exit 0", shell=True, check=True)
