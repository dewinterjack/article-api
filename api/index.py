import os
import replicate
from flask import Flask, request
from newspaper import Article

app = Flask(__name__)
os.environ.get("REPLICATE_API_TOKEN")

@app.route("/")
def index():
    return "LLM functions for articles"

@app.route('/generate')
def home():
  args = request.args
  articleUrl = args.to_dict().get('articleUrl')

  article = Article(articleUrl)
  article.download()
  article.parse()

  model = replicate.models.get("replicate/llama-2-70b-chat")
  llm = model.versions.get("58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781")

  system_prompt="""
You are a web article summary writer.
Summaries are concise and only cover the essentials.
Take the 3 most important points from the article and write 3 single sentance bullet points.

This is an example of the structure of a summary:

• AI tools like DALL-E and Midjourney are increasingly being used in creative production and have started winning awards for their output.
• AI's potential to generate new, creative content is impacting industries such as Hollywood, as seen in the writers strike.
• A recent study found that AI, like GPT-4, scored in the top percent for originality in creativity tests, challenging the notion that creativity is exclusive to humans.
"""

  return llm.predict(system_prompt=system_prompt, prompt=article.text)
