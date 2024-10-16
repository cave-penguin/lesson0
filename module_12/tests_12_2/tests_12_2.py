import unittest

from module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    """
    Тестовый набор для проверки работы турнира (класса Tournament).

    Этот класс проверяет, как разные участники (бегуны) соревнуются друг с другом
    в зависимости от их скоростей и дистанций. В тестах проводится проверка того,
    кто приходит последним к финишу в разных сценариях.
    """

    @classmethod
    def setUpClass(cls):
        """
        Устанавливает общие настройки для всех тестов класса.

        Создает общий словарь для хранения результатов всех запусков турниров.
        """
        cls.all_results = {}

    def setUp(self):
        """
        Инициализирует бегунов перед каждым тестом.

        Создает объекты для трех бегунов с разной скоростью:
        - Усейн: скорость 10
        - Андрей: скорость 9
        - Ник: скорость 3
        """
        self.runner_1_test = Runner("Усейн", 10)
        self.runner_2_test = Runner("Андрей", 9)
        self.runner_3_test = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        """
        Выполняет действия после завершения всех тестов класса.

        Печатает все результаты, собранные за время тестирования.
        """
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_start_1(self):
        """
        Тестирует работу турнира с двумя участниками: Усейн и Ник.

        Проверяет, что Ник (более медленный) приходит последним при дистанции 90.
        """
        tournament_test = Tournament(90, self.runner_1_test, self.runner_3_test)
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_1"] = result

    def test_start_2(self):
        """
        Тестирует работу турнира с двумя участниками: Андрей и Ник.

        Проверяет, что Ник (более медленный) приходит последним при дистанции 90.
        """
        tournament_test = Tournament(90, self.runner_2_test, self.runner_3_test)
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_2"] = result

    def test_start_3(self):
        """
        Тестирует работу турнира с тремя участниками: Усейн, Андрей и Ник.

        Проверяет, что Ник (более медленный) приходит последним при дистанции 90.
        """
        tournament_test = Tournament(
            90, self.runner_1_test, self.runner_2_test, self.runner_3_test
        )
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_3"] = result

    def test_start_1_extra(self):
        """
        Тестирует работу турнира с тремя участниками при короткой дистанции 20.

        Проверяет, что Ник приходит последним на короткой дистанции.
        """
        tournament_test = Tournament(
            20, self.runner_1_test, self.runner_2_test, self.runner_3_test
        )
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_1_extra"] = result

    def test_start_2_extra(self):
        """
        Тестирует работу турнира с тремя участниками при дистанции 35.

        Проверяет, что Ник приходит последним на дистанции 35.
        """
        tournament_test = Tournament(
            35, self.runner_1_test, self.runner_2_test, self.runner_3_test
        )
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_2_extra"] = result

    def test_start_3_extra(self):
        """
        Тестирует работу турнира с тремя участниками при дистанции 50.

        Проверяет, что Ник приходит последним на дистанции 50.
        """
        tournament_test = Tournament(
            50, self.runner_1_test, self.runner_2_test, self.runner_3_test
        )
        result = tournament_test.start()
        last_runner_key = max(result)
        self.assertTrue(result[last_runner_key], "Ник")
        TournamentTest.all_results["test_start_3_extra"] = result


if __name__ == "__main__":
    unittest.main()
