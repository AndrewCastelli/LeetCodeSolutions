def lengthOfLongestSubstring(s: str) -> int:
    last = {}
    biggest = 0
    start = 0

    for i in range(0, len(s)):
        if s[i] in last:
            start = max(start, last[s[i]] + 1)

        biggest = max(biggest, i - start + 1)

        last[s[i]] = i

    return biggest
