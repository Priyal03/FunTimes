class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask =0
        for x in nums:
            bitmask ^= x
        #rightmost one bit difference between x and y
        twonums = bitmask & (-bitmask)

        y=0
        for x in nums:
            #bitmast which will only contain y
            if x & twonums:
                y ^= x

        return [bitmask^y, y]

        #please revisit this dear.. 