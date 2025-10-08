from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_len = len(words) * word_len
    word_count = Counter(words)
    
    result = []
    
    for i in range(word_len):
        left = i
        right = i
        seen = Counter()
        
        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len
            
            if word in word_count:
                seen[word] += 1
                
                while seen[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                
                if right - left == total_len:
                    result.append(left)
            
            else:
                seen.clear()
                left = right
    
    return result

print(findSubstring("dogcatcatcodecatdog", ["cat", "dog"]))  # [0, 13]
print(findSubstring("barfoobazbitbyte", ["dog", "cat"]))      # []
