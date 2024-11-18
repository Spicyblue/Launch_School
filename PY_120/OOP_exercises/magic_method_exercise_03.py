'''
Exercise 3
Challenge: Create the classes needed to make the following code work as shown:

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
print(election.results())

Outputs

Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes

Don't worry about ties or whether votes should be singular.

Hint
You should use the __iadd__ method to customize the behavior of += in the for loop.
__iadd__ is similar to __add__ except that it implements +=.
You don't need a __add__ method.
'''

# Solution

class Candidate:

    def __init__(self, candidate_name):
        self._name = candidate_name
        self._vote = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self._vote += other
        return self


class Election:

    def __init__(self, candidate):
        self._candidate = candidate

    def results(self):
        max_votes = 0
        vote_counted = 0
        winner = ''

        for members in candidates:
            name = members._name
            votes = members._vote
            print(f'{name}: {votes} votes')
        
        print()
        for members in candidates: # accessing the set global variable candidate that is an instance object of class Candidate
            vote_counted += members._vote

            if members._vote > max_votes:
                max_votes = members._vote
                winner = members._name

        percent = 100 * (max_votes / vote_counted)
        return f'{winner} won: {percent}% of votes'

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
print(election.results())

## LS Answer ##
## LS Answer ##
# class Candidate:

#     def __init__(self, name):
#         self.name = name
#         self.votes = 0

#     def __iadd__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented

#         self.votes += other
#         return self

# class Election:

#     def __init__(self, candidates):
#         self.candidates = candidates

#     def results(self):
#         max_votes = 0
#         vote_count = 0
#         winner = None

#         for candidate in candidates:
#             vote_count += candidate.votes
#             if candidate.votes > max_votes:
#                 max_votes = candidate.votes
#                 winner = candidate.name

#         for candidate in candidates:
#             name = candidate.name
#             votes = candidate.votes
#             print(f'{name}: {votes} votes')

#         percent = 100 * (max_votes / vote_count)
#         print()
#         print(f'{winner} won: {percent}% of votes')

# The __iadd__ method is crucial to this solution. 
# Note that we are adding integers to the Candidate objects;
# thus, our __iadd__ method needs to deal with integers to the right of the +.

# We didn't customize + in this example.
# Had we done so, we would have had to create a new Candidate object,
# which implies multiple Candidate objects for the same candidate.
# They might even end up with different vote counts.

# In general, you shouldn't customize + and += when you need to create an unwanted new object. 
# se something like an add_vote method instead.
