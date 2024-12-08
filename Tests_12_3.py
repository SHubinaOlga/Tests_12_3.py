import unittest
from runner_and_tournament import Runner, Tournament
import runner

def frozen(func):
    def wrapper(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func
        return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walks = runner.Runner('Лео')
        for i in range(10):
            walks.walk()
        self.assertEqual(walks.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runs = runner.Runner('Лена')
        for i in range(10):
            runs.run()
        self.assertEqual(runs.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walks = runner.Runner('Леo')
        runs = runner.Runner('Лена')
        for i in range(10):
            runs.run()
            walks.walk()
        self.assertNotEqual(runs.distance, walks.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run_1 = Runner('Усэйн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)
        self.distans = 90

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tourn_1 = Tournament(self.distans, self.run_1, self.run_3)
        result = tourn_1.start()
        self.all_results['test_1'] = result


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tourn_2 = Tournament(self.distans, self.run_2, self.run_3)
        result = tourn_2.start()
        self.all_results['test_2'] = result


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tourn_3 = Tournament(self.distans, self.run_1, self.run_2, self.run_3)
        result = tourn_3.start()
        self.all_results['test_3'] = result

        # Дополнительно.

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_4(self):
        tourn_4 = Tournament(5, self.run_1, self.run_2, self.run_3)
        result = tourn_4.start()
        self.all_results['test_4'] = result