#! /usr/bin/env python3
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
import traceback
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

def process_direct_url(args):
    try:
        # create parsers based on URL
        parser = ParserFactory.create_parser(args.url)
        print(f'URL will be processed by {parser.__class__.__name__}')
        # instantiate template generator
        template = TemplateFactory.create_template(args.template)
        # download the URL
        print(f'Downloading... {args.url}')
        r = requests.get(args.url)
        if r.status_code != 200:
            raise Exception(f"Unable to retrieve URL: {args.url}")
        # parse for results
        print("Parsing...")
        result = parser.parse_html(r.text)
        result['url'] = args.url
        if result['valid']:
            # TODO: wait until the upstream issue with google translator gets resolved, https://github.com/ssut/py-googletrans/issues/234
            # translate into english
            translator = Translator()
            translation = translator.translate("".join(result['quoted_text']), src='sr', dest='en')
            result['translation']  = translation.text
            # generate the result
            text = template.generate(result)
            print('----------------------------------------------')
            print(text)
            print('----------------------------------------------')
        else:
            print('Result is invalid')
    except Exception as e:
        print(e)
        traceback.print_exc()

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
    program_shortdesc = 'cov19.main -- Tool for extraction of online article data about vaccination'
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
#         indent = len(program_name) * " "
#         sys.stderr.write(program_name + ": " + repr(e) + "\n")
#         sys.stderr.write(indent + "  for help use --help")
#         return 2

if __name__ == "__main__":
    sys.exit(main())
