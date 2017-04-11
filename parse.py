from optparse import OptionParser

def main():
    usage = "useage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-a", "--all", type="string", dest="search_and", help="find ALL lines in the file for the word1 AND word2")
    parser.add_option("-f", "--file", type="string", dest="filename", help="Name of file")
    (options, args) = parser.parse_args()

    if (options.search_and is None) or (options.filename is None):
        parser.error("not enough number of arguments")

    words = options.search_and.split(',')
    lines = open(options.filename).readlines()
    for idx, line in enumerate(lines):
        for word in words:
            if word.lower() in line.lower():
                print "The word, %s, was found at: Line %s" % (word, idx + 1)

if __name__ == "__main__":
    main()
