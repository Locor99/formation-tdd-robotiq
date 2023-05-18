import os
from src.chap4_classes.file_not_found_exception import FileNotFoundException

class LineCompactor:
    def compact(self, from_path, to_path):
        if os.path.isfile(from_path):
            with open(from_path) as file:
                lines = [line.rstrip('\n') for line in file]

            with open(to_path, 'w+') as file:
                file.write(str.join('', lines))
        else:
            raise FileNotFoundException("Error: File not found: {}".format(from_path))
