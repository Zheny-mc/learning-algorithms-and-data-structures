from typing import List


def countTestedDevices(batteryPercentages: List[int]) -> int:
    count = 0
    for i in range(len(batteryPercentages)):
        if batteryPercentages[i] > count:
            count += 1
    return count




print(countTestedDevices([1,1,2,1,3]))
print(countTestedDevices([0,1,2]))