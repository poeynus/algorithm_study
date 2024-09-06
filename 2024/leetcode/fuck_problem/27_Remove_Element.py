class Solution:
    def removeElement(self, nums, val):
        change_data = 101
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt += 1
                nums[i] = change_data
        nums.sort()
        return cnt


class OtherSolution:
    def removeElement(self, nums, val):
        EMPTY = 101
        k = 0
        for index, num in enumerate(nums):
            if num == val:
                nums[index] = EMPTY
            else:
                k += 1
        nums.sort()
        return k


class GPTSolution:
    def removeElement(self, nums, val):
        # 두 포인터 사용
        k = 0  # k는 val이 아닌 요소를 저장할 위치

        for i in range(len(nums)):
            print(f"i {i} , nums {nums[i]}, k {k}")
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1  # val이 아닌 요소가 있으면 k를 증가시킴
        print(nums)
        return k


# local에서는 결과가 같은데, for range로 돌린건 사이트 컴파일러가 이상함, 댓글 보니 문제 이상해서 욕이 많음 진짜 개같네

GPTSolution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
