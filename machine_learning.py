import os

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import pandas as pd


[print('\n') for i in range(10)]




data = {
    'texts': [],
    'target_names': [],
    'targets': [i for i in range(5)],
}


files = os.listdir('school-subject-prediction/articles/')
for file in files:
    data['target_names'].append(file[:-4])

    with open(f'school-subject-prediction/articles/{file}', 'r') as f:
        data['texts'].append(f.read().lower())




word_vector = CountVectorizer()
word_vector_counts = word_vector.fit_transform(data['texts'])

term_freq_transformer = TfidfTransformer()
term_freq = term_freq_transformer.fit_transform(word_vector_counts)

model = MultinomialNB().fit(term_freq, data['targets'])



fake_texts = [
    'biology'
]

fake_texts = [text.lower() for text in fake_texts]

fake_counts = word_vector.transform(fake_texts)
fake_term_freq = term_freq_transformer.transform(fake_counts)

predictions = model.predict(fake_term_freq)

for prediction in predictions:
    print(data['target_names'][prediction])




probabilities = model.predict_proba(fake_term_freq)



# proba_df = pd.DataFrame(probabilities, columns=data['target_names'])
# pred_df = pd.DataFrame([data['target_names'][prediction] for prediction in predictions])
# pred_df['text'] = fake_texts

# print('Probabilities\n',proba_df,'\n\n')
# print('Predictions\n',pred_df)
