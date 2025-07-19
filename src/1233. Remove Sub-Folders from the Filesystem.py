from itertools import islice
from typing import List


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        result = [folders[0]]
        for folder in islice(folders, 1, None):
            if not folder.startswith(result[-1] + '/'):
                result.append(folder)

        return result


if __name__ == '__main__':
    print(Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))