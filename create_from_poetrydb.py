import requests 
"""
Write all the poems in the poetry db that have between 2 and 16 lines to separate text files.
"""
for i in range(2,16):
    r =requests.get(f"https://poetrydb.org/random,linecount/100;{i}/author,title,lines")
    poems = r.json()
    for p in poems:
        if p['author'] == 'Emily Dickinson':
            continue
        title = list(p['title'])
        while ':' in title:
            title.remove(':')
        while '"' in title:
            title.remove('"')
        while '?' in title:
            title.remove('?')
        while '-' in title:
            title.remove('-')
        title = ''.join(title)
        try:
            f = open(f"{title} - {p['author']}.txt",'x')
        except FileExistsError:
            print('file already exists' + title)
            continue
        f.write(f"{p['title']} - {p['author']}")
        for l in p['lines']:
            if len(l) > 0:
                f.write('\n')
                try:
                    f.write(l)
                except UnicodeEncodeError: 
                    continue
        f.close()
