#!/usr/bin/make -f

# enable or disable tests here:
TESTS := test1 test2 test3 test4 test5 test6

all: $(TESTS)

test%:
	make -C t$* run
	make -C t$* check

clean-test%:
	make -C t$* clean

clean: $(TESTS:%=clean-%)
	rm -f *\.dsc *\.tar\.gz *\.build *\.changes *\.deb
	@find . -prune -name '*.egg-info' -exec rm -rf '{}' ';' || true

.PHONY: clean
