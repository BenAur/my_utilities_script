import os
import fileinput
import sys
import re

path = "some/path"
for root, dirs, files in os.walk(path):
        for name in files:
                for i, line in enumerate(fileinput.input(os.path.join(root, name), inplace=1)):
                        line = line.replace('</doc>','')
                        line = re.sub("^<doc.*>$",'', line)
                        sys.stdout.write(line)
