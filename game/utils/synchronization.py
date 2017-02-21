'''Simple emulation of Java's 'synchronized'
keyword, from Peter Norvig.'''
import threading

def synchronized(method):
    def f(*args):
        self = args[0]
        self.mutex.acquire();
        # print(method.__name__, 'acquired')
        try:
            #return apply(method, args)
            return method(*args)
        finally:
            self.mutex.release();
            # print(method.__name__, 'released')
    return f


def synchronize(klass, names=None):
    """Synchronize methods in the given class.
    Only synchronize the methods whose names are
    given, or all methods if names=None."""
    if type(names)==type(''): names = names.split()
    for (name, val) in klass.__dict__.items():
        if callable(val) and name != '__init__' and \
          (names == None or name in names):
            # print("synchronizing", name)
            #klass.__dict__[name] = synchronized(val)
            setattr(klass, name, synchronized(val))


"""
>>> class A:                 
    pass
... 
>>> A.__dict__['foo'] = 'bar'
Traceback (most recent call last):
  File "<ipython-input-117-92c06357349d>", line 1, in <module>
    A.__dict__['foo'] = 'bar'
TypeError: 'mappingproxy' object does not support item assignment

>>> setattr(A, 'foo', 'bar')
>>> A.foo
'bar'
"""



# You can create your own self.mutex, or inherit
# from this class:
class Synchronization:
    def __init__(self):
        self.mutex = threading.RLock()


class ToSynch:
    def __init__(self):
        self.mutex = threading.RLock()
        self.val = 1

    def aSynchronizedMethod(self):
        self.mutex.acquire()
        try:
            self.val += 1
            return self.val
        finally:
            self.mutex.release()