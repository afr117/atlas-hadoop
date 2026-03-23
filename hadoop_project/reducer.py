#!/usr/bin/python3

import sys

top = []


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split('\t')
    if len(parts) != 2:
        continue

    emp_id = parts[0]
    rest = parts[1].split(',')
    if len(rest) != 2:
        continue

    company = rest[0]
    try:
        salary = float(rest[1])
    except ValueError:
        continue

    top.append((salary, emp_id, company))
    top = sorted(top, reverse=True)[:10]

print("id\tSalary\tcompany")
for salary, emp_id, company in top:
    print("{}\t{}\t{}".format(emp_id, salary, company))
