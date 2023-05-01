class Solution:
    def str_count(self, string):
        str_dict = {}
        for s in string:
            if s in str_dict.keys():
                str_dict[s] += 1
            else:
                str_dict[s] = 1

        return str_dict

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.str_count(s)
        t_dict = self.str_count(t)

        return s_dict == t_dict
