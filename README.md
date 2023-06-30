# Chat With Documents

Apply LLM and ANN (Embedding Recall) to chat with document or do summarization.

## Main Dependencies

* LangChain: Drive LLMs
* annoy: relevance embedding recall (alternative of Pinecone)
* Python version >= 3.8

## Getting Started

1. `pip install -r requirements.txt`
2. Solve dependency issues of the PDF parser (see [Trouble Shooting](#trouble-shooting))
3. Copy `.env.example` to `.env`, and paste your [OpenAI API key](https://platform.openai.com/account/api-keys)
4. `cd chat_with_doc` then `python llm_chain.py` (temporarily, will have interactive CLI or WebUI)

## TODO

* Prompt Engineering
  * [ ] Change Chinese prompt
    * [X] [Example 1](https://github.com/imClumsyPanda/langchain-ChatGLM/blob/dc0cdfba9065c49099508616b0ed177cb4c54062/chains/local_doc_qa.py#L89-L96)
  * [ ] Try other prompt (Chat friendly)
* Replace OpenAI API with open source alternatives
  * [ ] Embedding
    * [ ] shibing624/text2vec -> GanymedeNil/text2vec-large-chinese
  * [ ] LLM
    * [ ] THUDM/ChatGLM-6B
    * [ ] Jittor-based LLM
  * [ ] ANN
* Approach
  * [ ] Extract topic from document for relevance search instead of compare the document embedding itself
  * [ ] Chunk document into smaller pieces e.g. sections / paragraphs / sentences
* UI/UX
  * [ ] CLI
  * [ ] WebUI
* Application
  * [ ] Simple QA
  * [ ] Chat with Document (with Chat History)

## Resources

* [Document QA | 🦜️🔗 Langchain](https://python.langchain.com/docs/modules/chains/additional/question_answering)
* Tutorial
  * [LangChain101: Question A 300 Page Book (w/ OpenAI + Pinecone) - YouTube](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
    * [langchain-tutorials/Ask A Book Questions.ipynb at main · gkamradt/langchain-tutorials · GitHub](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)
  * [GPT-4 & LangChain Tutorial: How to Chat With A 56-Page PDF Document (w/Pinecone) - YouTube](https://www.youtube.com/watch?v=ih9PBGVVOO4)
    * [mayooear/gpt4-pdf-chatbot-langchain: GPT4 & LangChain Chatbot for large PDF docs](https://github.com/mayooear/gpt4-pdf-chatbot-langchain)
  * [Tutorial: ChatGPT Over Your Data](https://blog.langchain.dev/tutorial-chatgpt-over-your-data/)
    * [hwchase17/chat-your-data](https://github.com/hwchase17/chat-your-data)
* Example
  * [imClumsyPanda/langchain-ChatGLM: langchain-ChatGLM, local knowledge based ChatGLM with langchain ｜ 基于本地知识的 ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM)
  * [GanymedeNil/document.ai: 基于向量数据库与GPT3.5的通用本地知识库方案(A universal local knowledge base solution based on vector database and GPT3.5)](https://github.com/GanymedeNil/document.ai)
  * [arc53/DocsGPT: GPT-powered chat for documentation search & assistance.](https://github.com/arc53/DocsGPT)
* OpenAI
  * [OpenAI API](https://openai.com/blog/openai-api)
    * [API Reference - OpenAI API](https://platform.openai.com/docs/api-reference)
* LLM
  * [hwchase17/langchain: ⚡ Building applications with LLMs through composability ⚡](https://github.com/hwchase17/langchain)
  * [THUDM/ChatGLM-6B: ChatGLM-6B：开源双语对话语言模型 | An Open Bilingual Dialogue Language Model](https://github.com/THUDM/ChatGLM-6B)
  * [Jittor/JittorLLMs: 计图大模型推理库，具有高性能、配置要求低、中文支持好、可移植等特点](https://github.com/Jittor/JittorLLMs)
  * [nomic-ai/gpt4all: gpt4all: an ecosystem of open-source chatbots trained on a massive collections of clean assistant data including code, stories and dialogue](https://github.com/nomic-ai/gpt4all)
  * [lm-sys/FastChat: The release repo for "Vicuna: An Open Chatbot Impressing GPT-4"](https://github.com/lm-sys/FastChat)
  * [BlinkDL/ChatRWKV: ChatRWKV is like ChatGPT but powered by RWKV (100% RNN) language model, and open source.](https://github.com/BlinkDL/ChatRWKV)
  * [abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)
* Embedding
  * OpenAIEmbedding
  * [shibing624/text2vec: text2vec, text to vector. 文本向量表征工具，把文本转化为向量矩阵，实现了Word2Vec、RankBM25、Sentence-BERT、CoSENT等文本表征、文本相似度计算模型，开箱即用。](https://github.com/shibing624/text2vec)
    * [shibing624/text2vec-base-chinese · Hugging Face](https://huggingface.co/shibing624/text2vec-base-chinese)
    * [GanymedeNil/text2vec-large-chinese at main](https://huggingface.co/GanymedeNil/text2vec-large-chinese/tree/main)
* ANN / Embedding Recall
  * [spotify/annoy: Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/saving to disk](https://github.com/spotify/annoy)
  * [SearchEngine/search/annoy at master · daviddwlee84/SearchEngine · GitHub](https://github.com/daviddwlee84/SearchEngine/tree/master/search/annoy)
* PDF Parser (we will use LangChain's PDF Loader -> it's actually depends on `unstructured` -> depends on `detectron2`)
  * [jstockwin/py-pdf-parser: A Python tool to help extracting information from structured PDFs.](https://github.com/jstockwin/py-pdf-parser)
    * [Overview — PDF Parser documentation](https://py-pdf-parser.readthedocs.io/en/latest/overview.html)
* .env
  * [theskumar/python-dotenv: Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.](https://github.com/theskumar/python-dotenv)
* Other Dependencies
  * [openai/tiktoken: tiktoken is a fast BPE tokeniser for use with OpenAI's models.](https://github.com/openai/tiktoken) (for OpenAIEmbeddings)
  * [Unstructured-IO/unstructured: Open source libraries and APIs to build custom preprocessing pipelines for labeling, training, or production machine learning pipelines.](https://github.com/Unstructured-IO/unstructured)
  * [facebookresearch/detectron2: Detectron2 is a platform for object detection, segmentation and other visual recognition tasks.](https://github.com/facebookresearch/detectron2)
    * [Installation — detectron2 0.6 documentation](https://detectron2.readthedocs.io/en/latest/tutorials/install.html)
  * [cbrunet/python-poppler: Python binding to Poppler-cpp pdf library](https://github.com/cbrunet/python-poppler)
    * [python-poppler’s documentation! — python-poppler documentation](https://cbrunet.net/python-poppler/)
    * [oschwartz10612/poppler-windows: Prebuilt Poppler binaries packaged for windows with dependencies](https://github.com/oschwartz10612/poppler-windows/)
  * [tesseract-ocr/tesseract: Tesseract Open Source OCR Engine (main repository)](https://github.com/tesseract-ocr/tesseract)
    * [Introduction | tessdoc](https://tesseract-ocr.github.io/tessdoc/Installation.html)
    * [Home · UB-Mannheim/tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* Other
  * [python - How to state in requirements.txt a direct github source - Stack Overflow](https://stackoverflow.com/questions/16584552/how-to-state-in-requirements-txt-a-direct-github-source)

## Trouble Shooting

### Install titoken

ERROR: Could not find a version that satisfies the requirement tiktoken (from versions: none)
ERROR: No matching distribution found for tiktoken

- [No matching distribution found for tiktoken · Issue #346 · GaiZhenbiao/ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT/issues/346)
- [problem solve after upgrade python3.7 to 3.8](https://github.com/acheong08/ChatGPT/issues/573#issuecomment-1419511208)

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

`pip install wheel` (~~`pip install annoy --use-pep517 --force`~~)

### Install Poppler

> For `unstructured`

```txt
..\..\meson.build:10:14: ERROR: Dependency lookup for poppler-cpp with method 'pkgconfig' failed: Pkg-config binary for machine 1 not found. Giving up.
```

`pip install --use-pep517 python-poppler`

* [How to install poppler on Windows10 ? (step by step) · Issue #42 · oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows/issues/42)

```powershell
# Use Scoppy (Couldn't find manifest for 'poppler'.)
irm get.scoop.sh | iex
scoop install poppler

# Use Chocolatey (Success)
choco install poppler
```

### Install tesseract

> For `unstructured`

```txt
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
```

* [tesseract-ocr/tesseract: Tesseract Open Source OCR Engine (main repository)](https://github.com/tesseract-ocr/tesseract)
* [Home · UB-Mannheim/tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki)

### Install ImageMagick

> For `py-pdf-parser`

```txt
ImportError: MagickWand shared library not found.
You probably had not installed ImageMagick library.
Try to install:
  https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows
```

### Install

* [image conversion - Imagemagick Convert PDF to JPEG: FailedToExecuteCommand `"gswin32c.exe" / PDFDelegateFailed - Stack Overflow](https://stackoverflow.com/questions/32466112/imagemagick-convert-pdf-to-jpeg-failedtoexecutecommand-gswin32c-exe-pdfdel)
* [Python 安装wand模块出错 wand.exceptions.DelegateError: FailedToExecuteCommand `"gswin64c.exe" -q -dQUI... - 简书](https://www.jianshu.com/p/812c2b46a86b)
* [Ghostscript](https://www.ghostscript.com/)
  * [Ghostscript : Downloads](https://www.ghostscript.com/releases/gsdnld.html)

```txt
wand.exceptions.DelegateError: FailedToExecuteCommand `"gswin64c.exe" -q -dQUIET -dSAFER -dBATCH -dNOPAUSE -dNOPROMPT -dMaxBitmap=500000000 -dAlignToPixels=0 -dGridFitTT=2 "-sDEVICE=pngalpha" -dTextAlphaBits=4 -dGraphicsAlphaBits=4 "-r150x150" -dPrinted=false -dFirstPage=1 -dLastPage=1 "-sOutputFile=C:/Users/david/AppData/Local/Temp/magick-zVgYM_snJYZPInoMrczafnS4JiAElv8t%d" "-fC:/Users/david/AppData/Local/Temp/magick-oCsZGHiEz2SbEDvyqNyZKMmsVkGS58Jd" "-fC:/Users/david/AppData/Local/Temp/magick-p0vM2uWevQNLAPkZhFJM4JWfyqROX5Jh"' (The system cannot find the file specified.
) @ error/delegate.c/ExternalDelegateCommand/517
```

### Create virtual environment

```sh
conda create -n venv python=3.8
```

- [How to create a virtual Python shell using Python tools - ActiveState](https://www.activestate.com/resources/quick-reads/virtual-python-shell/)
- [venv — Creation of virtual environments — Python 3.11.4 documentation](https://docs.python.org/3/library/venv.html)
- [how to create a venv with a different python version - Stack Overflow](https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version)
- [How to install 'pyenv' Python version manager on Ubuntu 20.04](https://brain2life.hashnode.dev/how-to-install-pyenv-python-version-manager-on-ubuntu-2004)
- [如何在ubuntu中安裝pyenv並使用多種版本的python？. 為什麼需要多種版本的python? | by Jeffrey | Medium](https://medium.com/@b10932006/%E5%A6%82%E4%BD%95%E5%9C%A8ubuntu%E4%B8%AD%E5%AE%89%E8%A3%9Dpyenv%E4%B8%A6%E4%BD%BF%E7%94%A8%E5%A4%9A%E7%A8%AE%E7%89%88%E6%9C%AC%E7%9A%84python-6626c1fbc76e)
