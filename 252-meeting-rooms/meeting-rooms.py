# Given an array of meeting time intervals consisting of start
# and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a
# person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

def attendAll(meetings):
    meetings.sort()

    if len(meetings) == 0:
        return True
    s, e = meetings[0]
    
    for m in meetings[1:]:
        ms, me = m
        if e >= ms:
            return False

    return True

def tests():
    # bad lists
    badTimes = [
        [[0, 30], [5,10], [15,20]],
        [[0, 100], [100, 120], [140, 150]]
    ]
    for meetings in badTimes:
        assert(attendAll(meetings) == False)

    # good lists
    goodTimes = [
        [[0, 30], [31, 54], [60, 70]],
        [[0, 100], [101, 120], [140, 150]]
    ]
    for meetings in goodTimes:
        assert(attendAll(meetings) == True)

if __name__ == "__main__":
    print("running tests for meeting-rooms.py...")
    tests()
    print("all tests passed")
