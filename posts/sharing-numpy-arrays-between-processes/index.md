<html><body><p>This is a little trick that may be useful to people using multiprocessing and numpy that I couldn't find any good examples of online.

Using the Python multiprocessing package you create a new Python process for each CPU in the system, but you may often want to work on the same data without making a copy. Here is one way to do that. First of all, we assume you're starting with a large numpy array S. We replace S with a version in shared memory, and then we can pass this

[python]
from multiprocessing import sharedctypes
size = S.size
shape = S.shape
S.shape = size
S_ctypes = sharedctypes.RawArray('d', S)
S = numpy.frombuffer(S_ctypes, dtype=numpy.float64, count=size)
S.shape = shape
[/python]

Now we can send S_ctypes and shape to a child process in multiprocessing, and convert it back to a numpy array in the child process as follows:

[python]
from numpy import ctypeslib
S = ctypeslib.as_array(S_ctypes)
S.shape = shape
[/python] </p></body></html>