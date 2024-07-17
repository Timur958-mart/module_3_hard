data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
list_sum = 0

def calculate_structure_sum(*args):
    global list_sum
    for i in args:
        if isinstance(i, (int, float)):
            list_sum += i
        elif isinstance(i, str):
            list_sum += len(i)
        elif isinstance(i, (list, tuple)):
            if len(i) == 0:
                break
            else:
                for j in i:
                    calculate_structure_sum(j)
        elif isinstance(i, set):
            a = list(i)
            if len(a) == 0:
                break
            else:
                for x in i:
                    calculate_structure_sum(x)
        elif isinstance(i, dict):
            b = list(i.items())
            if len(b) == 0:
                break
            else:
                calculate_structure_sum(b)
    return list_sum


result = calculate_structure_sum(data_structure)
print(result)
