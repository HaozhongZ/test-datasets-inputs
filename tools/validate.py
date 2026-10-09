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
print(f'PASS: infographic {n} unique blind-test inputs')

base=root/'suites'/'merger-video'/'v1.0.0'
manifest=json.loads((base/'manifest.json').read_text())
items=json.loads((base/'input.json').read_text())
n=manifest['case_count']
assert manifest['suite']=='merger-video'
assert len(items)==n
assert [x['id'] for x in items]==[f'merger-{i:03d}' for i in range(1,n+1)]
assert all(set(x)=={'id','title','source_file','input','original_markdown'} for x in items)
assert all(set(x['input'])=={'annotated_script','references','plain_script'} for x in items)
assert not re.search(r'/Users/|/home/[^/]+/', (base/'input.json').read_text())
print(f'PASS: merger-video {n} inputs')

base=root/'suites'/'html-chart-animation'/'v1.0.0'
manifest=json.loads((base/'manifest.json').read_text())
items=json.loads((base/'input.json').read_text())
n=manifest['case_count']
assert manifest['suite']=='html-chart-animation'
assert len(items)==n
ids=[x['id'] for x in items]
assert len(set(ids))==n
assert all(re.fullmatch(r'(?:case|rem)-\d{3}', x) for x in ids)
assert {p:sum(x.startswith(p+'-') for x in ids) for p in ('case','rem')}==manifest['id_prefix_counts']
assert all(set(x)=={'id','input'} for x in items)
assert all(set(x['input'])=={'intent','narration','tables'} for x in items)
assert all(isinstance(x['input']['intent'],str) and isinstance(x['input']['narration'],str) and isinstance(x['input']['tables'],list) and x['input']['tables'] for x in items)
assert all(isinstance(t.get('rows'),list) and t['rows'] for x in items for t in x['input']['tables'])
print(f'PASS: html-chart-animation {n} inputs')
