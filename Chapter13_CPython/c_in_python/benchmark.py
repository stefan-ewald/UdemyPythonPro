'''Test code.
'''
from timeit import Timer

import numpy as np

l1 = [i for i in range(1_000_000)]
l2 = [-i for i in range(1_000_000)]
a = np.array([i for i in range(1_000_000)])
b = np.array([-i for i in range(1_000_000)])
num_runs = 100

import_string = (
    '''
from __main__ import l1, l2, a, b
import add
import numpy as np
'''
)

python_timer = Timer(
    'l3 = [l1[i] + l2[i] for i in range(len(l1))]',
    setup=import_string
)

python_timer2 = Timer(
    '''\
l3 = []
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
''',
    setup=import_string
)

np_timer = Timer(
    'c = a + b',
    setup=import_string
)

c_timer = Timer(
    'l3 = add.add(l1, l2)',
    setup=import_string
)

c_timer2 = Timer(
    'l4 = add.clip(l1, 0.0, 10.0)',
    setup=import_string
)


def main() -> None:
    python_mean_time = np.mean(python_timer.repeat(repeat=num_runs, number=1))
    python2_mean_time = np.mean(python_timer2.repeat(repeat=num_runs, number=1))
    np_mean_time = np.mean(np_timer.repeat(repeat=num_runs, number=1))
    c_mean_time = np.mean(np_timer.repeat(repeat=num_runs, number=1))
    c_mean_time2 = np.mean(np_timer.repeat(repeat=num_runs, number=1))
    print(f'python add: {python_mean_time * 1_000.0}')
    print(f'python2 add: {python2_mean_time * 1_000.0}')
    print(f'np.add: {np_mean_time * 1_000.0}')
    print(f'cpython add: {c_mean_time * 1_000.0}')
    print(f'cpython clip: {c_mean_time2 * 1_000.0}')


if __name__ == '__main__':
    main()
