import subprocess
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter
import google.generativeai as genai
genai.configure(api_key='AIzaSyCPH0cf7oSdP28TFhTqgxobAnOmr3QrV1A')

def analyze_code(code):
            
    pylint_output = StringIO()  # Custom open stream
    reporter = TextReporter(pylint_output)
    Run([f'media/{code}', "--disable=import-error,invalid-name", "--msg-template='{path}:{line}:{column}: {msg_id}: {msg} ({symbol})'"], reporter=reporter, exit=False)
    result = pylint_output.getvalue().replace("\n", "<br>").replace((f'media\{code}').replace('/', '\\'), '').replace('*', '')
    lines = result.split('<br>')
    lines.pop(0)
    result_text = '<br>'.join(lines)

    with open (f'media/{code}', 'r') as c:
        l = c.read()
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Give me a vulnarability report of this code for displaying in a html page using innerHTMl " + l)

    return {'linter': result_text, 'vulnerability': response.text.replace("\n", "<br>")}

def fix_code(code):
    check = subprocess.check_output(f"python -m black --diff --verbose media/{code}")
    path = "media/"+code
    fix = subprocess.run(["python", "-m", "black", "--verbose", path], capture_output=True)
    return fix.stderr
