from approvaltests import verify

from lift import Lift, LiftSystem
from lift_printers import print_lifts


def test_request_to_move():
    lifts, lifts_before_tick = set_up_simple_lift_system(start_floor=2, request_floor=1, doors_open=False)
    lifts.tick()
    lifts_after_tick = print_lifts(lifts)
    _verify_lifts(lifts_after_tick, lifts_before_tick)


def test_on_requested_floor_open_door():
    lifts, lifts_before_tick = set_up_simple_lift_system(start_floor=1, request_floor=1, doors_open=False)
    lifts.tick()
    lifts_after_tick = print_lifts(lifts)
    _verify_lifts(lifts_after_tick, lifts_before_tick)


def test_dont_move_on_request_with_open_doors():
    lifts, lifts_before_tick = set_up_simple_lift_system(start_floor=1, request_floor=2, doors_open=True)
    lifts.tick()
    lifts_after_tick = print_lifts(lifts)
    _verify_lifts(lifts_after_tick, lifts_before_tick)


def set_up_simple_lift_system(start_floor, request_floor, doors_open):
    lift_a = Lift("A", start_floor)
    lift_a.request(request_floor)
    lift_a.doors_open = doors_open
    lifts = LiftSystem(floors=[1, 2], lifts=[lift_a])
    lifts_before_tick = print_lifts(lifts)
    return lifts, lifts_before_tick


def _verify_lifts(lifts_after_tick, lifts_before_tick):
    verify(f"""Before:
{lifts_before_tick}

After:

{lifts_after_tick}""")

