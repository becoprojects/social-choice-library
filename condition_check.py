from profile_tester import generate_all_profiles, all_profiles_results

def verify_pareto_efficient(voting_system, alternatives, voter_count):
    profiles = generate_all_profiles(voter_count,alternatives)
    results = all_profiles_results(voter_count,alternatives,voting_system)
    for i in range(len(profiles)):
        for alt in alternatives:
            other_alts = [x for x in alternatives if x != alt]
            for other_alt in other_alts:
                prefered = True
                for preferences in profiles[i].preferences:
                    if preferences.is_weakly_prefered(other_alt, alt):
                        prefered = False
                        break
                if prefered and results[i].is_weakly_prefered(other_alt, alt):
                    return False
    return True