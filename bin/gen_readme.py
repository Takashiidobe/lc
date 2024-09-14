#!/usr/bin/env python3

import subprocess

commit_messages = subprocess.run(["git", "log", "--oneline"], stdout=subprocess.PIPE)
lines = [l.decode("utf-8").split(" ") for l in commit_messages.stdout.splitlines()]

parsed = [(commit_hash, *rest) for commit_hash, *rest in lines]

filtered = []

for commit_hash, *rest in parsed:
    if not rest[0][0].isdigit():
        continue
    int_val = int(float(rest[0] + "0"))
    filtered.append((int_val, commit_hash, rest[0] + " " + " ".join(rest[1:])))

filtered.sort()

print("# Leetcode\n")
for _, commit, body in filtered:
    print(f"- [{body}](https://github.com/Takashiidobe/lc/commit/{commit})")
