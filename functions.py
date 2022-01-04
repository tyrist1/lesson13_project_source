import json

def read_json(file):
    with open(file, encoding='UTF-8') as f:
        return json.load(f)
# read_json('posts.json')

def get_tags(data):
    results = set()

    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results

def get_post_by_tag(data, tag):
    results = []
    for record in data:
        if f'#{tag}' in record['content']:
            results.append(record)
    return results

def add_post(file, post):
    data = read_json(file)
    data.append(post)
    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)

