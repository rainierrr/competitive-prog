class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in list('{:032b}'.format(n)) if i == '1'])
