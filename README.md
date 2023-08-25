# Article AI Backend

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/dewinterjack/article-api&env=REPLICATE_API_KEY&project-name=article-api&repo-name=article-api)

This Flask API will create a summary for an article and will eventually support
more AI interactions.

## How it works

This project uses public and custom LLM models from
[Replicate](https://replicate.com/) to generate a summary. You can feed the
Flask API endpoint an article url as a query param and it will return a short
summary.

## Running Locally

After cloning the repo, go to [Replicate](https://replicate.com/) to make an
account and put your API key in `.env`.

Then, run the following in the command line and your application will be
available at `http://localhost:3000`

```bash
npm i -g vercel
vercel dev
```

To use the API route, go to the link below in your browser or run a curl command
in your terminal to get a sample result. Feel free to replace the dub.sh link
with a link to any image.

```bash
curl http://localhost:3000/generate?articleUrl=https://vercel.com/blog/gpt-3-app-next-js-vercel-edge-functions
```
