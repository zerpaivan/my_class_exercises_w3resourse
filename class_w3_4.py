# Write a Python class to get all possible unique subsets from a set of distinct
# integers. Go to the editor
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class Script_4():

    def subsets(self, input_list):

        result = [[]]
        temp = []
        container = [[]]
        x = 0

        while x < len(input_list):

            for n, i in enumerate(container):
                for sublist in input_list[x + n:]:
                    temp.append(i + [sublist])

            x = x + 1
            result.extend(temp)
            container = temp[::]
            temp = []

        return result


if __name__ == "__main__":
    listin = [1, 2, 3, 4]
    len_list = len(listin)
    for i in Script_4().subsets(listin):
        print(i)
