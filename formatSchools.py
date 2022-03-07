schools = []
with open('schools.txt', encoding="utf8") as f:
    for line in f:
        schools = "<option value=\""+ line.rstrip() + "\">"

print(schools)