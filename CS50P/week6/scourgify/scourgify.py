import sys
import csv

# check the commond-line argument
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# create the empty list to append the readed row in it
student = []

# try to open the file
try:
    with open(sys.argv[1]) as file:
        with open(sys.argv[2], "w", newline="") as cfile:
            reader = csv.DictReader(file)
            for row in reader:
                student.append({"name": row["name"].split(","), "house": row["house"]})
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(cfile, fieldnames=fieldnames)

            # write the filed names on the top of the file
            writer.writeheader()
            for row in student:
                writer.writerow(
                    {
                        "first": row["name"][1].lstrip(),
                        "last": row["name"][0],
                        "house": row["house"],
                    }
                )
# exception if the file isn't exist
except:
    sys.exit(f"Could not read {sys.argv[1]}")
