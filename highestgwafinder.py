# 1. Open gwa.txt in read mode
myFile = open("gwa.txt", "r")

# 2. Set top_student as empty and highest_gwa as None
top_student = ""
highest_gwa = None

# 3. Loop through each line in gwa.txt
for line in myFile:
    # 3.1 Split the line by comma to get name and gwa
    parts = line.strip().split(",")
    name = parts[0]
    # 3.2 Convert gwa to float
    gwa = float(parts[1])

    # 3.3 If highest_gwa is None or current gwa is lower, update highest_gwa and top_student
    if highest_gwa is None or gwa < highest_gwa:
        highest_gwa = gwa
        top_student = name

# 4. Close the file
myFile.close()

# 5. Print the student with the highest GWA and their GWA
print("Student with highest GWA: " + top_student)
print("GWA: " + str(highest_gwa))
