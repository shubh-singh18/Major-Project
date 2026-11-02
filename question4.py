# Question 4: Study Hours and Exam Results

# Chart Type: Scatter Plot

# A college wants to investigate whether students who study more hours tend to achieve higher marks.

# Dataset

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Student": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
#                 "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
#                 "Karan", "Meena"],
#     "Study_Hours": [1, 2, 3, 4, 5, 2, 6, 3, 7, 5, 8, 6],
#     "Marks": [28, 42, 50, 65, 78, 45, 88, 55, 96, 75, 98, 84],
#     "Attendance": [55, 65, 72, 80, 90, 68, 95, 75, 98, 88, 99, 92]
# }

# df = pd.DataFrame(data)

# Tasks

# 1. Calculate the average marks of all students.
# 2. Identify students who scored more than 80 marks.
# 3. Find the student who studied the most hours.
# 4. Create a scatter plot with study hours on the X-axis and marks on the Y-axis.
# 5. Customize the marker color, shape, and size.
# 6. Set the X-axis limit from 0 to 10 and the Y-axis limit from 0 to 100.
# 7. Add a title, axis labels, and grid.
# 8. Analyze whether the data suggests a relationship between study hours and marks.


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
                "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
                "Karan", "Meena"],
    "Study_Hours": [1, 2, 3, 4, 5, 2, 6, 3, 7, 5, 8, 6],
    "Marks": [28, 42, 50, 65, 78, 45, 88, 55, 96, 75, 98, 84],
    "Attendance": [55, 65, 72, 80, 90, 68, 95, 75, 98, 88, 99, 92]
}

df = pd.DataFrame(data)
print(df)
a=df["Marks"].mean()
print(a)
b=df[df["Marks"]>80]
print(b)
c=df.loc[df["Study_Hours"].idxmax()]
print(c)
plt.scatter(df["Study_Hours"],df["Marks"],color="red",marker="x")
plt.yticks(range(0,110,10))
plt.title("Study Hours and Exam Results",color="navy",fontsize=20)
plt.xlabel("Study_Hours",color="orange",fontsize=15)
plt.ylabel("Marks",color="orange",fontsize=15)
plt.grid()
plt.show()