from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        """
        Test for walk method in Runner
        :return:
        """
        runner_1 = Runner("Ivan")
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        """
        Test for run method in Runner
        :return:
        """
        runner_1 = Runner("Alex")
        for _ in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    def test_challenge(self):
        """
        Test for challenge in Runner
        Runners Micky and Max are performing a challenge.
        Micky runs and Max walks for 10 times.
        At the end of challenge, their distances are compared.
        """
        runner_1 = Runner("Micky")
        runner_2 = Runner("Max")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


RunnerTest()
