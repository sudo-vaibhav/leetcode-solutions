class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Stack-like list to store cumulative sums and their indices
        cumulative_sum_stack = [(0, -1)]

        running_cumulative_sum = 0
        shortest_subarray_length = float("inf")

        for i in range(n):
            # Update cumulative sum
            running_cumulative_sum += nums[i]

            # Remove entries from stack that are larger than current cumulative sum
            while (
                cumulative_sum_stack
                and running_cumulative_sum <= cumulative_sum_stack[-1][0]
            ):
                cumulative_sum_stack.pop()

            # Add current cumulative sum and index to stack
            cumulative_sum_stack.append((running_cumulative_sum, i))

            candidate_index = self._find_candidate_index(
                cumulative_sum_stack, running_cumulative_sum - k
            )

            # If a valid candidate is found, update the shortest subarray length
            if candidate_index != -1:
                shortest_subarray_length = min(
                    shortest_subarray_length,
                    i - cumulative_sum_stack[candidate_index][1],
                )

        # Return -1 if no valid subarray found
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )

    # Binary search to find the largest index where cumulative sum is <= target
    def _find_candidate_index(
        self, nums: List[Tuple[int, int]], target: int
    ) -> int:
        # temp = bise÷
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right