
def test_run(nums1, m, nums2, n):
    curr = m + n
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        curr -= 1
        if nums1[m] >= nums2[n]:
            nums1[curr] = nums1[m]
            m -= 1
        else:
            nums1[curr] = nums2[n]
            n -= 1
        

    if m < n:
        nums1[:curr] = nums2[:n+1]

    print(nums1)
    return

if __name__ == '__main__':
    result = test_run(nums1 = [0], m = 0, nums2 = [1], n = 1)
    print(f"result: {result}")