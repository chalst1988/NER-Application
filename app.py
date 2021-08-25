from flask import Flask,url_for,render_template,request
import spacy
from spacy import displacy
#nlp = spacy.load("en")
#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("C:/Users/csury001/Downloads/custom_ner")
import json

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
	# raw_text = "Because of the bullshit I had to endure, I doubt I'll purchase another set of Michelin tires. The tires are great until they begin to have issues. That's when it all goes downhill. Maybe Goodyear, Yokohama, Dunlop, Bridgestone, Continental, Cooper, Hankook, Nokian, Toyo, and others are the same way, but I'll take my chances. Josee at Michelin was great to deal with."
	# docx = nlp(raw_text)
	# html = displacy.render(docx,style="ent")
	# html = html.replace("\n\n","\n")
	# result = HTML_WRAPPER.format(html)

	return render_template('index.html')


@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		docx = nlp(raw_text)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('result.html',rawtext=raw_text,result=result)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext

	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)