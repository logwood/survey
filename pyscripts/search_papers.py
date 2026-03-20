import urllib.request
import json
import urllib.parse

queries = [
    'MimicGen Mandlekar',
    'Scaling Robot Learning with Semantic Imagination Ha',
    'GenSim Wang',
    'Manipulate-Anything Deng',
    'RoboGen Wang',
    'SkillMimicGen',
    'DemoGen Xue',
    'IntervenGen Li',
    'MoMaGen Gu',
    'R2RGen Zhang',
    'HumanoidGen'
]

for q in queries:
    url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=' + urllib.parse.quote(q) + '&limit=3&fields=title,authors,year,abstract'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f'\n--- Query: {q} ---')
            if data.get('data'):
                for paper in data['data']:
                    authors = ', '.join([a['name'] for a in paper.get('authors', [])])
                    print(f"Title: {paper.get('title')}")
                    print(f"Authors: {authors}")
                    print(f"Year: {paper.get('year')}")
                    abstract = paper.get('abstract')
                    print(f"Abstract: {abstract[:500] if abstract else 'None'}...")
            else:
                print('No results found.')
    except Exception as e:
        print(f'Error searching {q}: {e}')
