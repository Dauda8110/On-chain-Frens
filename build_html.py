import json

with open('nft_pool.json') as f:
    urls = json.load(f)

# Format as JavaScript array string
js_pool = '[\n    ' + ',\n    '.join(f'"{u}"' for u in urls) + '\n  ]'

with open('index_template.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('__JS_POOL__', js_pool)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Generated index.html successfully!')
