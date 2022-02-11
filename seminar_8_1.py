import re

email = "asics1313@yandex.ru"

info = ['username', 'domain']


def email_parse(email):
    parse = re.compile(r'(^[\w\-]+)\@([\w]*\.[a-z]*$)')
    if parse.match(email) is None:
        raise ValueError(f'wrong email: {email}')
    else:
        result = parse.findall(email)
        return {f'username: {result[0][0]}, domain: {result[0][1]}'}

print(email_parse(email))

