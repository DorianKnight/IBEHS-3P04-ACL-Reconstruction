from os import listdir
from os.path import isfile, join
anglefiles = ['sebt/' + f for f in listdir('sebt') if isfile(join('sebt', f))]
CofMfiles = ['CofM_images/' +
             f for f in listdir('CofM_images') if isfile(join('CofM_images', f))]


print(anglefiles)
print(CofMfiles)
