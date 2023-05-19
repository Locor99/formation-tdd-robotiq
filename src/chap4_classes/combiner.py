EMPTY = None

class Combiner:
    def __init__(self):
        pass

    def squash(self, array):
        for i in range(len(array)-1):
            if array[i] is EMPTY :
                self._remove_empty_neighbors(array, i)

            if self._can_combine_tiles(array, i):
                array[i] *= 2
                array[i+1] = None

        return array

    def _remove_empty_neighbors(self, array, i):
        for j in range(i+1, len(array)):
            if array[j] is not EMPTY:
                array[i] = array[j]
                array[j] = None
                i += 1

    def _can_combine_tiles(self, array, i):
        return array[i] and array[i] == array[i+1]
