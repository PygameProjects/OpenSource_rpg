#!/usr/bin/make -f

all: run check

DPY=$(shell PYTHONPATH=../../ python -c 'import debpython.version as v; print(v.vrepr(v.DEFAULT))')

run: clean
	dpkg-buildpackage -b -us -uc

check:
	grep -q "Depends: .*python-mako" debian/python-foo/DEBIAN/control
	test -f debian/python-foo/usr/lib/python2.6/dist-packages/foo/__init__.py
	test ! -f debian/python-foo/usr/lib/python2.6/dist-packages/foo/spam.py
	grep -q "Depends: .*python (<<" debian/python-foo/DEBIAN/control
	[ `readlink debian/python-foo/usr/lib/python$(DPY)/dist-packages/foo/absolute_link_to_tmp` = /tmp ]
	[ `readlink debian/python-foo/usr/lib/python$(DPY)/dist-packages/foo/link_to_parent_dir` = .. ]

clean:
	./debian/rules clean
	rm -rf lib/Foo.egg-info
