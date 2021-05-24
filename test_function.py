from Preference import PreferenceList
import random
def plurality_rule(profile, candidates):
    cand_count = {x:0 for x in candidates}
    for preference in profile.preferences:
        top_candidates = []
        for c in candidates:
            other_cands = [x for x in candidates if x != c]
            top = True
            for o in other_cands:
                if preference.is_strongly_prefered(o,c):
                    top = False
                    break
            if top:
                top_candidates.append(c)
        cand_count[random.choice(top_candidates)] += 1
    max_val = max(cand_count.values())
    final_list = [x for x in candidates if cand_count[x] == max_val]
    other_cands = [x for x in candidates if x not in final_list]
    return PreferenceList({1:final_list, 2:other_cands})

def borda_count(profile, candidates):
    cand_count = {x:0 for x in candidates}
    for preference in profile.preferences:
        preference_dict = preference.ordered_dict
        ranks = list(preference_dict.keys())
        for rank in ranks:
            if len(preference_dict[rank]) == 1:
                cand_count[preference_dict[rank][0]] += len(candidates) - rank
            else:
                points = len(candidates) - rank
                points_each = points/len(preference_dict[rank])
                for cand in preference_dict[rank]:
                    cand_count[preference_dict[rank][0]] += points_each
    final_order_dict = {}
    rank = 1
    remaining_cands = [x for x in candidates if cand_count[x] != -1]
    while len(remaining_cands) > 0:
        final_order_dict[rank] = []
        max_points = max(list(cand_count.values()))
        for cand in candidates:
            if cand_count[cand] == max_points:
                final_order_dict[rank].append(cand)
                cand_count[cand] = -1
        rank += 1
        remaining_cands = [x for x in candidates if cand_count[x] != -1]
    return PreferenceList(final_order_dict)

        
    

