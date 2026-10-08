import os
import json
import requests
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
default_scores_file = os.path.join(base_dir, "scores.json")
chart_output_file = os.path.join(base_dir, "student_scores.png")

url = input("Enter the API URL (press Enter to use local 'scores.json'): ").strip()

try:
    if not url or not url.startswith(("http://", "https://")):
        data_file = url if (url and os.path.exists(url)) else default_scores_file
        print(f"Loading student dataset from: {data_file}")
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print("Could not get student data from API.")
            data = []
        else:
            data = response.json()

        students = []
        marks = []

        for student in data:
            if "student" in student and "marks" in student:
                students.append(student["student"])
                marks.append(float(student["marks"]))

        if not marks:
            print("No student data found.")
        else:
            average = sum(marks) / len(marks)

            print("\nStudent Scores")
            print("-" * 30)

            for name, mark in zip(students, marks):
                print(name, ":", mark)

            print("\nClass Average:", round(average, 2))

            colors = [
                "green" if mark >= average else "red"
                for mark in marks
            ]

            plt.figure(figsize=(8, 5))
            plt.bar(students, marks, color=colors)

            plt.axhline(
                average,
                color="black",
                linestyle="--",
                label="Class Average"
            )

            plt.xlabel("Students")
            plt.ylabel("Marks")
            plt.title("Student Test Scores")
            plt.legend()

            plt.tight_layout()
            plt.savefig(chart_output_file)
            plt.show()

except requests.RequestException as error:
    print("Error while getting data:", error)

except ValueError:
    print("The API returned invalid data.")