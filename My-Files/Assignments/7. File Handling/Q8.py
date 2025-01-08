# 8.	Write a program that renames a specified file. The user should provide the current filename and the new filename.

import os

of = input('Enter Old File Name for Rename: ')
nf = input('Enter New File Name to Rename:')

if os.path.exists(of):
    os.rename(of, nf)
    print(f'File {of} is Renamed as {nf}')

else:
    print(f'File {of} does not Exist')