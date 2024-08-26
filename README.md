# READABILITY RATER

### Rating the reading difficulty of a text based on three readability metrics.

This programme enables the user to measure and classify an input text according to its readability via three readability metrics: _SMOG Index_, _Gunning Fog Index_, and _Flesch-Kincaid Grade Level Score_. This was the final project for a course I took at university.


### 1. Introduction

Although readability measures are merely based "on surface characteristics of text" (Collins-Thompson 2014: 101), they can, nevertheless, provide a basic insight into the difficulty of a text. Consequently, these measures continue to play a crucial role in certain fields and applications (Bailin and Grafstein 2016: 1, 34) such as in
linguistics (c.f. Kayam 2018, Lim 2008) or health care (Ley and Florio 1996). This program, the _Readability Rater_, will implement a total of three commonly used readability formulas (c.f. Zamanian and Heydari 2012: 44-46; Ley and Florio 1996: 9-11):

* __SMOG Index__ (cf. McLaughlin 1969)**: Grade Level = 3+√(number of polysyllabic words per 30 sentences)

* __Gunning Fog Index__ (cf. Gunning 1973)**: Grade Level = 0.4×((number of words/number of sentences)+100×(number of polysyllabic words/number of words))

* __Flesch-Kincaid Grade Level Score__ (cf. Kincaid et al. 1975): Grade Level = (0.39×(number of words/number of sentences))+(11.8×(number of syllables/number of words))-15.594

_Note_: All metrics interpret polysyllabic words as words with three or more syllables. However, the _Gunning Fog Index_ excludes polysyllabic words which are only polysyllabic due to common inflectional affixes (e.g. "-ing", "-ed", or "es"), proper nouns, and hyphenated words (cf. "The Gunning's Fog Index (or FOG) Readability Formula").

The resulting values of these three tests are indicative of the grade level (U.S. grade level) required to understand the text. In other words, a grade level score of 6.2 indicates that the text is understandable to an average 6th grade student in the American school system.


### 2. Usage

With this program, the user will be able to select any of these tests and additional functions via the following flags including their abbreviations in parentheses.

* SMOG Index: ```--smog```			Abbreviation: ```-sm```
* Gunning Fog Index: ```--gunningfog```		Abbreviation: ```-gf```
* Flesch-Kincaid Score: ```--fleschkincaid```	Abbreviation: ```-fk```

The flag ```--stats``` will  provide the user with a few basic readability measures such as the type/token ratio, average
sentence and word lengths, the average number of syllables per word, and the percentage of monosyllabic and polysyllabic
words within the text file. The flag --all will display the results of all three readability metrics per file.

* Readability Statistics: ```--stats```		Abbreviation: ```-st```
* All Readability Scores: ```--all```		Abbreviation: ```-a```

A sample input prompt for one of the readability metrics applied to the sample text files in "data" would be:

```>>> python main.py data --gunningfog```
	
The output for each file on the terminal would be:

```
-------------------------------------------------
File: Frances_Burney_simple.txt
Gunning Fog: 6.88
-------------------------------------------------
```

The same applies to the other two flags, i.e. ```--smog``` and ```--fleschkincaid```. Also, the input prompt for the ```--all```
and ```--stats``` flags is analogous to the sample input provided above. In terms of output, however, the ```--all``` flag applied
to the files in "data" would render the following output for each file:

```
-------------------------------------------------
File: Frances_Burney_simple.txt
SMOG: 10.14
Gunning Fog: 6.88
Flesch-Kincaid: 6.81
-------------------------------------------------
```

Similarly, the ```--stats``` flag applied to the files in "data" would create this output for each file:

```
-------------------------------------------------
File: Frances_Burney_simple.txt
Type-Token Ratio: 0.38
Average word length: 4.59
Average sentence length: 10.86
Average number of syllables per word: 1.54
Percent of monosyllabic words: 60.05
Percent of polysyllabic words: 12.33
-------------------------------------------------
```

If no flag is given, the file name(s) will be printed. Further information can also be retrieved via the
```--help``` flag or its abbreviation ```-h```. Unlike existing Python packages, this programme utilizes _spaCy_ and the _syllables_
Python package (see below). It is, therefore, recommended to install these packages before using this programme.

Please consider the following when using this programme:

* Please ensure that your input consists of complete sentences (cf. Collins-Thompson 2014: 101).
* Likewise, your input can either consist of a single text or a folder of multiple texts. However, each input text needs to have a minimum length of 300 words for _Gunning Fog_ and _Flesch-Kincaid_ (Collins-Thompson 2014: 101) and a minimum length of 600 words for _SMOG_ (McLaughlin 1969: 641). Moreover, the _SMOG Index_ requires a sample of thirty sentences from the input text, i.e. 10 consecutive ones from the beginning, middle and end of the text (McLaughlin 1969: 639). Thus, please ensure that your input text consists of 30 sentences minimum for the _SMOG_ metric. You will receive an error message if your input is too short.
* This program can be used with any text file or folder of text files placed in the same directory as main.py.
* Should the folder contain other files, you will receive an error message and only the text files will be considered.
* One should not analyze too many or too large files at once due to processing reasons.
* In order to run certain tests in test_metrics.py, please make sure that test_file.txt is in the same directory.
* As several automatic algorithms are used, e.g. to count syllables (_syllables_ package) or filter out proper nouns (_spaCy_ tagger), one should be aware that the readability scores depend on the accuracy of these algorithms. There may be miscategorizations.


### 3. Data

This program was tested by creating a small data set containing the following texts based on the English and
Simple English Wikipedia entries on these female British authors:

* Frances_Burney_simple.txt
* Frances_Burney_en.txt
* Mary_Shelley_simple.txt
* Mary_Shelley_en.txt
* Jane_Austen_simple.txt
* Jane_Austen_en.txt

This sample data set shows, for example, that the Simple English files consistently render lower grade level scores than the Standard English files. Therefore, one could claim that the Simple English files in this data set are easier to comprehend than the Standard English ones.


### Data sources:
"Jane Austen". 2021. Wikipedia. Available at <https://en.wikipedia.org/wiki/Jane_Austen> (last accessed June 4, 2021).<br/>
"Jane Austen". 2021. Wikipedia. Available at <https://simple.wikipedia.org/wiki/Jane_Austen> (last accessed June 4, 2021).<br/>
"Frances Burney". 2021. Wikipedia. Available at <https://en.wikipedia.org/wiki/Frances_Burney> (last accessed June 4, 2021).<br/>
"Frances Burney". 2021. Wikipedia. Available at <https://simple.wikipedia.org/wiki/Frances_Burney> (last accessed June 4, 2021).<br/>
"Mary Shelley". 2021. Wikipedia. Available at <https://en.wikipedia.org/wiki/Mary_Shelley> (last accessed June 4, 2021).<br/>
"Mary Shelley". 2021. Wikipedia. Available at <https://simple.wikipedia.org/wiki/Mary_Shelley> (last accessed June 4, 2021).<br/>

### References:

Bailin, A., and Grafstein, A. 2016. Readability: Text and Context. Basingstoke: Palgrave Macmillain.<br/>
Collins-Thompson, K. 2014. "Computational assessment of text readability. A survey of current and future research". International Journal of Applied Linguistics 165: 97–135.<br/>
Gunning, R. 1973. The art of clear writing (revised edition). New York: McGraw Hill.<br/>
Kayam, O. 2018. "The Readability and Simplicity of Donald Trump’s Language". Political Studies Review 16: 73–88.<br/>
Kincaid, J.P., Fishburne, R.P., Rogers, R.L., & Chissom, B.S. 1975. "Derivation of new readability formulas for Navy enlisted personnel." (Millington, Tennessee, Navy Research Branch).<br/>
Ley, P. and Florio, T. 1996. "The use of readability formulas in health care". Psychology, Health & Medicine 1: 7–28.<br/>
Lim, E. T. 2008. The Anti-Intellectual Presidency: The Decline of Presidential Rhetoric from George Washington to George W. Bush. Oxford: Oxford University Press.<br/>
McLaughlin, G. H. 1969. "SMOG Grading – a new readability formula". Journal of Reading 12: 639–646.<br/>
Zamanian, M. and Heydari, P. 2012. "Readability of Texts: State of the Art". Theory and Practice in Language Studies 2: 43-53.<br/>
"The Gunning’s Fog Index (or FOG) Readability Formula". 2021. Readability Formulas. Available at <https://www.readabilityformulas.com/gunning-fog-readability-formula.php> (accessed June 1, 2021).<br/>
For more details on the Python package “readability”, please see: <https://pypi.org/project/readability/> (last accessed on March 2, 2021).<br/>
For more details on the Python package “syllables”, please see:<https://pypi.org/project/syllables/> (last accessed on March 2, 2021).<br/>
For more details on the Python library "spaCy", please see:<https://spacy.io/> (last accessed on March 3, 2021).
