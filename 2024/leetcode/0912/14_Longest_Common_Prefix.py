from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key=len)
        prefix = ""
        for i in range(len(min_str)):
            for j in range(len(strs)):
                if min_str[i] != strs[j][i]:
                    return prefix
            prefix += min_str[i]
        return prefix


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 문자열을 Trie에 삽입
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # 공통 접두사 찾기
    def longest_common_prefix(self) -> str:
        prefix = []
        node = self.root
        while node:
            # 자식 노드가 1개일 때만 계속 탐색
            if len(node.children) == 1 and not node.is_end:
                char = list(node.children.keys())[0]
                prefix.append(char)
                node = node.children[char]
            else:
                break
        return "".join(prefix)


class GPTSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = Trie()
        # 모든 문자열을 Trie에 삽입
        for word in strs:
            trie.insert(word)

        # 공통 접두사 반환
        return trie.longest_common_prefix()


Solution().longestCommonPrefix(["a"])

# GPT는 Trie 자료 구조 활용했음 어렵네 이거 이해를 잘 못하겠는데
