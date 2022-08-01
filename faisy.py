import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from FLASTffs import super_fsl
    super_fsl()
elif bit == '32bit':
    exit('\x1b[1;91m\n\tOpps not upload')

