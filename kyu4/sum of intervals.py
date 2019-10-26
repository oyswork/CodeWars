def sum_of_intervals(intervals):

    intervals = sorted(intervals, key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    print(sum([end - beg for beg,end in merged]))
sum_of_intervals([[1,2],[11, 15],
   [6, 10]
   ])