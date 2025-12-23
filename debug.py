import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        logging.debug(f"Input list: {nums}")

        closest = nums[0]
        logging.debug(f"Initial closest set to: {closest}")

        for x in nums:
            logging.debug(f"Checking number: {x}")
            logging.debug(f"abs({x}) = {abs(x)}, abs({closest}) = {abs(closest)}")

            if abs(x) < abs(closest):
                logging.debug(f"{x} is closer to zero than {closest}. Updating closest.")
                closest = x
        
        logging.debug(f"Closest after loop: {closest}")

        if closest < 0 and abs(closest) in nums:
            logging.debug(f"Negative closest found with positive counterpart. Returning {abs(closest)}")
            return abs(closest)
        else:
            logging.debug(f"Returning closest: {closest}")
            return closest


# Sample values for testing
solution = Solution()

print("Result for [4, -1, -3, 2, 1]:", solution.findClosestNumber([4, -1, -3, 2, 1]))

print("I love Git")

print("Hi Suresh")