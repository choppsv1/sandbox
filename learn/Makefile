#
# Copyright (c) 2014 by Christian E. Hopps.
# All rights reserved.
#
# REDISTRIBUTION IN ANY FORM PROHIBITED WITHOUT PRIOR WRITTEN
# CONSENT OF THE AUTHOR.
#

PYLINT3=/home/chopps/local/bin/pylint3
PYTEST3=/home/chopps/local/bin/py.test
PYTHON3=/home/chopps/local/bin/python3

PYLINT2=/home/chopps/venv/bin/pylint
PYTEST2=/home/chopps/venv/bin/py.test
PYTHON2=/home/chopps/venv/bin/python

test2-%:
	$(PYTEST2) --doctest-modules -v $*

test3-%:
	$(PYTEST3) --doctest-modules -v $*

doctest2-%:
	$(PYTHON2) $*

doctest3-%:
	$(PYTHON3) $*

lint2:
	@for f in $$(find . -name '*.py'); do \
		echo "=== Linting $$f"; \
		$(PYLINT2) -r n $$f; \
	done

lint3:
	@for f in $$(find . -name '*.py'); do \
		echo "=== Linting $$f"; \
		$(PYLINT3) -r n $$f; \
	done
