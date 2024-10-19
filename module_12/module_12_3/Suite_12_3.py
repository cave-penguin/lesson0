import unittest
from tests_12_3 import RunnerTest, TournamentTest

runTourTS = unittest.TestSuite()

all_tests = [RunnerTest, TournamentTest]
for test in all_tests:
    runTourTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test))


# runTourTS.addTests(
#     [
#         unittest.TestLoader().loadTestsFromTestCase(RunnerTest),
#         unittest.TestLoader().loadTestsFromTestCase(TournamentTest),
#     ]
# )

runner = unittest.TextTestRunner(verbosity=2)

runner.run(runTourTS)
