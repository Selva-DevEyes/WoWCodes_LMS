import ast

filepath = "app/seed/data/WoWCodes_WoWCodes_data.py"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines:", len(lines))

for idx, line in enumerate(lines, 1):
    if line.strip() == '""",':
        print(f"Closing quote on line {idx}")
    elif line.strip() == '),':
        print(f"Closing tuple on line {idx}")
