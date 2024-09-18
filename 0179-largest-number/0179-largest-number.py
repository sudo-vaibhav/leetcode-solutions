class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)