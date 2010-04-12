from jargon_data import links
import re
import webbrowser

def find(word, lnks=links):
    """lookup word in the Hacker Jargon File.  Returns a list of results."""
    regex = re.compile(word.lower())
    try: it = lnks.iteritems()
    except:
        it=iter(lnks)
    return sorted(((title,link) for title, link in it if regex.search(title)),
                    key = lambda t: t[0])

def go(word,lnks=links):
    """Looks up word in the Jargon File, opens first result.
    Returns True on sucess, False on no results"""
    res = find(word, lnks)
    if len(res) == 1:
        webbrowser.open(res[0][1])
        return True
    return res

def main(word, lnks=links):
    res = go(word,lnks)
    if res is True: return 
    for n, (title, url) in enumerate(res):
        print "%s: %s" % (n+1, title)
    prompt = "\nPick a number, or enter a more precise search term: "
    numberOfResults = len(res)
    while True:
        inp = raw_input(prompt) if sys.version_info < (3,) else input(prompt)
        try:
            i = int(inp)
            if i < 1: raise IndexError
            link = res[i-1]
        except ValueError:
            main(inp, res)
            return
        except IndexError:
            print "Number out of range, must be between 1 and %s" % numberOfResults
        else:
            webbrowser.open(link[1])
            


if __name__ == "__main__":
    import sys
    try:
        main(" ".join(sys.argv[1:]))
    except KeyboardInterrupt:
        print
        