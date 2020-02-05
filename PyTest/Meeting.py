#Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

meeting = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


last_meeting = meeting[0]

for current_meeting_start, current_meeting_end in meeting:
    last_meeting_start, last_meeting_end = last_meeting[-1]
    if last_meeting_end>current_meeting_start:
        last_meeting=current_meeting_start,max(last_meeting_end,current_meeting_start)
    else:
        last_meeting.append(current_meeting_start,current_meeting_end)

