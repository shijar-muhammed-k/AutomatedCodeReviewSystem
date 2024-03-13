import subprocess
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter


def analyze_code(code):
    pylint_output = StringIO()  # Custom open stream
    reporter = TextReporter(pylint_output)
    Run([f'media/{code}', "--disable=import-error,invalid-name --verbose=True"], reporter=reporter, exit=False)
    print(pylint_output)
    print(f'media/{code}')
    return pylint_output.getvalue().replace("\n", "<br>").replace((f'media\{code}').replace('/', '\\'), '')

def fix_code(code):
    check = subprocess.check_output(f"python -m black --diff --verbose media/{code}")
    print(check.decode())
    path = "media/"+code
    print(path)
    fix = subprocess.run(["python", "-m", "black", "--verbose", path], capture_output=True)
    # return fix.decode().replace('\r\n', '<br>')
    print(fix)
    return fix.stderr