class Solution {
public:
    bool hasAllCodes(string s, int k) {
        set<string> seen;
        int n = s.size();
        string window = "";
        for (int i = 0; i < n; i++)
        {
            window += string(1, s[i]);
            if (window.size() == k)
            {
                seen.insert(window);
            }
            if (i >= k - 1)
            {
                window.erase(window.begin());
            }
        }

        return seen.size() == pow(2, k);
    }
};