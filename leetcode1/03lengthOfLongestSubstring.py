class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        :param s:
        :return:
        """
        length = len(s)
        if length < 1:
            return 0

        char_idx_dict = {}
        res = 0
        last = 0
        for idx, i in enumerate(s):
            if i in char_idx_dict:
                last = max(char_idx_dict[i], last)
            res = max(res, idx - last)
            char_idx_dict[i] = idx
        return res

if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
