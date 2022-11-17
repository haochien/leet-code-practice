from typing import List

def test_run(strs: List[str]) -> str:
    result = ''
    for letter_set in zip(*strs):
        if len(set(letter_set)) == 1:
            result += letter_set[0]
        else:
            break

    return result


if __name__ == '__main__':
    result = test_run(["flower","flow","flight"])
    print(f"result: {result}")