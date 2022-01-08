from subprocess import Popen, PIPE
import os

output = b''
i = 0
while not b'Secret message' in output:
    cmd = f'./program_flow {i+2} \x89\x11 '
    print(f'Payload: {cmd}')
    p = Popen(cmd.split(" "), stdout=PIPE)
    output = p.stdout.readline()
    print("output: ", output)
    i += 1
    break

