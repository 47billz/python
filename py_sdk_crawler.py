import glob
import pprint

report = ""
#report +=

for filename in glob.iglob('src/**/*.py', recursive=True):
    #print("Module: "+filename.replace('\\','.').replace('src.',''))
    report += "Module: "+filename.replace('\\','.').replace('src.','') + "\n "
    with open(filename.replace('\\','/')) as f:
        data = f.read()
        lines = data.split("\n")
        for line in lines:
            if(line.find('class ')!=-1) and line[-1]==':':
                #print("\n "+line)
                report += "\n "+ line + "\n "
            
                #print("   Parent:"+(line.split('(')[-1]).strip('):'))
                report += "   Parent:"+(line.split('(')[-1]).strip('):')
            if(line.find('def ')!=-1):
                #print("\t method: "+line)
                report += "\t method: "+line + "\n "
            if(line.find('return ')!=-1):
                #print("\t\t "+line)
                report += "\t\t "+line + "\n "
    #print("\n")
    report += "\n"

    print(report)
