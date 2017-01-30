import unittest
import roulette as rl

class JsonTestCase(unittest.TestCase):
    """tests for app.py"""

    def is_json_loading(self):
        """the data type of the participants variable is a dictionary"""
        self.assertTrue(type(rl.participant_dict) == dictionary)
        self.assertTrue(type(rl.lunch_dict) == dictionary)

if __name__ == '__main__':
    unittest.main()
