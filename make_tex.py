import json
import subprocess
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-j", "--json", help="Minified and Escaped json")
#args = parser.parse_args()

#data = json.loads(args.json)
f = open("CurrentJSON.json", 'r')
data = json.loads(f.read())
f.close()

preambleTEX = r"""\documentclass[addpoints]{exam}"""

documentTEX = r"""\begin{{document}}
\makebox[\textwidth]{{Name and section:\enspace\hrulefill}}
\vspace{{0.2in}}
\makebox[\textwidth]{{Instructor’s name:\enspace\hrulefill}}
\begin{{questions}}
{MQuestions}
{OQuestions}
\end{{questions}}
\end{{document}}
"""

MQuestionTEX = r"""\question
{Question}
\begin{{choices}}
{Choices}
\end{{choices}}
"""

ChoiceTEX = r"""\choice {choice}"""

OQuestionTEX = r"""\question
{Question}
\fillwithlines{{{Length}}}
"""


TITLE = data['title']
VERSION = data['version']

mult_questions = []
open_questions = []

for item in data['questions']:
	question = item['question']
	if item['type'] == 'multi':
		choices = []
		for choice in item['answers']:
			c = ChoiceTEX.format(choice=choice)
			choices.append(c)
		ch = "\n".join(choices)
		currQ = MQuestionTEX.format(Question=question, Choices=ch)
		mult_questions.append(currQ)
	elif item['type'] == 'open':
		length = item['customNumberOfInches']
		currQ = OQuestionTEX.format(Question=question, Length=length)
		open_questions.append(currQ)
	else:
		pass

mq = "\n".join(mult_questions)
oq = "\n".join(open_questions)
finalTEX = preambleTEX + documentTEX.format(MQuestions=mq, OQuestions=oq)

tex_file = open("CurrTEX.tex", "w")
tex_file.write(finalTEX)
tex_file.close()

subprocess.call("pdflatex CurrTEX.tex", shell=True)
