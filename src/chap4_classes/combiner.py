class Combiner:
    def squash(self, array):
        # return [None, None, None, None]

        while True:
            tileWasMoved = False
            for i in range(1, len(array)):
                if array[i-1] is None and array[i] is not None:
                    array[i-1] = array[i]
                    array[i] = None
                    tileWasMoved = True

            if not tileWasMoved:
                break

        return array