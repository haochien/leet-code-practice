from typing import List

def test_run(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i, v in enumerate(nums):
        search = target - v
        if search in hash_map:
            return [hash_map[search], i]
        
        hash_map[v] = i

    return


if __name__ == '__main__':
    result = test_run([2,7,11,15], 9)
    print(f"result: {result}")