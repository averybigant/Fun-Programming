# This Python script finds recursively all
# Processing and SuperCollider programs
# under the current directory that have
# been added to Git, then saves the
# resulting list to the file "readme.md",
# which GitHub uses as a read me file.

import os, os.path, subprocess

execstr = "git ls-files ./ | grep -E '.pde|.scd'"
result = subprocess.check_output(execstr, shell=True).split('\n')

absolutePath = 'https://github.com/hamoid/Fun-Programming/blob/master/processing'

f = open('readme.md', "w")
for line in result:
  if line:
    f.write('[%s](%s/%s)  \n' % (os.path.basename(line), absolutePath, line))
f.close()

