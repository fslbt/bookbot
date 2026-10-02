
def countwords(content):
    new_content=content.split()
    size=int(len(new_content))
    print(f"Found {size} total words")

def charactermap(content):
    hashmap={}
    for word in content:
        if word in hashmap:
            hashmap[word]=hashmap.get(word,0)+1
        else:
            hashmap[word]=1
    return hashmap


def sort_on(map):
    return map["num"]

def dict_list(map):
    result=[]
    for key,value in map.items():
        result.append({"char":key,"num":value})
    return result

def sort_dict(map):
    list=dict_list(map)
    list.sort(reverse=True,key=sort_on)
    for data in (list):
        if data["char"].isalpha():
            print(f"{data['char']}: {data['num']}")

