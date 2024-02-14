from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter

def analyze_code(code):
    pylint_output = StringIO()  # Custom open stream
    reporter = TextReporter(pylint_output)
    Run([f'media/{code}', "--disable=import-error,invalid-name"], reporter=reporter, exit=False)
    print(f'media/{code}')
    return pylint_output.getvalue().replace("\n", "<br>").replace((f'media\{code}').replace('/', '\\'), '')
