import os


#
# constants 
#

template = """
javadoc \\
  -doclet $DOCLET \\
  -docletpath $doclet_path \\
  -cp '' \\
  -sourcepath {placeholder} \\
  -subpackages me.ele \\
  -commit $sha \\
  -author $mail \\
  -message $message
rm -rf nirvana-bluray/
"""

base = '''
# prepare parma
sha=$(git rev-parse HEAD)
message=$(git log --format=%B -n 1 | base64 | tr -d '\n')
mail=$(git --no-pager show -s --format='%an <%ae>' HEAD | base64 | tr -d '\n')
echo $sha $message $mail
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8

# prepare generator
git clone git@git.elenet.me:napos.backend/nirvana-bluray.git
cd nirvana-bluray
gradle clean build
doclet_path=./nirvana-bluray/build/libs/nirvana-bluray.jar:$(cat docletClassPath)
DOCLET=me.ele.napos.nirvana.bluray.DocLet
echo $doclet_path
cd ..

'''

def suffix_tester(item, suffix):
    if len(item) > len(suffix) and item[len(item) - len(suffix):] == suffix:
        return True
    return False

def get_descriptors():
    java_list = []
    for root, sub_dir, files in os.walk(os.getcwd()):
        if suffix_tester(root, 'src/main/java'):
            java_list.append(root)
    descriptor_list = []
    for java in java_list:
        if 'descriptor' in java:
            descriptor_list.append(java)
    if len(descriptor_list) == 0:
        return java_list
    return descriptor_list

def generate_sh():
    descriptors = get_descriptors()
    f = open('./generate_doc.sh', 'w')
    f.write(base)
    for descriptor in descriptors:
        f.write(template.replace('{placeholder}', descriptor))
    f.close()

if __name__ == '__main__':
    generate_sh()

