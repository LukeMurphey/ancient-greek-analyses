from greek_analyses_parser import GreekAnalysesParser
import re

class GreekAnalysesTester(GreekAnalysesParser):

    def __init__(self):
        self.results = {
            "missing_meaning": 0,
            "has_strange_meaning": 0,
        }

    def is_missing_meaning(self, form, lemma_form, meaning, details, attrs, definition):
        return meaning.strip() == ""

    def has_strange_meaning(self, form, lemma_form, meaning, details, attrs, definition):
        return re.search('\[|\]', meaning) != None

    def process_word_description(self, form, lemma_form, meaning, details, attrs, definition):

        # Detect missing definitions
        if self.is_missing_meaning(form, lemma_form, meaning, details, attrs, definition):
            self.results["missing_meaning"] += 1

        # Detect strange meanings
        if self.has_strange_meaning(form, lemma_form, meaning, details, attrs, definition):
            self.results["has_strange_meaning"] += 1

        return None

    def print_results(self):
        print("Missing meanings: " + str(self.results["missing_meaning"]))
        print("Has strange meanings: " + str(self.results["has_strange_meaning"]))
