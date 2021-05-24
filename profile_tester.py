from Profile import Profile
import itertools
from Preference import PreferenceList

def generate_all_profiles(voter_count, alternatives):
    all_preferences = []
    permutations = list(itertools.permutations(alternatives))
    for permutation in permutations:
        rank = 1
        order = {}
        for cand in permutation:
            order[rank] = [cand]
            rank += 1
        preference = PreferenceList(order)
        all_preferences.append(preference)
    return [Profile(x) for x in list(itertools.product(all_preferences,repeat=voter_count))]

def all_profiles_results(voter_count, alternatives, voting_system):
    profiles = generate_all_profiles(voter_count, alternatives)
    results_list = []
    for profile in profiles:
        result = voting_system.run(profile, alternatives)
        results_list.append(result)
    return results_list
