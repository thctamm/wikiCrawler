import grequests, string, json, re, csv, sys

def main(arg1, arg2):
    printable = set(string.printable)
    url = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles="
    target_links = []
    targets = []
    def callback(response):
        if response.ok:
            body = json.loads(response.text)
            if 'query' in body:
                if 'pages' in body['query']:
                    for key, page in body['query']['pages'].items():
                        if 'revisions' in page:
                            if '*' in page['revisions'][0]:
                                content = page['revisions'][0]['*']
                                links = re.findall(r"\[\[[^\[\]]+\]\]", content)
                                for link in links:
                                    parsed_link = link[2:-2].split('|')[0].replace(u'\u2013', '')
                                    parsed_link = filter(lambda x: x in printable, parsed_link)
                                    target_links.append(parsed_link)


    with open(arg1, 'rb') as csvfile:
        targetreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in targetreader:
            targets = row

    target_urls = []
    for target in targets:
        target_url = url + target
        target_urls.append(target_url)
    start = 0
    length = len(target_urls)
    while start < length:
        end = start + 50
        if end > length:
            end = length
        res = (grequests.get(u) for u in target_urls[start:end])
        results = grequests.map(res)
        for response in results:
            callback(response)
        start += 50

    with open(arg2, 'wb') as csvfile:
        linkwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
        linkwriter.writerow(target_links)


if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
