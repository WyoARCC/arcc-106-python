# arcc-106-python
Introduction to Python for Scientific Computing

## Why Python
Python is a flexible high level programming language that supports
many different programming paradigms including procedural, object-
oriented, and functional giving the programmer many different options
in how to solve different problems. Several advantages that Python
has is that it is cross platform, meaning it works on Linux, OS X,
and Windows. 

### Implementations
Although Python is a language, there are several implementations
of the Language, however the most common is CPython where the base
of the language is written in the C programming language. There are
even many distributed versions of the CPython including the reference
implementation, Anaconda, and Enthought Python Distribution. For
scientific computing, ARCC recommends the use of the Anaconda Python
implementation because of the ease of use and capability. Anaconda
can be downloaded here: https://www.continuum.io/downloads

### Advantages
Python has gained massive attraction over the last decade. It's
easy to understand language is very beneficial for those scientist
who would like to concetrate on solving problems while minimizing
the need to understand quirks of lower level languages like C, C++,
and Fortran. One of Python's biggest advantages for the scientific 
community is that the implementations are Open Source. With Python
being open source and due to the large adoption of the language, many
scientist and developers have created additional libraries that are
easily usable generating building blocks to help many scientist
concentrate on solving the problems, not reinventing the wheel
so to speak.

### Disadvantages
Python is a nice high level language, however there are some issues
with the language. Although Python is a very easy to understand, the
performance can suffer when comparing to C, C++, Fortran. The other
inherent issue with the CPython implementation is the Global Interpreter
Lock, or GIL. The GIL is a mutex lock which prevents native python
threads from executing concurrently. This makes Python difficult 
to use for parallelism based on threads. Therefore different methods
must be used such as multiprocessing and MPI bindings into Python.

## Helpful Libraries
-    NumPy
-    SciPya
-    Pandas
-    Matplotlib
-    Numba
-    SymPy
-    mlpy
-    PyACTS

## Additional Resources
-    Anaconda Python: https://www.continuum.io/
-    SciPy Lectures: http://www.scipy-lectures.org/index.html
-    Software Carpentry: http://www.scipy-lectures.org/index.html
-    There are many O'Reilly books available.
-    Python Primer: https://hplgit.github.io/primer.html/doc/pub/half/book.pdf
-    Python for Computational Science and Engineering: http://www.southampton.ac.uk/~fangohr/training/python/pdfs/Python-for-Computational-Science-and-Engineering.pdf
