# import requests
# import json
# STATS_PARAMS=[
#    'open_play_pass','fwd_pass','formation_used','possession_percentage',"touches","successful_open_play_pass","keeper_throws","rightside_pass",
#     "ball_recovery","duel_won","accurate_pass","poss_lost_all","total_pass","accurate_keeper_throws", "aerial_won", "leftside_pass","total_back_zone_pass",
#     "accurate_back_zone_pass","poss_lost_ctrl", "total_long_balls","total_contest","passes_right","backward_pass","total_final_third_passes",
#     "total_fwd_zone_pass","total_throws","accurate_long_balls", "accurate_flick_on"
# ]
# def get_stats():
#     new_result = []
#     for match_id in range(66342, 66462):
#         url = 'https://footballapi.pulselive.com/football/stats/match/' +str(match_id)
#         data = requests.get(url, headers={
#         'Origin': 'https://www.premierleague.com'
#         }).json()
#
#         result = {
#             'team': [x['team']['name'] for x in data['entity']['teams']]
#         }
#         result['opponent'] = [x for x in result['team']]
#         result['opponent'].reverse()
#
#         for stat in STATS_PARAMS:
#             result[stat] = [
#                 list(filter(lambda el: el['name'] == stat, x['M']))[0]['value']
#                 for x
#                 in data['data'].values()
#             ]
#
#         for x in range(len(result['team'])):
#             new_result.append({y: result[y][x] for y in result.keys()})
#
#     result = json.dumps(new_result)
#     jsonFile = open("result.json", "w")
#     jsonFile.write(result)
#     jsonFile.close()
#
#     print('success')
# get_stats()