import json
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("-j", "--json", help="Minified and Escaped json")
#args = parser.parse_args()

#data = json.loads(args.json)
f = open("CurrentJSON.json", 'r')
data = json.loads(f.read())
f.close()

preambleTEX = """\documentclass[addpoints]{{exam}}"""

documentTEX = """\begin{{document}}
\makebox[\textwidth]{{Name and section:\enspace\hrulefill}}
\vspace{{0.2in}}
\makebox[\textwidth]{{Instructor’s name:\enspace\hrulefill}}
\begin{{questions}}
{MQuestions}
{OQuestion}
\end{{questions}}
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


TITLE = data['title']

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
		currQ = MQuestionTEX.format(Question=question, choices=ch)
		mult_questions.append(currQ)
	elif item['type'] == 'open':
		length = item['customNumberOfLines']
		currQ = OQuestionTEX.format(Question=question, Length=length)
		open_questions.append(currQ)
	else:
		pass

mq = "\n".join(mult_question)
oq = "\n".join(open_question)
finalTEX = preambleTEX + documentTEX.format(MQuestions=mq, OQuestions=oq)

tex_file = open("")
