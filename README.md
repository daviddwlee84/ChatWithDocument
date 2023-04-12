# Chat With Documents

Apply LLM and ANN (Embedding Recall) to chat with document or do summarization.

## Main Dependencies

* LangChain: Drive LLMs
* annoy: relevance embedding recall (alternative of Pinecone)

## Resources

* Tutorial
  * [LangChain101: Question A 300 Page Book (w/ OpenAI + Pinecone) - YouTube](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
    * [langchain-tutorials/Ask A Book Questions.ipynb at main · gkamradt/langchain-tutorials · GitHub](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)
  * [GPT-4 & LangChain Tutorial: How to Chat With A 56-Page PDF Document (w/Pinecone) - YouTube](https://www.youtube.com/watch?v=ih9PBGVVOO4)
    * [mayooear/gpt4-pdf-chatbot-langchain: GPT4 & LangChain Chatbot for large PDF docs](https://github.com/mayooear/gpt4-pdf-chatbot-langchain)
* OpenAI
  * [OpenAI API](https://openai.com/blog/openai-api)
    * [API Reference - OpenAI API](https://platform.openai.com/docs/api-reference)
* LLM
  * [hwchase17/langchain: ⚡ Building applications with LLMs through composability ⚡](https://github.com/hwchase17/langchain)
* ANN / Embedding Recall
  * [spotify/annoy: Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/saving to disk](https://github.com/spotify/annoy)
  * [SearchEngine/search/annoy at master · daviddwlee84/SearchEngine · GitHub](https://github.com/daviddwlee84/SearchEngine/tree/master/search/annoy)
* PDF Parser (we will use LangChain's PDF Loader)
  * [jstockwin/py-pdf-parser: A Python tool to help extracting information from structured PDFs.](https://github.com/jstockwin/py-pdf-parser)
    * [Overview — PDF Parser documentation](https://py-pdf-parser.readthedocs.io/en/latest/overview.html)
* .env
  * [theskumar/python-dotenv: Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.](https://github.com/theskumar/python-dotenv)
* Other
  * [openai/tiktoken: tiktoken is a fast BPE tokeniser for use with OpenAI's models.](https://github.com/openai/tiktoken) (for OpenAIEmbeddings)

## Trouble Shooting

### Install annoy

```txt
building 'annoy.annoylib' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

* [Microsoft C++ Build Tools - Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

```txt
Installing collected packages: annoy
  DEPRECATION: annoy is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
```

`pip install annoy --use-pep517 --force`
