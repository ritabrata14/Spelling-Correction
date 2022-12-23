# Spelling-Correction
Pick out all the misspelled words and give the most probable correct word and list of other probable correct words


Spellchecker
===============================================================================

It uses a `Levenshtein Distance <https://en.wikipedia.org/wiki/Levenshtein_distance>`__
algorithm to find permutations within an edit distance of 2 from the
original word. It then compares all permutations (insertions, deletions,
replacements, and transpositions) to known words in a word frequency
list. Those words that are found more often in the frequency list are
**more likely** the correct results.

``Spellchecker`` supports English Language Only. It uses the Levenshtein Distance (up to two) to be set for checking.

``Spellchecker`` supports **Python 3**


Installation
-------------------------------------------------------------------------------

The easiest method to install is using pip:

.. code:: bash

    pip install pyspellchecker

To build from source:

.. code:: bash

    1. git clone (https://github.com/ritabrata14/Spelling-Correction.git)
    
    2. cd spellchecker
    
    3. pip install pyspellchecker

    4. pip install pyspellchecker==0.5.6

    5. python main_model.py

Dataset
-------------------------------------------------------------------------------
A few dataset are already provided in the directory ./Dataset.
We have tested our model using those datasets.
You can also used other dataset given in the https://www.kaggle.com/code/bittlingmayer/spell-py/data

Running the code
-------------------------------------------------------------------------------

For any dataset path not specificed in the code, the code uses the default dataset which is already set.

On running main_model.py, the code will run and produce output of probable correct words and list of probable correct words.
