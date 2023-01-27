def study_schedule(permanence_period, target_time):
    students_counter = 0

    if not target_time or not permanence_period:
        return None

    for entry, exit in permanence_period:
        if ((type(entry) is not int) or (type(exit) is not int)):
            return None

        if entry <= target_time <= exit:
            students_counter += 1

    return students_counter
