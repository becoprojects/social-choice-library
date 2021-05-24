from Preference import Preference, PreferenceList
class Profile:

    def __init__(self, preferences):
        self.preferences = preferences

    def __repr__(self):
        return str(self.preferences)