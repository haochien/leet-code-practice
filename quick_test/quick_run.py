
def test_run(nums):
    l, r = 0, 1

    k = 1
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            k += 1
            nums[l] = nums[r]
  

        r += 1

    print(nums)
    return k

if __name__ == '__main__':
    result = test_run([0,0,1,1,1,2,2,3,3,4])
    print(f"result: {result}")