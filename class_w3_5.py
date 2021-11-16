# Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the
# same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4


# the solution from the previous exercise is imported.
# This returns all the combinations that can be made with the list

from class_w3_4 import Script_4


class Script_5():

    def match_sum(self, num, input_list):
        comb = Script_4().subsets(input_list)

        result = []

        # all combinations are tested looking for a target match
        for i in comb:

            if sum(i) == num:

                result.append(i)

        return result


if __name__ == "__main__":

    listin = [10,  20,  10, 40, 50, 60, 70]
    print(Script_5().match_sum(50, listin))
