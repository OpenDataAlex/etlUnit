__author__ = 'coty'

import sys
import optparse


def main(argv):
    """
        This class is the entry point for the application. It takes the arguments, validates them, and passes
        them on to the appropriate classes to continue execution.

        There are three main functions of this application.
        1) Take in yaml
        2) Generate code from that yaml
        3) Execute that code so that we can take advantage of the unittest libraries
    """
    parser = optparse.OptionParser("usage: %prog [options]")

    # no arguments, print usage
    if len(argv) == 0:
        parser.print_usage()

    # all available options are defined here
    parser.add_option("-f", "--infile", dest="in_file", type="string", help="Specify the input file.")
    parser.add_option("-d", "--indir", dest="in_dir", type="string", help="Specify the input directory.")
    parser.add_option("-o", "--outdir", dest="out_dir", type="string", help="Specify the output directory.")
    parser.add_option("-g", "--gen", dest="gen_code", default=False, action="store_true",
                      help="Generate new test code.")
    parser.add_option("-e", "--exec", dest="exec_code", default=False, action="store_true",
                      help="Execute test code.")
    parser.add_option("-t", "--test", dest="test_run", default=False, action="store_true",
                      help="Run app as tests. Does not persist generated code or execute code.")
    (options, args) = parser.parse_args()

    # validating options
    if options.in_file and options.in_dir:
        parser.error("Options infile and indir are mutually exclusive. Please choose one.")

    if options.gen_code:
        from etlunit.yaml_reader import YAMLReader
        t = YAMLReader(options.in_file, options.in_dir)
        yaml_data = t.readTests()

        from etlunit.code_generator import CodeGenerator
        g = CodeGenerator(options.out_dir, yaml_data)
        # TODO: Decide if there should be a way to check if generated code should be updated or not.
        g.generateCode(options.test_run)

    if options.exec_code:
        from etlunit.code_executor import CodeExecutor
        e = CodeExecutor(options.out_dir)
        e.execute(options.test_run)

if __name__ == "__main__":
    main(sys.argv[1:])
