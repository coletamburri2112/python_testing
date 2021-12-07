import unittest
import my_lib
import random
import statistics

class TestLib(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n Running class setUp...")
        
    @classmethod
    def tearDownClass(cls):
        print("\n Running class tearDown...")
        
    def setUp(self):
        print("\nRunning setUp...")
        
    def tearDown(self):
        print("Running tearDown...")
        
    def test_list_avg_null(self):
        res = my_lib.list_avg(None)
        self.assertEqual(res, None)
        self.assertIsNone(res)
    
    def test_list_avg_empty(self):
        res = my_lib.list_avg([])
        self.assertIsNone(res)
        
    def test_mylib_load(self):
        res = my_lib.load_sample()
        self.assertIsNone(res)
        
    def test_list_avg_const(self):
        print("Running test_list_avg_const...")
        res = my_lib.list_avg([5, 5, 5, 5, 5, 5])
        self.assertEqual(res, 5)
    
        res = my_lib.list_avg([-10, -10, -10])
        self.assertEqual(res, -10)
        
        res = my_lib.list_avg([23])
        self.assertEqual(res, 23)
    
    def test_list_avg_floats(self):
        for _ in range(10):
            vals =[]
            size = random.randint(1, 100)
            
            for _ in range(size):
                val = random.uniform(-200, 1000)
                vals.append(val)
            
            res = my_lib.list_avg(vals)
            exp = statistics.mean(vals)
            self.assertAlmostEqual(res, exp, places=10)
            
    def test_list_avg_nonlist(self):

        self.assertRaises(TypeError, my_lib.list_avg, {'a': 1, 'b': 23.0})
        
        # dictionary input
        self.assertRaises(TypeError,my_lib.list_avg,{'a': 1, 'b': 2, 'c': 3})
        # set input
        self.assertRaises(TypeError,my_lib.list_avg,{4.4, 55, -0.4, 18})

class OtherTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nOther class setup...")
        
    @classmethod
    def tearDownClass(cls):
        print("\nOther class tear down...")
        
    def test_other_func_or_lib(self):
        print("Running our test for other stuff...")
        
    
    
if __name__ == "__main__":
    unittest.main()