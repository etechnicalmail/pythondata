from urllib.request import  urlopen
"""
this is a module to fetch text from website
"""
def fetch_module():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
            story_words = []
            for line in story:
                    line_words = line.decode('utf-8').split()
                    for word in line_words:
                            story_words.append(word)
    for word in story_words:
        print(word)


if __name__ == '__main__':
    fetch_module()
