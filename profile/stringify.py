# def py2func ():
#     return 0

# def pyfunc():
#     pyvar = p2func()

from ctypes import cast, c_char, c_ubyte, POINTER, Structure, Union


class ba (Structure):
    _fields_ = [("s", c_ubyte * 4)]


class ca (Structure):
    _fields_ = [("s", c_char * 4)]


class Ua (Union):
    _fields_ = [("ba", ba),
                ("ca", ca)]

fp = ba()
up = Ua()
d = { '\x00\x00\x00\x00': 1 }


def mycast ():
    return d[cast(fp.s, POINTER(c_char * 4)).contents.raw]


def mycoerce ():
    return d[str(bytearray(fp.s))]

def mytobytes ():
    return d[memoryview(fp.s).tobytes()]


def myjoin ():
    return d[str(buffer(fp.s, 0, 4))]


def myjoin2 ():
    return d[str(buffer(fp.s))]


def myjoin3 ():
    return d[bytes(buffer(fp.s))]


def myjoin4 ():
    return d[buffer(fp.s).__str__()]


def myunion ():
    return d[up.ca.s]


def df (mybuf):
    mybuf.__str__()
    str(mybuf)


def mybaseline ():
    return d['\x00\x00\x00\x00']

if __name__ == '__main__':
    import timeit
    count = 1000000
    print("cast->contents->raw: {}".format(timeit.timeit("mycast()", number=count, setup="from __main__ import mycast")))
    print("Bytearray->str: {}".format(timeit.timeit("mycoerce()", number=count, setup="from __main__ import mycoerce")))
    print("mem->tobytes: {}".format(timeit.timeit("mytobytes()", number=count, setup="from __main__ import mytobytes")))
    print("Bufferslice->str: {}".format(timeit.timeit("myjoin()", number=count, setup="from __main__ import myjoin")))
    print("Buffer->str {}".format(timeit.timeit("myjoin2()", number=count, setup="from __main__ import myjoin2")))
    print("Buffer->bytes {}".format(timeit.timeit("myjoin3()", number=count, setup="from __main__ import myjoin3")))
    print("Buffer.__str__ {}".format(timeit.timeit("myjoin4()", number=count, setup="from __main__ import myjoin4")))
    # print(timeit.timeit("myunion()", number=100000, setup="from __main__ import myunion"))
    print("Direct Index: {}".format(timeit.timeit("mybaseline()", number=100000, setup="from __main__ import mybaseline")))

    import pdb
    pdb.set_trace()
    mybuf = buffer(fp.s)
