import csv
import string

def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# get 25,000 restaurants, for each restaurant, there are a couple of reviews
numofRes = 25000
businessSet = {}
with open('yelp_academic_dataset_review.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		businessId = row[4]
		label = row[6]
		review = row[2]
		if isEnglish(review) == False:
			continue
		for c in ("\n", "\t"):
			review=review.replace(c, " ")
			review=review.replace(c, " ")
		if len(businessSet) < numofRes:
			if businessId not in businessSet:
				businessSet[businessId] = [(review, label)]
			else:
				businessSet[businessId].append((review, label))
		else:
			if businessId in businessSet:
				businessSet[businessId].append((review, label))

# print businessSet
# summarize the vocab list and star
vocab_set = set()
stars = {}
for i in range(numofRes):
	values = businessSet.values()[i]
	for value in values:
		text = value[0]
		star = value[1]
		if i not in stars:
			stars[i]=[star]
		else:
			stars[i].append(star)
		# make all vocab to lowercase
		text = text.lower()
		# remove punctuation
		for c in string.punctuation:
			text = text.replace(c,"")
		split_text = text.split(" ")
		for vocab in split_text:
			
			if vocab not in vocab_set:
				vocab_set.add(vocab)

thefile = open('new_vocab.txt','w')
for item in sorted(vocab_set):
	thefile.write("%s\n" % item)
			


