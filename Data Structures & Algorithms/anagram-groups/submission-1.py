class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}  # dictionary
        for word in strs:
            key = ''.join(sorted(word))   #getting sorted word

            if key not in output:
                output[key] = []  #if key is not present in output ductionary then make a new key and value is list

            output[key].append(word)  #put the word as value for key

        return list(output.values())
