from pprint import pprint


clients = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for fr_line in fr:
        client = fr_line.split(' ')[0]
        clients.update({client: clients.get(client, 0) + 1})
spammer, *other = sorted(clients.items(), key=lambda i: i[1], reverse=True)

pprint(spammer)
