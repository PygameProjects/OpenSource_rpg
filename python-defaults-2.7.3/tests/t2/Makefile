#!/usr/bin/make -f

all: run check


run: clean
	dpkg-buildpackage -b -us -uc

check:
	test -f debian/python-foo/usr/lib/python2.6/dist-packages/foo.py
	test -f debian/python-foo/usr/lib/python2.6/dist-packages/bar/bar.py
	grep -q pycompile debian/python-foo/DEBIAN/postinst
	grep -q pyclean debian/python-foo/DEBIAN/prerm

clean:
	./debian/rules clean
