# CSV means: Comma Separated Values

# Looks like:
# name,age
# Roman,19
# Hari,20

# Used for:
# spreadsheets
# datasets
# exports/imports


# Writing CSV
# import csv

# data = [
#     ["name", "age"],
#     ["Roman", 19],
#     ["Hari", 20]
# ]

# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)

#     writer.writerows(data)

#     Reading CSV
# import csv

# with open("data.csv", "r") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

# # Output:

# # ['name', 'age']
# # ['Roman', '19']
# # ['Hari', '20']
# CSV Dict Reader
# Better approach.
# import csvwith open("data.csv", "r") as f:    reader = csv.DictReader(f)    for row in reader:        print(row)
# Output:
# {'name': 'Roman', 'age': '19'}

# CSV Dict Writer
# import csvdata = [    {"name": "Roman", "age": 19},    {"name": "Hari", "age": 20}]with open("data.csv", "w", newline="") as f:    fields = ["name", "age"]    writer = csv.DictWriter(f, fieldnames=fields)    writer.writeheader()    writer.writerows(data)

# Real Backend Usage

# CSV:

# exports
# reports
# analytics
# datasets

# JSON:

# APIs
# configs
# web applications
# AI systems