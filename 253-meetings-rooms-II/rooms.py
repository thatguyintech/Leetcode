# Given an array of meeting time intervals consisting of start
# and end times [[s1,e1],[s2,e2],...] find the minimum number
# of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 3

import heapq

def rooms(meetings):
    if len(meetings) == 0:
        return 0

    meetings.sort()
    rooms = [meetings[0][1]]

    for m in meetings[1:]:
        if m[0] > rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, m[1])

    return len(rooms)

def tests():
    cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[0, 1], [2, 3], [4, 5]], 1),
        ([[0, 30], [35, 70], [25, 30], [20, 40], [17, 60], [15, 35]], 5),
        ([[10,16],[11,13],[14,17]], 2)
    ]

    for case in cases:
        i, o = case
        answer = rooms(i)
        assert answer == o, "\ninput: {}\noutput: {}\nexpected: {}".format(i, answer, o)

if __name__ == "__main__":
    print("running tests...")
    tests()
    print("all tests passed")
