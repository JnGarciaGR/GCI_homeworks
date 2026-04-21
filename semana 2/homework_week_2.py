import numpy as np
a = np.array([1, 5, 10, 3, 4, 25, 30])

def homework(array_1: np.ndarray) -> np.ndarray:
    result = []
    for i in array_1:
        if (i % 5 == 0) and (i % 2 == 1):
            result.append(i)
    return np.array(result)

result = homework(a)
print(result)
