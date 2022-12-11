from mdx_utils.base.readmdict import MDX
from mdx_utils.reader import get_record
import os
from shutil import copyfile

dict = 'OALD9EnEn.mdx'
words = 'top10k.txt'
dst = '../words'
invalid = ['con']

if __name__ == '__main__':
    mdx = MDX(dict, '', False, None)
    top10k = [line.rstrip('\n') for line in open('top10k.txt')]
    record = None
    found = True
    if os.path.exists(dst) == False:
        os.mkdir(dst)
    copyfile('OALD9EnEn.css', '%s/OALD9EnEn.css' % dst)

    for i in range(len(top10k)):
        break;
        if i % 1000 == 0:
            print(i)
        word = top10k[i]
        found = False
        record = []
        for idx in range(len(mdx._key_list)):
            offset, key = mdx._key_list[idx]
            if key == word.encode('UTF-8'):
                found = True
                length = -1
                if (idx + 1) < len(mdx._key_list):
                    length = mdx._key_list[idx + 1][0] - offset
                record.append(get_record(mdx, key, offset, length))
        if word in invalid:
            word = '%s1' % word
        with open('%s/%s.html' % (dst, word), 'w', encoding="utf-8") as out:
            if (found):
                record = '\n---\n'.join(record)
                out.write('%s' % record)

    with open('../top10k.md', 'w', encoding="utf-8") as out:
        for word in top10k:
            word1 = word
            if word in invalid:
                word1 = '%s1' % word
            out.write('1. [%s](./words/%s.html)\n' % (word, word1))
    