#!/usr/bin/make -f

all: run check

DPY=$(shell PYTHONPATH=../../ python -c 'import debpython.version as v; print(v.vrepr(v.DEFAULT))')

run: clean
	dpkg-buildpackage -b -us -uc

check:
	grep -q "pycompile -p python-foo /usr/lib/python-foo -V $(DPY)"\
		debian/python-foo/DEBIAN/postinst
	test -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/bar.so
	test ! -f debian/python-foo/usr/share/pyshared/foo/bar.so
	test -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/spam.so
	test ! -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/spam.so.0.1
	test -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/baz.so
	test ! -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/baz.so.0.1
	test ! -f debian/python-foo/usr/lib/python${DPY}/dist-packages/foo/baz.so.0.1.2

clean:
	./debian/rules clean
	rm -rf lib/Foo.egg-info build
