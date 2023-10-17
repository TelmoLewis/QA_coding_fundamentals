data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
import statistics
grades = data.split(",")
grades = list(map(int, grades))

print("Minimum grade is:", min(grades))
print("Maximun grade is:", max(grades))

# Calculate the average of the grades
average_grade = sum(grades) / len(grades)

# Round the average to 2 decimal places
average_grade = round(average_grade, 2)

print("Average grade is:", average_grade)



# Calculate the mean (average) using the statistics.mean() function
mean_grade = statistics.mean(grades)

# Calculate the median using the statistics.median() function
median_grade = statistics.median(grades)
print("Median grade is:", median_grade)

# Calculate the minimum and maximum
min_grade = min(grades)
max_grade = max(grades)

# Format and display the values using str.format()
output = "Minimum grade: {}, Maximum grade: {}, Mean (average): {:.2f}, Median: {:.2f}".format(
    min_grade, max_grade, average_grade, median_grade
)

print(output)
