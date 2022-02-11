import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as r:
    for i in r:

        parse_2 = re.compile(r'([\w\.\+\:\/]+)')

        a = parse_2.findall(i)

        #b = str(a).replace('', "-").replace('-','')
        print((a[0], a[1] + " " + a[2], a[3], a[4], a[5], a[6], a[7],))