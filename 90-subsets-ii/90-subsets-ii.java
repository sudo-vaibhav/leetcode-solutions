class Solution {
   List<List<Integer>> ans = new ArrayList<>();
    int[] nums;
    Stack<Integer> s = new Stack<>();

    void solve(int idx) {
        ans.add(new ArrayList<>(s));

        for (int i = idx; i < nums.length; i++) {
            if (idx < i && nums[i] == nums[i - 1])
                continue;
            s.push(nums[i]);
            solve(i + 1);
            s.pop();
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        this.nums = nums;
        solve(0);
        return ans;
    }
}