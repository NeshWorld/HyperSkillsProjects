# Write your code here >>>


# Function for input and use recursivity
def input_time_allowed(subject_choice):
    time_allowed_choice = input(f"Enter time allocated for {subject_choice}:")
    return check_integer_value(time_allowed_choice, subject_choice)


# Recursivity use for not integer value for an expected integer input
def check_integer_value(value, subject_choice):
    try:
        value = int(value)
        if value <= 0:  # Not allowed to use negative input
            return input_time_allowed(subject_choice)
        else:
            return value
    except ValueError:
        return input_time_allowed(subject_choice)


# Empty dictionary for futur use
subjects = {}


def get_user_study_plan():
    while True:
        # Ask user for subject input
        subject_choice = input("Enter subject name: ")

        if subject_choice != "":

            time_allowed_choice = input_time_allowed(
                subject_choice
            )  # Ask user to the time allowed for this subject

            subjects[subject_choice] = int(time_allowed_choice)
        else:
            break
    return subjects


if __name__ == "__main__":
    subjects = get_user_study_plan()
