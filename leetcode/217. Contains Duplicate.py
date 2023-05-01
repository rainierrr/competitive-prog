class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict.keys():
                return True

            num_dict[num] = True

        return False
