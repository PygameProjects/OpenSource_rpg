#! /usr/bin/python
# -*- coding: UTF-8 -*-
# Copyright © 2010 Piotr Ożarowski <piotr@debian.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
from subprocess import Popen, PIPE

skip_sensible_names = True if '--skip-sensible-names' in sys.argv else False
os.chdir(os.path.dirname(__file__))
if os.path.isdir('../debpython'):
    sys.path.append('..')
else:
    sys.path.append('/usr/share/python/debpython/')
from debpython.pydist import sensible_pname


if not os.path.isdir('cache'):
    process = Popen('apt-file -s sources.list -c cache update', shell=True)
    process.communicate()
    if process.returncode != 0:
        sys.stderr.write('Cannot download APT data files')
        exit(1)

# find .egg-info files/directories
process = Popen('apt-file -s sources.list -c cache find -x '
                '"/usr/((share/pyshared)|(lib/python2\.[0-9]/((site)|(dist))-packages)|(share/python-support/[^/]+))/[^/]*\.egg-info"',
                shell=True, stdout=PIPE)
stdout, stderr = process.communicate()
if process.returncode != 0:
    sys.stderr.write('Cannot find packages with Egg metadata')
    exit(2)

processed = set()
result = []
for line in stdout.splitlines():
    pname, path = line.split(': ', 1)
    if pname == 'python-setuptools':
        continue
    egg_name = [i.split('-', 1)[0] for i in path.split('/')\
                if i.endswith('.egg-info')][0]
    if egg_name.endswith('.egg'):
        egg_name = egg_name[:-4]
    if skip_sensible_names and sensible_pname(egg_name) == pname:
        continue
    if egg_name not in processed:
        processed.add(egg_name)
        result.append("%s %s\n" % (egg_name, pname))
        #result.append("%s %s\t%s\n" % (egg_name, pname, path))

result.sort()
fp = open('dist_fallback', 'w')
fp.write('python python\n')
fp.write('setuptools python-pkg-resources\n')
fp.write('wsgiref python (>= 2.5) | python-wsgiref\n')
fp.writelines(result)
