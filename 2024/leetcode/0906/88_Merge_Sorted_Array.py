from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = {}
        for i in nums1[:m]:
            nums[i] = nums.get(i, 0) + 1
        for i in nums2[:n]:
            nums[i] = nums.get(i, 0) + 1

        nums1.clear()
        for key, value in nums.items():
            nums1.extend([key] * value)
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums 딕셔너리를 nums1, nums2로 만들기 => 하나로 해서 나중에 List에 담으면 되겠네 ㅎㅎ
        # 정렬 해야 해


# gpt 방식은 무조건 입력으로 들어오는 리스트가 정렬이 되어있다는 전제하에 사용가능


class GPTSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 포인터 초기화
        i, j, k = m - 1, n - 1, m + n - 1

        # 두 리스트를 역순으로 비교하여 큰 값을 뒤에서부터 nums1에 넣습니다.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2에 남은 요소가 있다면 nums1에 복사합니다.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        # nums1에 남은 요소는 이미 정렬되어 있으므로 추가 작업 필요 없음


GPTSolution().merge([1, 3, 2, 0, 0, 0], 3, [2, 5, 6], 3)
