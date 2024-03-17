import subprocess
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
# from google.colab import userdata

# GOOGLE_API_KEY=userdata.get('AIzaSyCPH0cf7oSdP28TFhTqgxobAnOmr3QrV1A')

genai.configure(api_key='AIzaSyCPH0cf7oSdP28TFhTqgxobAnOmr3QrV1A')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def analyze_code(code):
            
    pylint_output = StringIO()  # Custom open stream
    reporter = TextReporter(pylint_output)
    Run([f'media/{code}', "--disable=import-error,invalid-name"], reporter=reporter, exit=False)
    result = pylint_output.getvalue().replace("\n", "<br>").replace((f'media\{code}').replace('/', '\\'), '').replace('*', '')
    lines = result.split('<br>')
    lines.pop(0)
    result_text = '<br>'.join(lines)
    print(result_text)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Give me some linter report for this code" + codeto)
    with open('result_text.py', 'w') as f:
        f.write(response.text.replace('```python', '').replace('```', ''))
    return result_text

def fix_code(code):
    check = subprocess.check_output(f"python -m black --diff --verbose media/{code}")
    path = "media/"+code
    fix = subprocess.run(["python", "-m", "black", "--verbose", path], capture_output=True)
    # return fix.decode().replace('\r\n', '<br>')
    print(fix, 'dadda')
    return fix.stderr
