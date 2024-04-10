import itertools
import json

c = json.load(open("config.json"))

ex = c["exercises"]["practice"]

ex.sort(key=lambda it: (it["difficulty"], len(it["prerequisites"]), it.get("status")))

for key, items in itertools.groupby(ex, key=lambda it: it["difficulty"]):
    print (f"\n### Difficulty: {key}\n")
    for it in items:
        print(f"- [{it['name']}](practice/{it['slug']})", end='')
        ## print(", ".join(it['prerequisites']), end='')
        status = it.get('status', '')
        if status:
            print(f" *{status}*", end='')
        print()
