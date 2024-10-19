class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        if self.full_distance < 55:
            finish_time = {}
            for participant in self.participants:
                time = self.full_distance / participant.speed
                finish_time[participant.name] = time
            sorted_finishers = dict(
                sorted(finish_time.items(), key=lambda item: item[1])
            )
            finishers = {
                index: participant
                for index, participant in enumerate(sorted_finishers, start=1)
            }
            return finishers
        else:
            place = 1
            while self.participants:
                for participant in self.participants:
                    participant.run()
                    if participant.distance >= self.full_distance:
                        finishers[place] = participant.name
                        place += 1
                        self.participants.remove(participant)
        return finishers
