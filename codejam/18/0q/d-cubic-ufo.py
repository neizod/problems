#!/usr/bin/env python3

import math


def transform_rotate(x_angle, z_angle):
    points = [[0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]]
    tmp_transform = []
    for point in points:
        tmp = []
        tmp += [point[0]]
        tmp += [math.cos(x_angle) * point[1] - math.sin(x_angle) * point[2]]
        tmp += [math.sin(x_angle) * point[1] + math.cos(x_angle) * point[2]]
        tmp_transform += [tmp]
    points = tmp_transform
    tmp_transform = []
    for point in points:
        tmp = []
        tmp += [math.cos(z_angle) * point[0] - math.sin(z_angle) * point[1]]
        tmp += [math.sin(z_angle) * point[0] + math.cos(z_angle) * point[1]]
        tmp += [point[2]]
        tmp_transform += [tmp]
    points = tmp_transform
    return points


def hexagon_shadow(angle):
    return 2**0.5 * math.cos(angle) + math.sin(angle)


def rotate_two_axis(area):
    lower = 0
    upper = math.atan(1/2**0.5)
    angle = (lower + upper) / 2
    while True:
        guess_area = hexagon_shadow(angle)
        if math.isclose(guess_area, area):
            break
        elif guess_area < area:
            lower = angle
        elif guess_area > area:
            upper = angle
        angle = (lower + upper) / 2
    return math.radians(45), angle


def rotate_one_axis(area):
    angle = math.radians(45) - math.acos(area/2**0.5)
    return angle, 0


def compatible_points(area):
    if area <= 2**0.5:
        x_angle, z_angle = rotate_one_axis(area)
    else:
        x_angle, z_angle = rotate_two_axis(area)
    return transform_rotate(x_angle, z_angle)


def main():
    for case in range(int(input())):
        area = float(input())
        answers = compatible_points(area)
        print('Case #{}:'.format(case+1))
        for point in answers:
            print(' '.join(str(num) for num in point))


if __name__ == '__main__':
    main()
