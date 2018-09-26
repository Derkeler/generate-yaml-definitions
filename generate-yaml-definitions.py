#!python2

from vocabulary.vocabulary import Vocabulary as vb
import sys, getopt, htmllib
import json


def usage():
    print """\
    Usage: generate-definitions [OPTIONS]
         -h                    Display this message
         -i inputfile.txt      Specifies input text file
         -o outputfile.yml     Specifies output YAML file
    """

def fix(s):
   s = s.replace('&quot;', '')
   s = s.replace('<i>', '')
   s = s.replace('</i>', '')
   s = s.replace(r'&#39;', "")
   s = s.replace(':', ';')
   return s

def main(argv):
    
    #vocabList = open("vocabList.txt", "r")
    #yamlOut = open("yamlOut.txt", "w+")

    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["help","ifile=","ofile="])
    except:
        usage()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-i", "--ifile"):
            vocabInput = open(arg, "r")
        elif opt in ("-o", "--ofile"):
            yamlOut = open(arg, "w+")
    
    
    for line in vocabInput.read().splitlines():
        # try:
        #print (str(vb.meaning(line)))
        yamlOut.write("\n-")
        yamlOut.write("\n topic: " + line.strip())
        print line
        vocabDefDict = json.loads(vb.meaning(line.strip()))
        yamlOut.write("\n content: " + fix(str(vocabDefDict[0]['text'])))
        # except Exception:
        #     yamlOut.write("\n content: " + "error")
        #     # exc_type, exc_value, exc_traceback = sys.exc_info()
        #     # traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        #     # traceback.print_exception(exc_type, exc_value, exc_traceback,
        #     #                           limit=2, file=sys.stdout)
        #     # traceback.print_exc()
        #     #
        #     # print repr(traceback.extract_tb(exc_traceback))
        #     # print repr(traceback.format_tb(exc_traceback))
        #
        # #print (vocabDefDict[0]['text'])

    yamlOut.close()


if __name__ == "__main__":
    main(sys.argv[1:])
