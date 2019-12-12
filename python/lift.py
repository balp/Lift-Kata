from enum import Enum
from typing import List
from attr import dataclass


class Direction(Enum):
    UP = 0
    DOWN = 1


@dataclass
class Call:
    floor: int
    direction: Direction


class Lift:

    def __init__(self, id, floor, doors_open=False, requested_floors=None):
        self.id = id
        self.floor = floor
        self.doors_open = doors_open
        self.requested_floors = list(requested_floors) if requested_floors else []

    def request(self, floor: int) -> None:
        self.requested_floors.append(floor)

    def tick(self):
        if self.floor == self.requested_floors[0]:
            self.doors_open = True
            self.requested_floors.pop(0)
        elif self.doors_open:
            self.doors_open = False
        else:
            self.floor = self.requested_floors[0]

class LiftSystem:
    def __init__(self, floors=None, calls=None, lifts=None):
        self.floors = list(floors) if floors else []
        self.calls = list(calls) if calls else []
        self.lifts: List[Lift] = list(lifts) if lifts else []

    def calls_for(self, floor):
        return [c for c in self.calls if c.floor == floor]

    def tick(self):
        for lift in self.lifts:
            lift.tick()


