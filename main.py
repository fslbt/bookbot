from stats import * 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents


if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    

    map={}

    content=None
    content=get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    countwords(content)
    print("--------- Character Count -------")
    map=(charactermap(content.lower()))
    sort_dict(map)
    print("============= END ===============")
