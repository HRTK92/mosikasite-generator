import re
import requests

query = input('Word: ')

print(f'{query}を検索します。')

res = requests.get(f'https://www.google.com/search?q={query}&hl=ja', headers={
                   'User-Agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36'})

print(res.status_code)

mosikasite = input('表示したい文字を入力してください: ')

html = res.text.replace('<div id="taw"><div><div></div></div>', f'''<div id="taw"><div><div><p class="gqLncc card-section KDCVqf Ww4FFb vt6azd" aria-level="3" role="heading"><spanclass="gL9Hy">もしかして:</span> <a class="gL9Hy" href="/search?hl=ja&amp;q={mosikasite}"><b>{mosikasite}</b></a></p></div></div>
''')

html = re.sub(r'href="/(.*?)"', r'href="https://www.google.com/\1"', html)
html = re.sub(r'src="/(.*?)"', r'src="https://www.google.com/\1"', html)


with open(f'output/{query} - {mosikasite}.html', 'w') as f:
    f.write(html)

print(f'output/{query} - {mosikasite}を作成しました。')
