import argparse
import secrets
import string
from sys import exit

parser = argparse.ArgumentParser(description="Random password generator")

parser.add_argument('-n',
                    dest='num_passwords',
                    type=int,
                    default=1,
                    help='Number of passwords to generate (default is 1)')
parser.add_argument('-l',
                    dest='length',
                    type=int,
                    default=16,
                    help='Length of passwords (default is 16 characters)')
parser.add_argument('-nl',
                    dest='include_lowercase',
                    action='store_false',
                    help='Do not include lowercase characters')
parser.add_argument('-nu',
                    dest='include_uppercase',
                    action='store_false',
                    help='Do not include uppercase characters')
parser.add_argument('-nd',
                    dest='include_digits',
                    action='store_false',
                    help='Do not include numerical characters')
parser.add_argument('-np',
                    dest='include_punctuation',
                    action='store_false',
                    help='Do not include punctuation marks')

args = parser.parse_args()

#Error handling in case all arguments are expressed
if not args.include_uppercase and not args.include_lowercase and not args.include_digits and not args.include_punctuation:
    print("You must include at least one character set to generate a password.")
    exit(0)

#Creating desired character set
alphabet = ''
if args.include_lowercase:
    alphabet += string.ascii_lowercase
if args.include_uppercase:
    alphabet += string.ascii_uppercase
if args.include_digits:
    alphabet += string.digits
if args.include_punctuation:
    alphabet += string.punctuation

for number_of_passwords in range(args.num_passwords):
    print("".join(secrets.choice(alphabet) for i in range(args.length)))
