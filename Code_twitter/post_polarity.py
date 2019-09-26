from get_positive_words import get_positive_words
from get_negative_words import get_negative_words

positive_words = get_positive_words()
negative_words = get_negative_words()

def post_polarity(post):
	pos = 0
	neg = 0

	for word in post:
		if word in positive_words:
			pos = pos + 1
		elif word in negative_words:
			neg = neg + 1

	if ( pos > neg):
		return 1
	elif (pos < neg):
		return -1
	else:
		return 0