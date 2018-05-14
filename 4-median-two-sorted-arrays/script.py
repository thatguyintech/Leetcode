class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)

        if n == 0:
            middle = m // 2
            return nums2[middle] if m % 2 == 1 else (nums2[middle] + nums2[middle - 1]) / 2.0

        if m == 0:
            middle = n // 2
            return nums1[middle] if n % 2 == 1 else (nums1[middle] + nums1[middle - 1]) / 2.0

        if m > n:
            nums1, n, nums2, m = nums2, m, nums1, n

        low, high = 0, n

        while low <= high:
            i = (low + high) // 2
            j = (n + m + 1) // 2 - i

            if j < 0 or i > n:
                high = i - 1
            elif i < 0 or j > m:
                low = i + 1
            elif (i == 0 or j == m or nums1[i-1] <= nums2[j]) and (j == 0 or i == n or nums2[j-1] <= nums1[i]):
                if (n + m) % 2 == 0:
                    if i == 0:
                        left = nums2[j-1]
                    elif j == 0:
                        left = nums1[i-1]
                    else:
                        left = max(nums1[i-1], nums2[j-1])
                    if i == n:
                        right = nums2[j]
                    elif j == m:
                        right = nums1[i]
                    else:
                        right = min(nums1[i], nums2[j])
                    return (left + right) / 2.0
                else:
                    if i == 0:
                        return nums2[j-1]
                    elif j == 0:
                        return nums1[i-1]
                    else:
                        return max(nums1[i-1], nums2[j-1])
            elif i > 0 and j < m and nums1[i-1] > nums2[j]:
                high = i - 1
            else:
                low = i + 1

def tests():
    cases = [
        ([1,2], [3,4], 2.5),
        ([1], [2,3], 2.0),
        ([1,3,5,7,9,11], [0,2,4,4,4,12], 4),
        ([1,3,5,7,9,11], [0,2,4,4,4,4,12], 4),
        ([], [1], 1),
        ([1], [], 1),
        ([1, 3], [2], 2.0),
        ([3], [1, 2], 2.0),
        ([5], [1,2,3,4,6], 3.5),
        ([1, 2], [3, 4, 5, 6], 3.5)
    ]

    s = Solution()

    for case in cases:
        nums1, nums2, expected = case
        answer = s.findMedianSortedArrays(nums1, nums2)
        assert answer == expected, "\nnums1: {}\nnums2: {}\nexpected: {}\nactual: {}".format(nums1, nums2, expected, answer)

if __name__ == "__main__":
    print("running tests...")
    tests()
    print("all tests passed")
