#!/usr/bin/env python3

##rember to run pip install marvel

#Usage
from marvel import Marvel 

def main():
    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    #Keys
    m = Marvel(privkey,pubkey) #m=Marvel("PUBLIC_KEY","PRIVATE_KEY")
    name = "Captain" #string/ character name that begin with the specified string

    all_characters = m.characters.all(nameStartsWith=name) #nameStartsWith parameter

    print(all_characters)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    main()
