from codrone_edu.drone import *

DISTANCE_THRESHOLD = 50
FORWARD_POWER = 20

drone = Drone()
drone.pair()


def is_object_detected(within_a_distance):
    return drone.get_front_range() <= within_a_distance


def look_left():
    drone.turn_left(90)


def look_right():
    drone.turn_right(90)


def avoid_object():
    drone.set_pitch(0)

    look_left()
    left_blocked = is_object_detected(150)

    look_right()
    right_blocked = is_object_detected(150)

    if left_blocked:
        look_right()
        drone.set_pitch(FORWARD_POWER)

    if right_blocked:
        look_left()
        drone.set_pitch(FORWARD_POWER)
    else:
        if left_blocked and right_blocked:
            drone.set_pitch(-FORWARD_POWER)


def fly_drone():
    drone.takeoff()
    drone.set_pitch(FORWARD_POWER)
    try:
        while True:
            drone.move()
            if is_object_detected(DISTANCE_THRESHOLD):
                avoid_object()
    finally:
        drone.set_pitch(0)
        drone.land()
        drone.close()


fly_drone()

