def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    print('sorted_meetings',sorted_meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    print('merged_meetings', merged_meetings)

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        print('second_sorted', sorted_meetings[1:])
        print('current start,current end', current_meeting_start,current_meeting_end)
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        print('last_merged_meeting_start,last_merged_meeting_end',last_merged_meeting_start,last_merged_meeting_end)

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
            print(merged_meetings)
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
            print(merged_meetings)

    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))