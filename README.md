# Chat With Documents

Apply LLM and ANN (Embedding Recall) to chat with document or do summarization.

## Main Dependencies

* LangChain: Drive LLMs
* annoy: relevance embedding recall (alternative of Pinecone)

## Getting Started

1. `pip install -r requirements.txt`
2. Solve dependency issues of the PDF parser (see [Trouble Shooting](#trouble-shooting))
3. `cd chat_with_doc` then `python llm_chain.py` (temporarily, will have interactive CLI or WebUI)

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
