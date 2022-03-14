from collections import deque
from collections import OrderedDict

a = OrderedDict()
a['1'] = 'a'
a['2'] = 'b'
a['3'] = 'c'
a.move_to_end('2')


del(a['1'])

for k, v in (a.items()):
    print(k, v)
