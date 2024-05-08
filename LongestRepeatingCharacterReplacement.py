#Longest Repeating Character Replacement

#Brute force approach
#Time: O(N*N), Space: O(N)
def characterReplacement(s, k):
    result = 0
        
    for l in range(len(s)):
        count = {}
        for r in range(l, len(s)):
            
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count.values())
            
            if r - l + 1 - maxf <= k:
                result = max(result, r - l + 1)
                
    return result


#Two pointer and sliding window approch
#Time: O(26*N), Space: O(1)
def characterReplacement(s, k):
    count = {}
    result = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)
    
    return result

#Two pointer and sliding window with more optimization
#Time: O(N), Space: O(1)
def characterReplacement(s, k):
    count = {}
    result = 0
    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        
        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)
    
    return result