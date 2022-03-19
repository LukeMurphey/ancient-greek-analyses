import io
from zipfile import ZipFile
from analyses_tester import GreekAnalysesTester

ZIPPED_FILENAME = 'greek-analyses.txt.zip'
FILENAME = 'greek-analyses.txt'

with ZipFile(ZIPPED_FILENAME) as archive:
    with archive.open(FILENAME, 'r') as analyses_file:
        words = io.TextIOWrapper(analyses_file, newline=None)
        greek_tester = GreekAnalysesTester()
        greek_tester.parse_file(words)
        greek_tester.print_results()
