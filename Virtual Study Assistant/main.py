# Write your solution here
import sys

from huggingface_hub import InferenceClient

from study_assistant import get_user_study_plan

if __name__ == "__main__":
    subjects = get_user_study_plan()
    if not subjects:
        sys.exit()


# Create empty space for future sum of minutes
def total_minutes_study(dictionary_study_plan):
    total_time = sum(dictionary_study_plan.values())
    return total_time


study_time = total_minutes_study(subjects)

total_break_time = study_time // 45 * 15
total_study_time = study_time + total_break_time

# Final output:
print("Your study plan:")
for subject in subjects:
    print(f"{subject}: {subjects[subject]} minutes")
print(
    f"Total study time: {study_time} minutes\n"
    f"Total time including breaks: {total_study_time} minutes"
)

user_time_spent_input = int(input("Enter the time spent studying: "))

if user_time_spent_input > study_time:
    user_time_spent_input = study_time
else:
    pass
completeness = user_time_spent_input / study_time * 100
print(f"You have completed{completeness: .2f}% of your planned study time.")

# AI request
with open(".env", "r") as fp:
    HF_API_KEY = fp.read().strip()

client = InferenceClient(provider="featherless-ai", api_key=HF_API_KEY)
prompt = """
I have to prepare for my {subjects} exams. I've completed {completeness:.2f}% of my curriculum. My motivation should be:
""".format(subjects=",".join(subjects.keys()), completeness=completeness)

response = client.chat_completion(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.01,
    max_tokens=50,
    seed=42,
)

print(response.choices[0].message.content)
