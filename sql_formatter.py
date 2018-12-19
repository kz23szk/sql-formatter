#!/Users/kzfm/.pyenv/shims/python

import sys

output = []

while True: 
    line = sys.stdin.readline()
    if line:
        output.append(line.rstrip())
    else:
        break

for line in output:
    print(line)
