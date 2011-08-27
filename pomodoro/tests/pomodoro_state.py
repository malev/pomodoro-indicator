import unittest
from pomodoro-indicator.pomodoro_state import PomodoroState

class TestPomodoroState(unittest.TestCase):

    def setUp(self):
        self.state = PomodoroState()

    def test_has_all_the_methods(self):
        """There a list of methods it has to have but do nothing"""
        methods_list = ["enabled_buttons", "start", "next_state", "pause", "resume"]
        for method in methods_list:
            assert hasattr(self.state, method)
            
    def test_should_not_be_on_any_state(self):
        """The super class should not be on any singular state"""
        states = ["working", "resting", "paused", "waiting"]
        for state in states:
            method = getattr(self.state, state)
            self.assertFalse(method())
    
    def test_current_state(self):
        """Every state should have a name and this method provides it"""
        self.state.name = "name"
        self.assertEqual("name", self.state.current_state())
    
    def test_wont_work(self):
        self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()
