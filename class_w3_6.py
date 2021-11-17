# Write a Python class to find the three elements that sum to zero from a set
# of n real numbers. Go to the editor
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

from class_w3_4 import Script_4


class Script_5():

    def sum_zero(self, input_list):

        operation = Script_4()
        combinations = operation.subsets(input_list)
        result = []

        for comb in combinations:
            if sum(comb) == 0:
                result.append(comb)

        return result


if __name__ == "__main__":
    result_1 = Script_5()
    print(result_1.sum_zero([-25, -10, -7, -3, 2, 4, 8, 10]))
