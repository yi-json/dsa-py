# Collections

## SortedList

```python
from sortedcontainers import SortedList
sl = SortedList()   # SortedList(key=...) for custom order
```

All ops ~O(log n). Slicing is O(log n + k).

| Op | Does |
|---|---|
| `sl.add(x)` / `sl.update(it)` | insert |
| `sl.remove(x)` | delete, raises if missing |
| `sl.discard(x)` | delete, no error |
| `sl.pop(i=-1)` | remove by index |
| `sl[i]`, `sl[i:j]` | by position (`sl[0]` min, `sl[-1]` max) |
| `x in sl`, `sl.count(x)`, `sl.index(x)` | by value |
| `sl.bisect_left(x)` | first index with value ≥ x |
| `sl.bisect_right(x)` | first index with value > x |
| `sl.irange(lo, hi)` | iterate values in [lo, hi] |

No `append`, `insert`, or `sl[i] = x`. To update, `remove(old)` then `add(new)`.

## Patterns

```python
sl[len(sl) // 2]                          # median
i = sl.bisect_left(t); sl[i:i + k]        # k smallest >= t
i = sl.bisect_left((t, -1))               # assuming sl is a tuple like (val, id)
sl.bisect_right(hi) - sl.bisect_left(lo)  # count in [lo, hi]
```