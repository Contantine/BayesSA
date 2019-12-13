from analyzer import SentimentAnalyzer

model_path = 'model.pkl'
userdict_path = 'userdict.txt'
stopword_path = 'stop_words.txt'
# corpus_path = './data/review.csv'

analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
text = '因为听说是游记,我耐着性子看完,最后,还是失望了...'

pos = analyzer.analyze(text=text)
