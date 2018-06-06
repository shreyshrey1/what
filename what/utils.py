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
        # if len(line)>0 and line[0]=='#':
        #     try:
        #         dt = datetime.fromtimestamp(int(line.replace("#","")))
        #         continue
        #     except:
        #         dt = None
        if line == '': continue
        commands.append(line)
    return commands

def getLast(commands):
    line = commands[len(commands) - 2]
    line = line.split(";")
    return line[1]

def checkOutput(command):
    print(command.split(' '))
    return subprocess.check_output(command.split(' '))

def getLastOutput():
    shell = getShell()
    history = readHistory(shell)
    last = getLast(history)
    # env = dict(os.environ)
    # env.update(settings.env)
    output = Popen(last, shell=True, stdin=PIPE,
                        stdout=PIPE, stderr=STDOUT)
    return output.stdout.read().decode('utf-8')