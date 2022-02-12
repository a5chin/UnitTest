import unittest
from typing import List

from method.code import main


class TestRunner(unittest.TestCase):
    TEST_CNT = 0
    def setUp(self) -> None:
        TestRunner.TEST_CNT += 1
        self.inputs = self.read_file(f'in/test_{TestRunner.TEST_CNT}.txt')
        self.answers = self.read_file(f'out/answer_{TestRunner.TEST_CNT}.txt')

    def test_1(self) -> None:
        self.assertEqual(main(self.inputs), self.answers)

    def test_2(self) -> None:
        self.assertEqual(main(self.inputs), self.answers)

    def read_file(self, file: str) -> List:
        lst = []
        with open(file, 'r') as f:
            for line in f:
                lst.append(line.strip('\n'))
        return lst
