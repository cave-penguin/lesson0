import logging
import unittest

from module_12_2 import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner_1 = Runner("Ivan", -15)
            for _ in range(10):
                runner_1.walk()
            assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as er:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner_2 = Runner(20)
            for _ in range(10):
                runner_2.run()
            assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as er:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    # @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    # def test_challenge(self):
    #     for _ in range(10):
    #         self.runner_3.run()
    #         self.runner_4.walk()
    #     self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filemode="w",
        filename=r"Homeworks\module_12\module_12_4\runner_tests.log",
        encoding="utf-8",
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    unittest.main()

