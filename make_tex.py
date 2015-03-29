import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--json", help="Minified and Escaped json")
args = parser.parse_args()

data = json.loads(args.json)

preambleTEX = """\documentclass[addpoints]{{exam}}"""

documentTEX = """\begin{{document}}
\makebox[\textwidth]{{Name and section:\enspace\hrulefill}}
\vspace{{0.2in}}
\makebox[\textwidth]{{Instructor’s name:\enspace\hrulefill}}
\begin{{questions}}
{MQuestions}
\end{{questions}}
{OQuestion}
\end{{document}}
"""

MQuestionTEX = """\question
{Question}
\begin{{choices}}
{Choices}
\end{{choices}}
"""

ChoiceTEX = """\choice {choice}"""

OQuestionTEX = """\question
{Question}
\fillwithlines{{{Length}}}
"""


