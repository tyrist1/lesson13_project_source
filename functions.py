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


