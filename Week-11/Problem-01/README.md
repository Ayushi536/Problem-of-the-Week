# 🧩 Problem of the Week – Dropbox Question  
**Company:** Dropbox  
**Difficulty:** Hard  
**Topics:** Hashing • Sliding Window • String Matching • Two Pointers  

---

## 📖 Problem Description
You are given a string `s` and a list of words `words`, where each word has the same length.  
Find all starting indices in `s` where the substring is a **concatenation of every word in `words` exactly once** (no extra characters).  
If no such substring exists, return an empty list.

---

## 🧠 Example
**Input**
s = "dogcatcatcodecatdog"
words = ["cat", "dog"]

**Output**
[0, 13]

Explanation :-

At index 0: "dogcat" → "dog" + "cat"
At index 13: "catdog" → "cat" + "dog"

⚙️ Approach

Each word has equal length k.

Use Sliding Window + Hash Map to check substrings of total length = len(words) * k.

Maintain frequency of words using Counter.

Slide the window in steps of k, track current word counts, and compare with the target count.

Time Complexity: O(N × wordLen × numWords)
Space Complexity: O(numWords)