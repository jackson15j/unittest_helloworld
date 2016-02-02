# -*- coding: utf-8 -*-
"""
Monkey Patching style test
==========================

TODO
To unittest our `hello_world.py`, we need to make a change to our functional
code so that it will be testable. We don't want to mess around trying to test
the `print()` function since we can assume that as the first function that
everyone uses in python, it has the most manual testing in the world (and
hopefully a good batch of unittests in it's own right).

So lets break the problem down:

* I want to print `"Hello World"`.

Now the testing question can be worded as:

* I want to test that `"Hello World"` is printed to stdout.
* I want to test that `"Hello World"` will be printed to stdout.

The second statement is the key here. We are trusting that `print()` will print
an appropriate string (integer, list, whatever) to stdout. If we believe that
the `print()` function will just "do it's job", then we can focus on:

* Am I passing the string: "Hello World", to `print()`.

Subtle, but this change in wording allows us to bring focus on what needs
unittesting, as well as hints on how to change the functional code.

The lest effort change to make the code testable, is to break out: `"Hello
World"`, to a global string, then import our `hello_world.py` file into our
unittest file.

Benefits:
---------

* No code changes to our program.
* Monkey Patching is cool!
* Actually a unittest.

Drawbacks:
----------

* We Monkey Patched `sys.stdout`! (Breaks all `print()` calls (uses `sys.stdout`) in our program 
TODO
* Had to change code to be testable (easy refactor in this case but may not be
  trivial).

To run:
-------

```bash
python3 test_monkey_patching_style.py
```

We should not see the assert exception if this is working.

Assumptions:
------------
TODO
Like the other tests, this is a very quick & least effort way of
unittesting. Here are the assumptions we made for a "good enough" unittest:

* Moving `"hello world"` to a global means that we get the `print()` occurring
  as an import side-effect (Not ideal and generally bad form). Like Monkey
  Patching; if you need import side-effects in your module, make sure you
  **really** need import side-effects.
* Placing trust in `print()` functionality if we abide by it's API contract and
  assuming it has been sufficiently tested by it's maintainer/provider.
* Not using the unittest framework, so cannot run with nosetests.

The key assumption here is that we trust people to maintain their own realm so
that we can both test a portion of our internal logic in isolation, as well as
the border to handing responsibility over to another function/module/party.

However, without an integration test we may find out that `print()` is broken
(does not print to stdout) despite what we are passing in is correct and all of
our unittests are passing.

"""
import sys
import io

default_stdout = sys.stdout
stdout_variable = io.StringIO()
sys.stdout = stdout_variable
from basic_hello_world import hello_world
sys.stdout = default_stdout

print('We\'ve swallowed the print from the import to check in our assert...')
assert("hello world" in stdout_variable.getvalue())
print('It appears my Monkey Patched assert passed.')
