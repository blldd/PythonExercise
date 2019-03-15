# -*- coding:UTF-8 -*-
import re
from collections import defaultdict

import operator


class Solution(object):
    def lengthOfLongestSubstr(self, s):
        used = {}
        maxl = left = 0
        # 判断传入的字符串是否为空
        if s is None or len(s) == 0:
            return maxl
        for ind, w in enumerate(s):
            if w in used and left <= used[w]:
                left = used[w] + 1
            else:
                maxl = max(maxl, ind - left + 1)
            used[w] = ind
        return maxl

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list_len = len(strs)
        if list_len < 1:
            return ""
        if list_len == 1:
            return strs[0]
        len_list = [len(i) for i in strs]
        min_len = min(len_list)
        if min_len < 1:
            return ""
        for j in range(min_len):
            for i in range(list_len):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0][:j+1]

    """
    使用hashmap的方式
    """

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        map_dict1 = defaultdict(int);
        map_dict2 = defaultdict(int);
        for i in s1:
            map_dict1[i] += 1
        for i in range(len(s2) - len(s1) + 1):
            for j in range(len(s1)):
                map_dict2[s2[i + j]] += 1
            if operator.eq(map_dict1, map_dict2):
                return True
            map_dict2.clear()
        return False

    def str_permutation(self, s=''):
        if len(s) <= 1:
            return [s]
        str_list = []
        for i in range(len(s)):
            for j in self.str_permutation(s[0:i] + s[i + 1:]):
                str_list.append(s[i] + j)
        return str_list

    """
    滑动窗口法，时间复杂度O(l1+26∗(l2−l1),l1是s1的长度,l2是s2的长度
    """

    def match(self, s1, s2):
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True

    def checkInclusion1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s2) - len(s1)):
            if self.match(list1, list2):
                return True
            list2[ord(s2[i + len(s1)]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] -= 1
        return self.match(list1, list2)

    """
    进阶的滑动窗口法,使用count来表示26个字符频率在s1,s2中相同个数
    """
    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if list1[i] == list2[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')
            if count == 26:
                return True
            list2[r] += 1
            if list2[r] == list1[r]:
                count += 1
            elif list2[r] == list1[r] + 1:
                count -= 1
            list2[l] -= 1
            if list2[l] == list1[l]:
                count += 1
            elif list2[l] == list1[l] - 1:
                count -= 1
        return count == 26

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        str_list = [0 for _ in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                str_list[i+j] += (int(num1[i])*int(num2[j]))

        result = ""
        up = 0
        for i in str_list:
            now = i + up
            cur = now % 10
            up = now // 10
            result += str(cur)

        begin = 0
        result = result[::-1]
        for i in result:
            if i == "0":
                begin += 1
            else:
                break
        return result[begin:]

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return " ".join(words[::-1])

    """
    给定一个文档 (Unix-style) 的完全路径，请进行路径简化。
    例如，
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"
    
    边界情况:
    你是否考虑了 路径 = "/../" 的情况？
    在这种情况下，你需返回 "/" 。
    此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
    在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
    """
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_li = path.split("/")
        stack = []
        new_path = ""
        for item in path_li:
            if item not in ["",".",".."]:
                stack.append(item)
            if ".." == item and stack:
                stack.pop(-1)

        if []==stack:
            return "/"
        for item in stack:
            new_path += "/"+item + ""
        return new_path

    """
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    示例:
    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]
    """
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ip_list = []
        self.dfs(s, [], ip_list)
        return ip_list

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.lengthOfLongestSubstr("abcabcbb"))
    # print(sol.lengthOfLongestSubstr("bbbbb"))
    # print(sol.lengthOfLongestSubstr("eeydgwdykpv"))
    # print(sol.lengthOfLongestSubstr("pwwkew"))
    # print(sol.lengthOfLongestSubstr("abcabcbb"))

    # print(sol.longestCommonPrefix(["c","c"]))

    # s1 = "abcdxabcde"
    # s2 = "abcdeaaabcdxhesd"
    # print(sol.checkInclusion1(s1, s2))
    # num1 = "9"
    # num2 = "9"
    # print(sol.multiply(num1, num2))

    # s = "  the  sky is   blue"
    # print(sol.reverseWords(s))

    # path = "///"
    # print(sol.simplifyPath(path))

    ip = "25525511135"
    # print(sol.restoreIpAddresses(ip))

    print(Solution().str_permutation("abc"))