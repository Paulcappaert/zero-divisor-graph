import timeit as ti

t1 = ti.timeit(
'semigroups = graph.semigroups()',
setup = '''
from zdg.zdg import ZeroDivisorGraph as ZDG
graph = ZDG(
(1, 2),
(2, 3),
(3, 4),
(4, 1),
(4, 5)
)
''',
number=1
)

print(f'5 vertex graph took {t1} seconds')

t2 = ti.timeit(
'semigroups = graph.semigroups()',
setup = '''
from zdg.zdg import ZeroDivisorGraph as ZDG
graph = ZDG(
('a1','x1'),
('a2','x2'),
('a3','x3'),
('a4','x4'),
('x1','x2'),
('x1','x3'),
('x1','x4'),
('x2','x3'),
('x2','x4'),
('x3','x4'),
('y1','c1'),
('y1','x1'),
('y1','x2'),
('c1','x3'),
('c1','x4'),
('y2','c2'),
('y2','x1'),
('y2','x4'),
('c2','x2'),
('c2','x3'),
('y3','c3'),
('y3','x1'),
('y3','x3'),
('c3','x2'),
('c3','x4'),
)
''',
number=1
)

print(f'14 vertex graph took {t2} seconds')
