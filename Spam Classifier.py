import pandas as pd

messages = pd.read_csv(r"C:\Users\Lenovo\Desktop\NLP\SMSSpamCollection", sep="\t", names=["label","message"])
               
import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps =PorterStemmer()
corpus = []
for i in range(len(messages)):
    review = re.sub("[^a-zA-Z]", " ", messages["message"][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review =" ".join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 4000)
X = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(messages["label"])
y = y.iloc[:,1].values



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 49)

from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred = spam_detect_model.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score
acuuracy = accuracy_score(y_test, y_pred)


    
    