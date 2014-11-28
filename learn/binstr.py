#
# November 28 2014, Christian Hopps <chopps@gmail.com>
#
# Copyright (c) 2014 by Christian E. Hopps.
# All rights reserved.
#
# REDISTRIBUTION IN ANY FORM PROHIBITED WITHOUT PRIOR WRITTEN
# CONSENT OF THE AUTHOR.
import sys
print("PYTHON {}".format(sys.version_info))
if sys.version_info >= (3, 0):
    PY3 = True
else:
    PY3 = False


def test_binary_string ():
    """This is a doctest for binary strings
    >>> if PY3:
    ...  b"\\x01\\xFF" == bytearray([1, 0xff])
    ... else:
    ...  br"\\x01\\xFF" == "\\x01\\xFF"
    ...
    True
    """

if __name__ == "__main__1":
    import doctest
    doctest.testmod()
