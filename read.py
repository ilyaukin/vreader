import vobject
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file', help='File to read')
parser.add_argument('--outfile', help='File to output')
parser.add_argument('--hasattr', help='Filter cards only has specified attribute')
args = parser.parse_args()
file = open(args.file, 'r')
outfile = None
if args.outfile:
    outfile = open(args.outfile, 'w')
filter_attr = args.hasattr
for v in vobject.readComponents(file):
    if filter_attr:
        if not hasattr(v, filter_attr):
            continue
    if outfile:
        outfile.write(v.serialize())
    v.prettyPrint()