#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 30.串联所有单词的子串-困难.py
Created Time: 2024/8/14 22:23
"""

"""
给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

 s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。


示例 1：
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。

示例 2：
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。

示例 3：
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
 

提示：

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 和 s 由小写英文字母组成

"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l_word = len(words[0])
        l_words = len(words)
        l_s = len(s)
        ans = []
        if l_s < l_word:
            return ans

        strandard_dic = {}
        for word in words:
            if word in strandard_dic:
                strandard_dic[word] += 1
            else:
                strandard_dic[word] = 1

        for i in range(l_word):
            star = i
            j = i
            count = 0
            count_dic = {}
            while j + l_word <= l_s:
                temp_word = s[j:j + l_word]
                if temp_word in strandard_dic:
                    count += 1
                    if temp_word not in count_dic:
                        count_dic[temp_word] = 1
                    else:
                        count_dic[temp_word] += 1
                    while count_dic[temp_word] > strandard_dic[temp_word]:
                        temp_wordV2 = s[star:star + l_word]
                        star += l_word
                        count -= 1
                        count_dic[temp_wordV2] -= 1
                    if count == l_words:
                        ans.append(star)
                        temp_wordV2 = s[star:star + l_word]
                        count_dic[temp_wordV2] -= 1
                        count -= 1
                        star += l_word

                    j += l_word
                else:
                    star = j + l_word
                    j = star
                    count = 0
                    count_dic.clear()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))