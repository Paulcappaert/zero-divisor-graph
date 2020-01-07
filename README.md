# Zero Divisor Graph math library

This is a pure python library for working with zero divisor graphs of commutative semigroups. The primary purpose is to automate the task of checking if a given graph is a zero divisor graph and for what possible semigroups.

# Installation

```
pip3 install zero-divisor-graph
```

You can also retrieve from source at https://github.com/Paulcappaert/zero-divisor-graph

# use

first start python3 in a terminal window and import the ZeroDivisorGraph object

```
python3
>>> from zdg.zdg import ZeroDivisorGraph as ZDG
```

You can create a zero divisor graph from edges as such. the vertices can be named whatever you want.

```
>>> example1 = ZDG((1, 2), (2, 3))
>>> example2 = ZDG(('a', 'b'), ('b', 'c'))
```

You can print all of the semigroups from a zero divisor graph as such

```
>>> semigroups = example1.semigroups()
>>> for s in semigroups:
...   print(s.caley_table())
```
