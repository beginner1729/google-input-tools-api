## Google Input Tools

[Google Input Tools](https://www.google.com/inputtools/) is a [transliteration](https://en.wikipedia.org/wiki/Transliteration) service from google. Apart from being usable from various Google products we can make http get request to it.
The implementation here accomplish just that in python(>=3.6). This repo here just adds asyncio flavour to the original implementation [here](https://www.kaggle.com/salonikalra/transliterate-using-http-google-input-tools). So that we may run in batches as its faster.

### How to Install

> pip install -r requirement.txt

### Command to Run

>python run_batchwise.py --input eng_to_bengali.txt --output in_bengali.csv --batch_size 100 --itc bn

__Input Args__

- *intput* : path to newline seperated input sentences in romanized version
- *output* : path to output file. which is a csv file with 2 colums romanWord,nativeWord
- *batch_size* : number of sentences to consider at a time
- *itc* : this is the code which specifies what language are we referring here. More codes can be found [here](https://cloud.google.com/translate/docs/languages)


