#! /usr/bin/dev python
class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        youvalue = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            if abs(x - target[0]) + abs(y - target[1]) <= youvalue:
                return False
    # all() 参数是一个 iterable
        l = [1,2,3]
        all(x for x in range(20))
    def main(self):
        l = [1,2,3]
        return all(x for x in l)

if __name__ == '__main__':
    solution = Solution()
    print(solution.main())