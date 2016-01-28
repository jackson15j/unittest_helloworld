# -*- coding: utf-8 -*-
"""Integration style test.
=======================

Going to take the stdout output of running the basic hello_world.py file and
pipe it into this file. From this file we will read stdin and check that it is
the "Hello World" string.

Note: This is the equivalent of an integration test, where we treat the
original hello_world.py as a black box.

Benefits:
---------

* No code changes to our initial program.

Drawbacks:
----------

* Cannot test internal logic (only external access). Note: not an issue here
  with such a simple program, but doesn't scale up well if programs are not
  designed with deterministic external APIs.
* Suffers from system formatting (will we get a newline in the string? Unix/Dos
  newline?).
* Integration tests are by design more external, so may not keep lock-step with
  functional code changes (again, not an issue here with such a simple
  example).

To run:
-------

```{bash}
cd tests
../basic_hello_world/./hello_world.py | python3 test_integration_style.py
```

We should not see the assert exception if this is working.

Assumptions:
------------

This is a pretty quick and dirty way of reading in the input but it's good
enough for now. However, what assumptions have we made to get a "good enough"
integration test going:

* You need to pip in the hello_world.py script as above.
* The test does not read the hello_world.py script as a module, runs said
  module, capture the stdout, and reads it back in neatly.
* Doing a read() of the piped input so will block if no newline is seen.
* Not using the unittest framework, so cannot run with nosetests.
* Doing an "in" check to avoid OS specific newlines.
* No lowercase of input to make it case-insensitive (foolishly forgot to follow
  form and make my hello world print as "Hello World").

Now must of these assumptions are either minor or common sense, but the devil
is always in the detail. At least we have a fairly concise list of
assumptions/issues and risks.

"""
import sys

expected_input = 'hello world'
input = sys.stdin.read()
print(
    'I read in: {!r}, and expecting: {!r}, in the stdout'.format(
        input, expected_input))
assert(expected_input in input)
print('And it appears my Integration assert passed.')
