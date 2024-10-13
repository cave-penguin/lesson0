import unittest


class Runner:
    def __init__(self, name):
        """
        Initialize the Runner with a name and set initial distance to 0.

        :param name: The name of the runner.
        """
        self.name = name
        self.distance = 0

    def run(self):
        """
        Simulate running by increasing the runner's distance by 10 units.
        """
        self.distance += 10

    def walk(self):
        """
        Simulate walking by increasing the runner's distance by 5 units.
        """
        self.distance += 5

    def __str__(self):
        """
        Return a string representation of the Runner object, which is the runner's name.

        :return: The name of the runner.
        """
        return self.name


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner_1 = Runner("Ivan")
        self.runner_2 = Runner("Alex")
        self.runner_3 = Runner("Micky")
        self.runner_4 = Runner("Max")

    def test_walk(self):
        """
        Test for walk method in Runner

        This test ensures that after calling walk 10 times,
        the runner's distance increases by 50 units.
        """
        for _ in range(10):
            self.runner_1.walk()
        self.assertEqual(self.runner_1.distance, 50)

    def test_run(self):
        """
        Test for run method in Runner

        This test ensures that after calling run 10 times,
        the runner's distance increases by 100 units.
        """
        for _ in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    def test_challenge(self):
        """
        Test for challenge in Runner
        Runners Micky and Max are performing a challenge.
        Micky runs and Max walks for 10 times.
        At the end of challenge, their distances are compared.
        """
        for _ in range(10):
            self.runner_3.run()
            self.runner_4.walk()
        self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)


if __name__ == "__main__":
    unittest.main()
