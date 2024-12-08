import unittest
from Tests_12_3 import RunnerTest, TournamentTest

TestST = unittest.TestSuite()


TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestST)



