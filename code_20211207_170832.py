def load_document(filepath):
    try:
        article = {}
        with open(filepath, 'r', encoding='utf8') as f:
            Lines = f.readlines()
            for line in Lines:
                arr = line.split("\t")
                article_id = int(arr[0])
                arr = arr[1].split(" ")
                article_name = arr[0]
                article_content = ""
                for x in range(1, len(arr)):
                    arr[x].strip()
                    if len(arr[x]) != 0 and x != len(arr)-1:
                        article_content += arr[x]+" "
                    elif len(arr[x]) != 0 and x == len(arr)-1:
                        article_content += arr[x][:-1:]
                article[article_id] = article_name+" "+article_content
        return article
    except ValueError:
        print("Error!")


def build_inverted_index(articles):
    word_dic = {}
    for x in articles:
        temp = articles[x].split(" ")
#         print(temp)
        for i in temp:
            if i not in word_dic:
                word_dic[i] = set([x])
            else:
                word_dic[i].add(x)
    return word_dic
