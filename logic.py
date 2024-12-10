from typing import List

class VotingLogic:
    def __init__(self):
        self.votes_file = "votes.txt"
        self.load_votes()

    def load_votes(self):
        self.votes = {"John": 0, "Jane": 0, "voters": []}
        try:
            with open(self.votes_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("John"):
                        self.votes["John"] = int(line.split(":")[1])
                    elif line.startswith("Jane"):
                        self.votes["Jane"] = int(line.split(":")[1])
                    else:
                        self.votes["voters"].append(line)
        except FileNotFoundError:
            pass

    def save_votes(self):
        with open(self.votes_file, "w") as file:
            file.write(f"John:{self.votes['John']}\n")
            file.write(f"Jane:{self.votes['Jane']}\n")
            for voter in self.votes["voters"]:
                file.write(f"{voter}\n")

    def has_voted(self, voter_id: str) -> bool:
        return voter_id in self.votes["voters"]

    def record_vote(self, voter_id: str, candidate: str):
        self.votes[candidate] += 1
        self.votes["voters"].append(voter_id)
        self.save_votes()
