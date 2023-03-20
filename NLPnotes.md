- NLP techniques
    - Rules and heuristics (no comlex ML/DL ... simple rule based regex)
    - Statistics and ML
    - Deep learning

- NLP tasks
    - Text Classfication (eg. Classify complaints as high/medium/low, sentiment analysis, document classification, hate speech classification etc. using labelled data)
    - Text similarity (eg. is resume matching job description)
    - Information extraction (like getting key details from flight ticket or credit card)
    - Information retrieval
    - Chatbots (type of chatbots: FAQ bots: simple QnA, Flow based bots: remebers previous replies in same convo, Open ended bot: like Siri, alexa)
    - Machine Translation (google translate: RNN Decoder-Encoder)
    - Text summarization
    - Topic Modelleing (Rtrieve abstract topics from lots and lots of documents, which we can't go through manually)

- Real life problem
    1. Step 1: Data Acquisition: Can be from org data source, public dataset or web scraping
    2. Step 2: Text Extraction & Cleanup
        - before doing anything else, we need to prepare the data
        - for that we should remove any text field which clearly will not affect the result
        - Then we can also combine some of the fields: like title and description if we are classifyin something becuase it can in the end be decided from words of either title or description
        - Then Spell correction and removal of extra new lines can also be done
    3. Preprocessing
        - Sentence segmentation sentence tokenization
            - in a simple scenario it will be simply to split text on '.', '?', '!' etc.
            - but some case can be complicated like dot after etc. or any abbreviation (Dr.) is not the end of a sentence.
            - so NLTK and spacy order some high level sentence tokenizers
        - Word tokenization
            - Stemming and Lemmatization: to convert each word to base word (eg. ate -> eat, loving -> love)
    4. Feature enginnering
        - incudes converting text to vectors and more connected words should have closer numeric value
    5. Model Building and evaluation (ML/DL)