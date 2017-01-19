l# Language-Lead-Bot
Python code for automating language lead tasks (localization/translation/corpus analysis)

The Language Lead Bot's goal is to replicate some of the tasks that language leads must do for localization projects, in an automated way. The code will output a report for all or selected features listed below.

This first version is simply an MVP, a proof of concept. It works with an English source, for now, UTF8. Powered by NLTK and TextBlob mainly.

FEATURES
Features included in version 1.0 are:

Counts:
  - wordcount
  - sentence count
  - paragraph count
  - character count
  - token count
  - unique words count
  - average sentence length
  - longest sentence

Frequencies:
- most frequent words
- less frequent words
- show frequent nouns (+ count)
- show frquent adj. (+count)

Glossaries and Dictionaries:
- glossary matching
- less frequent words defined

Spelling:
- hapaxes are spellchecked
- list of ignore terms
- stopwords

Lexical information:
- frequent collocations
- lexical richness

HOW TO USE:

- In the .py file, update the paths to your files: corpus, ignore list, glossary, as required.
- Running the code will generate a report with all available features.
- Some features are simple can be run directly from the relevant print() line

Individual funtions:
- fdistlen(): report number of words by length in your corpus
- findhapaxes(): prints the 50 less frequent words in your corpus
- hapaxdef(): prints hapaxes (words that appear only 1 time in your corpus) followed by their definition
- spell(): spellchecks hapaxes - if confidence is not 100%, presents all spelling suggestions
- __longestsent__(): prints out longest sentence in your corpus
- __averagesentlen__(): reports average sentence length
- findNN(): print out frequent nouns
- findJJ(): print out frequent adjectives
- glossarymatch(): find words from your corpus included in a glossary (CSV, source,target)

