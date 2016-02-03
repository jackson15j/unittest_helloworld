# -*- coding: utf-8 -*-
"""
Monkey Patching style test
==========================

How can we actually unittest our code without changing our program? After all,
the`hello_world.py` program has been ground down to its most efficient form, so
why add complexity to make it testable?

Putting on our "Dev" brain; we want to get inside the `print()` function and
find out what it is going to print. Then we can see if what it is going to
print is `"Hello World"` or not. So lets
[Monkey Patch](https://stackoverflow.com/questions/5626193/what-is-a-monkey-patch)
`print()`!

In reality it is easier to Monkey Patch `sys.stdout`, which `print()` is using
(`print()` calls `sys.stdout.write()`). As long as we patch it with a file-like
object we are golden. Do note that this will capture all `print()` calls until
we undo the Monkey Patch. It will also cyclically blow up if you try this in an
interpreter, but hey, no code changes to our main program at least.

Benefits:
---------

* No code changes to our program.
* Monkey Patching is cool!
* Actually a unittest.

Drawbacks:
----------

* We Monkey Patched `sys.stdout`! (Breaks all `print()` calls (uses
  `sys.stdout`) in our program until we undo the patching.
* Do you **really** need to do Monkey Patching? It's trivial here, but can be
  quite gnarly when the code gets more complex.
* Is there a better way to make the program more testable?

To run:
-------

```bash
python3 test_monkey_patching_style.py
```

We should not see the assert exception if this is working.

Assumptions:
------------

Like the other tests, this is a very quick & least effort way of
unittesting. Here are the assumptions we made for a "good enough" unittest:

* Monkey Patching `sys.stdout` is a bit heavy handed as we swallow all calls to
  it until the patching is undone. It also cyclically errors in interpreters.
* We're only patching `sys.stdout` because we've investigated how `print()` is
  implemented, to figure out how to mock it's behaviour to our needs. If the
  internal structure of `print()` changes, our test will break.
* The above two points show both big sweeping changes to Third Party code
  behaviour and investigation effort into code outside of our programs realm.
* From the design we are relying on import side-effects to execute the
  `print()` function.
* We step over any potential other `print()` calls by using `in` when checking
  for `"Hello World"`.
* Not using the unittest framework, so cannot run with nosetests.

The key assumption here is that we are doing something technically impressive
to not change our existing code. However, we are digging into the bowls of a
Third Party code base to meet our needs. At least it is a unittest though.
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
