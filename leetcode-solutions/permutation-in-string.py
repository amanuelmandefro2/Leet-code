class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s1_len = len(s1)
        s2_up = s2[:s1_len]
        s2_freq = defaultdict(int)
        for char in s2_up:
            s2_freq[char] += 1

        if s1_freq == s2_freq:
                return True    
        
        for i in range(s1_len, len(s2)):
            if s2_freq[s2[i-s1_len]] > 1:
                s2_freq[s2[i-s1_len]] -= 1
            else:
                del s2_freq[s2[i - s1_len]] 

            s2_freq[s2[i]] += 1  
            if s1_freq == s2_freq:
                return True                  

        return False
        