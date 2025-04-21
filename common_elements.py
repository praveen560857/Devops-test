class CommonElementsFinder:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def find_common(self):
        i, j = 0, 0
        result = []
        last_added = None

        while i < len(self.arr1) and j < len(self.arr2):
            if self.arr1[i] == self.arr2[j]:
                if self.arr1[i] != last_added:
                    result.append(self.arr1[i])
                    last_added = self.arr1[i]
                i += 1
                j += 1
            elif self.arr1[i] < self.arr2[j]:
                i += 1
            else:
                j += 1

        return result

# ----------- Example Usage ------------
if __name__ == "__main__":
    arr1 = [1, 2, 2, 3, 5, 7, 10]
    arr2 = [2, 2, 5, 6, 7, 8, 10]

    finder = CommonElementsFinder(arr1, arr2)
    common = finder.find_common()
    print("Common elements:", common)
