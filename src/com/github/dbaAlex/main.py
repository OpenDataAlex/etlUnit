__author__ = 'coty'

import sys
import optparse


def main(argv):
    parser = optparse.OptionParser("usage: %prog [options]")

    if len(argv) == 0:
        parser.print_usage()

    parser.add_option("-f", "--infile", dest="in_file", type="string", help="Specify the input file.")
    parser.add_option("-d", "--indir", dest="in_dir", type="string", help="Specify the input directory.")
    parser.add_option("-o", "--outdir", dest="out_dir", type="string", help="Specify the output directory.")
    parser.add_option("-g", "--gen", dest="gen_code", default=False, action="store_true",
                      help="Generate new test code.")
    parser.add_option("-e", "--exec", dest="exec_code", default=False, action="store_true",
                      help="Execute test code.")
    (options, args) = parser.parse_args()

    if options.in_file and options.in_dir:
        parser.error("Options infile and indir are mutually exclusive. Please choose one.")

if __name__ == "__main__":
    main(sys.argv[1:])
