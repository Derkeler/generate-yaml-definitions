#!python3

from vocabulary.vocabulary import Vocabulary as vb
import sys, getopt
import json


def usage():
    print ("""\
    Usage: generate-definitions [OPTIONS]
         -h                    Display this message
         -i inputfile.txt      Specifies input text file
         -o outputfile.yml     Specifies output YAML file
    """)

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
        
        vocabDefDict = json.loads(vb.meaning(line))
        yamlOut.write("\n-")
        yamlOut.write("\n topic: " + line)
        yamlOut.write("\n content: " + str(vocabDefDict[0]['text']))
        
        
        #print (vocabDefDict[0]['text'])
    yamlOut.close()


if __name__ == "__main__":
    main(sys.argv[1:])
