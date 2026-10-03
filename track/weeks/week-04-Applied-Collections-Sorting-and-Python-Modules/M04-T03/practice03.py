# Sort Student Marks in Different Orders

n = int(input())
marks = list(map(int, input().split()))

# Write your code here
asc_marks = sorted(marks)
desc_marks = sorted(marks, reverse = True)

print(*asc_marks)
print(*desc_marks)