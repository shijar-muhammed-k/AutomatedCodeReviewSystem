import re
import google.generativeai as genai
genai.configure(api_key='AIzaSyBm9nGWehu0TEDIdoYAJcThGXNP7nkLDLk')
import Utilities.autopep8 as autopep8

import Utilities.pep8 as pep8

def analyze_code(code):
    
    path = rf'media\{code}'
    check = pep8.Checker(filename = path)
    res = check.check_all()
    if(len(res) > 0):
        linter = ""
        for item in res:
            item = item.replace(path+':', '')
            linter += item + "<br>"
            
        linter = linter[:-4]

    else:
        linter = False

    with open (f'media/{code}', 'r') as c:
        l = c.read()
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Give me a vulnarability report of this code\n" + l)

    result = response.text.replace("\n", "<br>") if response.parts else False

    if result != False:
        pattern = re.compile(r'\*\*(.*?)\*\*')
        result = result.replace('**', '<b>', 1)
        result = re.sub(pattern, r'<b>\1</b>', result)
    else:
        result = 'Sorry we found error while fetching the vulnerability, please try again'
        
    return {'linter': linter, 'vulnerability': result}

def fix_code(code):
    path = "media/"+code
    print(path)
    with open(path, 'r') as code_to_fix:
        code_contents = code_to_fix.read()

    fix = autopep8.fix_code(code_contents, options={'aggressive': True, 'max_line_length': 64, 'diff':True, 'in_place': True})
    
    with open(path, 'w') as fixed_file:
        fixed_file.write(fix)
