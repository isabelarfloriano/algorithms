def find_duplicate(nums):
    nums.sort()

    number, count = [False, 1]

    if len(nums) <= 1 or any(isinstance(n, str) for n in nums) is True:
        return False

    for index in range(1, len(nums)):
        cur_number = nums[index]

        if type(cur_number) != int or cur_number < 1:
            return False

        if cur_number == nums[index - 1]:
            number = cur_number
            count += 1

    return number
