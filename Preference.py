class Preference:

    def __init__(self, pref1, pref2):
        self.prefered_alternative = pref1
        self.unprefered_alternative = pref2

    def __repr__(self):
        return "{0}-R-{1}".format(self.prefered_alternative, self.unprefered_alternative)

class PreferenceList:

    def __init__(self, ordered_alternative_dict):
        ranks = [rank for rank in ordered_alternative_dict.keys()]
        self.ordered_dict = ordered_alternative_dict
        self.preference_list = []
        for rank in ordered_alternative_dict:
            for alternative in ordered_alternative_dict[rank]:
                cur_rank = rank
                while cur_rank <= max(ranks):
                    for other_alt in ordered_alternative_dict[cur_rank]:
                        if other_alt != alternative:
                            temp_preference = Preference(alternative, other_alt)
                            self.preference_list.append(temp_preference)
                    cur_rank += 1


    def is_weakly_prefered(self, prefered_alternative, unprefered_alternative):
        if self._is_preference_in_list(prefered_alternative, unprefered_alternative):
            return True
        return False
    
    def is_strongly_prefered(self, prefered_alternative, unprefered_alternative):
        if (self._is_preference_in_list(prefered_alternative, unprefered_alternative)) and (not self._is_preference_in_list(unprefered_alternative, prefered_alternative)):
            return True
        return False
    
    def is_indifferent(self, alternative1, alternative2):
        if self._is_preference_in_list(alternative1,alternative2) and self._is_preference_in_list(alternative2, alternative1):
            return True
        return False

    def _is_preference_in_list(self, prefered_alternative, unprefered_alternative):
        for preference in self.preference_list:
            if preference.prefered_alternative == prefered_alternative and preference.unprefered_alternative == unprefered_alternative:
                return True
        return False

    def __repr__(self):
        return str(self.preference_list)