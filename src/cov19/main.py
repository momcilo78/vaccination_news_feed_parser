#! /usr/bin/env python
# encoding: utf-8
'''
cov19.main -- Tool for extraction of online article data about vaccination

cov19.main is a a simple tool combining beatifulsoup4 with regex to extract information about web site. For each site appropriate classes have to be implemented separately.

@author:     Momcilo Majic

@copyright:  2021 organization_name. All rights reserved.

@license:    GNU GENERAL PUBLIC LICENSE Version 3

@contact:    momcilo@majic.rs
@deffield    updated: Updated
'''

import sys
import os
from googletrans import Translator

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from cov19.vaccination.parsers import ParserFactory
from cov19.vaccination.templates import TemplateFactory

import requests

__all__ = []
__version__ = 0.1
__date__ = '2021-03-16'
__updated__ = '2021-03-16'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def process_direct_url(args):
    try:
        # create parsers based on URL
        parser = ParserFactory.create_parser(args.url)
        print(f'URL will be processed by {parser.__class__.__name__}')
        # instantiate template generator
        template = TemplateFactory.create_template(args.template)
        # download the URL
        r = requests.get(args.url)
        if r.status_code != 200:
            raise Exception(f"Unable to retrieve URL: {args.url}")
        # parse for results
        result = parser.parse_html(r.text)
        result['url'] = args.url
# TODO: wait until the upstrea issue with google translator gets resolved, https://github.com/ssut/py-googletrans/issues/234    
#         # translate into english
#         translator = Translator()
#         translation = translator.translate(result['sentence'], src='sr', dest='en')
#         result['translation']  = translation 
        # generate the result
        text = template.generate(result)
        print(text)
    except Exception as e:
        print(e)
def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by Momcilo Majic on %s.
  GNU GENERAL PUBLIC LICENSE Version 3

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        executors = {}

        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        common_arguments_parser = ArgumentParser(add_help=False)
        common_arguments_parser.add_argument('--dry-run', action='store_true', help='designates if dry run is to be executed. The tool should not change anything. Warning: this feaature is still not fully implemented!')        
        common_arguments_parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        subparsers  = parser.add_subparsers(help='sub-command help', dest="subparser_name")

        parser_process_direct_url = subparsers.add_parser('processDirectURL', help='', parents=[common_arguments_parser])
        parser_process_direct_url.add_argument('--url', required=True, help='url to be processed, tool will determine if it is able to parse it.')
        parser_process_direct_url.add_argument('--template', default='human', required=False, help='template generator (default is %(default)s) to be used for output', choices=[current.name for current in TemplateFactory.templates ])        
        executors[parser_process_direct_url.prog.split(' ')[-1]] = process_direct_url
        
        parser.add_argument('-V', '--version', action='version', version=program_version_message)

        # Process arguments
        args = parser.parse_args()

        executor = executors[args.subparser_name]
        # execute command
        return executor(args)
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
#     except Exception as e:
#         if DEBUG or TESTRUN:
#             raise(e)
#         indent = len(program_name) * " "
#         sys.stderr.write(program_name + ": " + repr(e) + "\n")
#         sys.stderr.write(indent + "  for help use --help")
#         return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'cov19.main_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())