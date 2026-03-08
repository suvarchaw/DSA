class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()){
            return false;
        }

        unordered_map<char, int> string1;
        unordered_map<char, int> string2;
        for(int i=0; i<s.length(); i++){
            string1[s[i]]++;
            string2[t[i]]++;
        } return string1==string2;
    }
};