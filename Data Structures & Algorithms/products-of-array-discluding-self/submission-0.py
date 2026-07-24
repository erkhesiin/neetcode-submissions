class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [0] * length

        for i in range(length):
            # we want to some sort of parsing
            temp = list(nums)
            temp.pop(i)
            product = math.prod(temp)
            # append that product to i
            output[i] = product

        return output