#!/usr/bin/env python
from script import path, shell, opts
import script

script.doc.purpose = \
    'How many flac files in ~/Music/flac belong to GENRE?'
script.doc.args = 'GENRE'
opts.add('verbose')

def main():
    if len(script.args) != 1:
        script.exit(1, 'Please specify GENRE (or run with --help)')
    genre = script.args[0].lower()
    count = 0
    root = path('~/Music/flac')
    if opts.verbose: print('scanning', root)
    for parent, dirs, files in root.walk('*.flac'):
        for file in files:
            cmd = 'metaflac --show-tag=GENRE ' + path(parent/file).sh
            result = shell(cmd, stdout='PIPE').stdout
            if genre == result.lstrip('GENRE=').rstrip().lower():
                count += 1
    print('found {} {} files'.format(count, genre))

if __name__ == '__main__': script.run(main)


