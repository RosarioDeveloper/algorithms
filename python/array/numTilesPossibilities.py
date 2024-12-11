import random


def numTilePossibilities(tiles: str) -> int:

    ans = set()
    size = len(tiles)

    for i in range(size):
        count = 0
        left = i + 1
        str = tiles[i]
        ans.add(str)

        while count < size - 1:
            str += tiles[left % size]
            ans.add(str)
            count += 1
            left +=1

    return len(ans)


res = numTilePossibilities("AAABBC")
print(res)
