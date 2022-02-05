import unittest

from method.code import total


class TestRunner(unittest.TestCase):
    TEST_CNT = 0
    def setUp(self) -> None:
        self.inputs, self.answers = [], []
        TestRunner.TEST_CNT += 1
        with open(f'in/test_{TestRunner.TEST_CNT}.txt', 'r') as f:
            for line in f:
                self.inputs.append(line.strip('\n'))
        with open(f'out/answer_{TestRunner.TEST_CNT}.txt', 'r') as f:
            for line in f:
                self.answers.append(line.strip('\n'))

    def test_1(self) -> None:
        self.assertEqual(total(self.inputs), self.answers)

    def test_2(self) -> None:
        self.assertEqual(total(self.inputs), self.answers)
