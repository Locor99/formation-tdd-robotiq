import subprocess

RETURN_CODE_INDEX = 0
OUTPUT_INDEX = 1
SUCCESS_RETURN_CODE = 0


class UnixShell(object):
    @staticmethod
    def get_output_from_command(command):
        return subprocess.getstatusoutput(command)