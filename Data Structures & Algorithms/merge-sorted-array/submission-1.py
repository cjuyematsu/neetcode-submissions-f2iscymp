class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_place =  len(nums1) - 1
        p1 = m - 1    
        p2 = n - 1

        while p1 >= 0 or p2 >= 0:
            if p2 < 0:
                nums1[index_place] = nums1[p1]
                p1 -= 1
            elif p1 < 0:
                nums1[index_place] = nums2[p2]
                p2 -= 1           
            elif nums1[p1] >= nums2[p2]:
                nums1[index_place] = nums1[p1]
                p1 -= 1
            else: 
                nums1[index_place] = nums2[p2]
                p2 -= 1
            
            index_place -= 1

            print(f'p1: {p1}, p2: {p2}, nums1: {nums1}')
        