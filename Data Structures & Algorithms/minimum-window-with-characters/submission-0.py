class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        window = {}

        required = len(count_t)
        formed = 0

        left = 0
        min_length = float("inf")
        result_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # This character now has the required frequency
            if char in count_t and window[char] == count_t[char]:
                formed += 1

            # Shrink the window while it remains valid
            while formed == required:
                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    result_start = left

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in count_t
                    and window[left_char] < count_t[left_char]
                ):
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[result_start:result_start + min_length]