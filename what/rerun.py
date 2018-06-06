from os import path, environ, popen
from subprocess import Popen, PIPE, STDOUT

def getShell():
    path = environ['SHELL']
    temp = path.split('/')
    return temp[len(temp) - 1]

# Returns and array of all the previous 
def readHistory(shell):
    commands = []
    for line in open(path.expanduser('~/.' + shell + '_history'),'rb'):
        try:
            line = line.decode('utf8')
        except:
            line = line.decode('utf8', 'ignore')
        line = line.strip()
        if line == '': continue
        commands.append(line)
    return commands

def getLast(commands):
    line = commands[len(commands) - 2]
    line = line.split(";")
    return line[1]

def getLastOutput():
    shell = getShell()
    history = readHistory(shell)
    last = getLast(history)
    output = Popen(last, shell=True, stdin=PIPE,
                        stdout=PIPE, stderr=STDOUT)
    return output.stdout.read().decode('utf-8')