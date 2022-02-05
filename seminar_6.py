import collections

with open('nginx_logs.txt', "r", encoding='utf-8') as f:
    pars = [(line.split()[0], line.replace('"', '').split()[5], line.split()[6]) for line in f]
    #print(*pars)
parses = collections.Counter(pars).most_common(1)
print(parses)

    # for i in range(6):
    #     print(pars[i])


