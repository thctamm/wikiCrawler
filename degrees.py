import requests, string, json, re, sys, csv, random


def main(arg1, arg2, arg3):
    printable = set(string.printable)
    url = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles="
    def callback(response):
        found_links = []
        if response:
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
                                        found_links.append(parsed_link)
        return found_links

    input_files = []
    target = ""
    with open(arg2, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i, row in enumerate(reader):
            if i == 0:
                target = row[0]
            else:
                input_files.append(row)

    target_links = []
    for level in input_files:
        level_links = []
        for inp_file in level:
            with open(inp_file, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in reader:
                    level_links += row
        target_links.append(level_links)

    iters = int(arg3)
    total_dist = 0
    shortest_path = []
    for i in range(iters):
        current_page = arg1
        last_page = current_page
        path = [current_page]
        dist = 1
        not_found = True
        while not_found:
            print("Exploring: " + current_page)
            found = False
            current_links = callback(requests.get(url+current_page))
            if target in current_links:
                path.append(target)
                if len(shortest_path) == 0 or len(shortest_path) > len(path):
                    shortest_path = list(path)
                total_dist += dist
                path_str = "Found path: "
                for el in path:
                    path_str = path_str + el + " -> "
                print(path_str[:len(path_str)-4])
                not_found = False
            for level in target_links:
                intersection = set(level).intersection(current_links) - set(path)
                if len(intersection) >= 1:
                    found = True
                    current_page = random.sample(intersection, 1)[0]
                    path.append(current_page)
                    dist +=1
                    break;
            if not found :
                if len(set(current_links) - set(path)) <= 0:
                    path = list(path[:-1])
                    if len(path) == 0:
                        found = True
                    current_page = path[-1]
                else:
                    current_page = random.sample(set(current_links), 1)[0]

    print("Average path from " + arg1 + " to " + target + " is " + str(total_dist/iters))
    print("The shortest path we found is: ")
    path_str = ""
    for el in shortest_path:
        path_str = path_str + el + " -> "
    path_str = path_str[:len(path_str)-4]
    print(path_str)
    return {'path': path_str, 'avg': float(total_dist)/float(iters)} 

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
