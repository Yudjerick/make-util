import sys
import os
import hashlib
import json

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Invalid argument")
        sys.exit()
    else:
        target = sys.argv[1]

if('Makefile' in os.listdir()):
    makefile = open('Makefile').read()
else:
    print('Makefile not found')
    sys.exit()
    
makefilejson = {}
phonylist = []

for i in makefile.split('\n'):
    if len(i) == 0:
        continue
    if i.startswith('    ') or i[0] == '\t':
        makefilejson[cur_target]["commands"].append(i.replace('    ','').replace('\t',''))
    elif i.split()[0].replace(':','') == '.PHONY':
        phonylist = i.split(':')[1].split(' ')
    else:    
        cur_target = i.split()[0].replace(':','')
        dependencies = i.split()
        dependencies.pop(0)
        if(':' in dependencies):
            dependencies.remove(':')
        makefilejson[cur_target] = {"commands" : [], "dependencies": dependencies}

if('hashes.txt' in os.listdir()):
    fileshashes = json.loads(open('hashes.txt').read())
else:
    fileshashes = {}

def make(target):
    if(target in phonylist):
        for i in makefilejson[target]["commands"]:
            os.system(i)
        return True
    need_to_change = False
    for i in makefilejson[target]["dependencies"]:
        r = make(i)
        if(not(need_to_change)):
            need_to_change = r
    if target in os.listdir() and target in fileshashes and not(need_to_change):
        if hashlib.sha1(open(target).read().encode()).hexdigest() == fileshashes[target]:
            return False
    for i in makefilejson[target]["commands"]:
        os.system(i)
    if target in os.listdir():
        fileshashes[target] = hashlib.sha1(open(target).read().encode()).hexdigest()
    return True

updated = make(target)
if not(updated):
    print("'" +target + "' is up to date")
f = open('hashes.txt', 'w')
f.write(json.dumps(fileshashes))