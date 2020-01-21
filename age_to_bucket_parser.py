import json
import yaml
with open('hw.json') as hw_json_file:
    json_data = json.load(open('hw.json'))
ppl_age = json_data['ppl_ages']
age_buckets = json_data['buckets']
age_limits = [max(ppl_age.values())+1]
age_buckets.extend(age_limits)
age_buckets.sort()
ppl_groups = []
for age in range(len(age_buckets) - 1):
    names = []
    for name in ppl_age:
        if ppl_age[name] >= age_buckets[age]:
            if ppl_age[name] < age_buckets[age + 1]:
                names.append(name)
    ppl_groups.append({str(age_buckets[age]) + "-" + str(age_buckets[age + 1]): names})
print(yaml.dump(ppl_groups))