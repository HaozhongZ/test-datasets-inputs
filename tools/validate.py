from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]
base=root/'suites'/'infographic'/'v1.0.0'
manifest=json.loads((base/'manifest.json').read_text())
items=json.loads((base/'input.json').read_text())
n=manifest['case_count']
assert len(items)==n
assert [x['id'] for x in items]==[f'BLD-{i:03d}' for i in range(1,n+1)]
assert len({x['source_id'] for x in items})==n
assert len({json.dumps(x['table'],ensure_ascii=False,sort_keys=True) for x in items})==n
assert all(set(x)=={'id','source_id','user_question','table'} for x in items)
assert all(set(x['table'])=={'headers','rows'} and all(len(r)==len(x['table']['headers']) for r in x['table']['rows']) for x in items)
assert not any(re.search(r'柱状图|条形图|折线图|环形图|饼图|矩形树图|时间轴|图表|四宫格|框选',x['user_question']) for x in items)
print(f'PASS: {n} unique blind-test inputs')
