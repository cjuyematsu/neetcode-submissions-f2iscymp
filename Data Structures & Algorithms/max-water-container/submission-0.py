class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxx = 0

        while(left < right):
            smaller_height = min(heights[left], heights[right])
            maxx = max(maxx, smaller_height * (right - left))

            if(smaller_height == heights[left]):
                left += 1
            else:
                right -= 1

        return maxx
