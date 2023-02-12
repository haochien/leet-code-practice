
def test_run(n):
    if n <=2:
        return n
    
    res = [-1] * n
    res[0], res[1] = 1, 2

    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]

    return res[-1]

if __name__ == '__main__':
    result = test_run(4)
    print(f"result: {result}")