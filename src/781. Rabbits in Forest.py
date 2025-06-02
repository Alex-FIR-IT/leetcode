class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """

        rabbits_answers = {}
        rabbits_count = 0

        for answer in answers:
            the_same_answers = rabbits_answers.get(answer, 0)

            if the_same_answers == answer:
                rabbits_count += (answer + 1)
                del rabbits_answers[answer]
            else:
                rabbits_answers[answer] = the_same_answers + 1
        else:
            return sum(rabbits_answers) + len(rabbits_answers) + rabbits_count


if __name__ == '__main__':
    print(Solution().numRabbits([1, 1, 2]))