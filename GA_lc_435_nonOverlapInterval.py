# -*- coding: utf-8 -*-
"""
435. Non-overlapping Intervals
Given a collection of intervals, 
find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

intervals=[[1,2],[2,3],[3,4],[1,3]]


def v1(intervals):
    """
    complete
    """
    initL=len(intervals)
    intervals.sort(key= lambda x: x[1])
    intervals=sorted(intervals, key= lambda x:x[1])
    s=[i[0] for i in intervals]
    a=[]
    while intervals!=[]:
        a.append(intervals[0])
        if len(intervals)>1:
            for i in range(1, initL):
                if s[i] >= intervals[0][1]:
                    del intervals[:i]
                    del s[:i]
                    break
        else:
            del intervals[0]

def v2(intervals):              
    """
    faster
    """
    intervals.sort(key= lambda x: x[1])
    cur=0
    remove=0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[cur][1]:
            remove+=1
        else:
            cur=i
v2(intervals)

