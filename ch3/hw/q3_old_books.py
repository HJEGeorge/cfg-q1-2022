"""
Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
quickly categorise books by the century and decade that they were written.
Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth
Century, Seventies")
"""
year = input("What year was the book written in?\n")

if len(year) != 4:
    print("Please enter a 4 digit number representing the year the book was written, eg. 1901")

if int(year) > 1950 or int(year) < 1800:
    print("Please enter a year between 1800 and 1950")

century = year[0:2]
decade = year[2]

tags = []

# Set century
if century == "18":
    tags.append("Eighteenth Century")
elif century == "19":
    tags.append("Nineteenth Century")

# Set decade
decades = {
    "0": "Noughties",
    "1": "Tens",
    "2": "Twenties",
    "3": "Thirties",
    "4": "Fourties",
    "5": "Fifties",
    "6": "Sixties",
    "7": "Seventies",
    "8": "Eighties",
    "9": "Nineties"
}

tags.append(decades[decade])

print(", ".join(tags))
