from unittest import TestCase
from prysm import Check, Fail

class test_simple_check_execution(TestCase):
    def setUp(self):
        class AlwaysFails(Check):
            def __call__(self):
                raise Fail()
        class AlwaysSucceeds(Check):
            def __call__(self):
                return True
                
        self.fail = AlwaysFails()
        self.succeed = AlwaysSucceeds()
        
    def test_failing_check(self):
        self.assertRaises(Fail, self.fail())
        
    def test_succeeding_check(self):
        self.assertEqual(True, self.succeed())
    
