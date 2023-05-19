class Combiner:
    def __init__(self):
        self.activeArray = []
    def squash(self, array):
        self.activeArray = array
        # return [None, None, None, None]

        tileWasMoved = True
        while tileWasMoved:
            tileWasMoved = False
            for i in range(1, len(array)):
                if self._tile_is_empty(i-1) and not self._tile_is_empty(i):
                    self.activeArray[i-1] = self.activeArray[i]
                    self.activeArray[i] = None
                    tileWasMoved = True

                elif not self._tile_is_empty(i-1) and self.activeArray[i-1] == self.activeArray[i]:
                    self.activeArray[i-1] *= 2
                    self.activeArray[i] = None

        return array

    def _tile_is_empty(self, index):
        return self.activeArray[index] is None
