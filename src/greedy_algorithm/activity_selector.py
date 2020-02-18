#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

activities = [
    (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)
]

def activity_selector(activities, activity_number):
    """活动选择问题
    """
    activity = activities[activity_number]
    activity_number += 1
    while activity_number < len(activities)-1:
        start_time = activities[activity_number][0]
        if start_time > activity[1]:
            break
        else:
            activity_number += 1
    if activity_number > len(activities) - 1:
        return {activity}
    else:
        return {activity}.union(activity_selector(activities, activity_number))

if __name__ == "__main__":
    print(activity_selector(activities, 0))