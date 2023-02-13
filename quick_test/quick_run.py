
def test_run(numbers, target):

    l, r = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

    return 

if __name__ == '__main__':
    result = test_run(numbers = [2,7,11,15], target = 9)
    print(f"result: {result}")