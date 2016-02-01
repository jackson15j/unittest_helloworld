Introduction
============

An attempt at writing a Hello World python program in it's most common
form. Then seeing how much the code changes as we try to unittest it.

The aim is to document the following styles of testing that most people would
do:

* Integration test (no code changes of functional code).
* Import and Monkey Patching `print()` (no code changes of functional code, +5
  dev "mad skills").
* Unittest (Modify functional code to be testable).

Please read the docstring in each test file for details of the following items
that concern that particular test mentality:

* Introduction on what that test is for and how it is written and why.
* Benefits/Drawbacks to that style of testing.
* Steps on how to run the test.
* Assumptions born from the proposed implementation.

As stated in the tests, these are quick hacks to get that style of testing with
the minimal changes. Ideally they would be progressed further to allow easier
automation and implementation into CI (Continuous Integration). But for now,
they are "good enough".
