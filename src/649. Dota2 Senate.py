from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        judge = {
            'R':
                {
                    'banned': 0,
                    'enemy': 'D',
                    'fullname': 'Radiant',
                    'overall': sum(1 for symbol in senate if symbol == 'R')
                },
            'D':
                {
                    'banned': 0,
                    'enemy': 'R',
                    'fullname': 'Dire',
                    'overall': sum(1 for symbol in senate if symbol == 'D')
                },
        }
        senate = deque(senate)

        while judge.get('R').get('overall') and judge.get('D').get('overall'):
            party = senate.popleft()

            if judge.get(party).get('banned') == 0:
                enemy_party = judge.get(party).get('enemy')
                judge[enemy_party]['banned'] += 1

                senate.append(party)
            else:
                judge[party]['banned'] -= 1
                judge[party]['overall'] -= 1

        return judge.get(senate[0]).get('fullname')



