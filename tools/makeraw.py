from cStringIO import StringIO
import sys,logging
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from sklearn.feature_extraction.text import CountVectorizer

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def makedict(text):
    count_vect=CountVectorizer()
    X_train_counts = count_vect.fit_transform([text.decode(encoding="utf8")])
    print X_train_counts.shape
    print count_vect.vocabulary_.get('linguistics')
    return count_vect


def display(bow):
    for key,value in bow.vocabulary_.items():
        print key,value


if __name__ == "__main__":

    filename=sys.argv[1]
    logging.info("Extracting text from {}".format(filename))
    if "test" in sys.argv:
        pages=[1]
    else:
        pages=None


    text=convert(filename,pages=pages)
    bow=makedict(text)
    display(bow)