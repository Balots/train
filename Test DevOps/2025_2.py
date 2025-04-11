import sys
from typing import List


class LogMobileDistinguisher:
    def __init__(self, desktop_file_name, mobile_file_name):
        self.mobile = self.read_file(mobile_file_name)
        self.desktop = self.read_file(desktop_file_name)
        self.process_log()

    @staticmethod
    def read_file(file_name: str) -> List[str]:
        with open(file_name, 'r') as fi:
            result = []
            for line in fi.readlines():
                result.append(line.strip())
            return result

    def get_line_client(self, line_ua: str) -> str:
        result = 'unknown'

        for ua in self.desktop:
            if ua == line_ua:
                result = 'desktop'

        for ua in self.mobile:
            if ua == line_ua:
                result = 'mobile'

        return result

    @staticmethod
    def get_line_fields(line: str) -> List[str]:
        result = []
        indexes = []
        for sym in line:
            if sym == '"':
                indexes.append(sym)
        for i in range(len(indexes)):
            result.append(line[indexes[i] + 1:indexes[i+1]])
        return result

    def process_log(self):
        for line in sys.stdin.readlines():
            fields = self.get_line_fields(line)
            client = self.get_line_client(fields[-1])
            print(client + ' ' + line.strip())


if __name__ == '__main__':
    LogMobileDistinguisher('d.txt', 'm.txt')