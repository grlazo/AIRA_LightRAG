## AIRA LightRAG (AIRA_LightRAG)

The AIRA LightRAG (AIRA_LightRAG) simply supports the data processed for the
AIRA example shown previously.

To use the LightRAG method for AIRA it is recommended to start from the sources and set-up environment accordingly.

The source files are located at:
https://github.com/HKUDS/LightRAG

To get started you would:
git clone https://github.com/HKUDS/LightRAG

```
cd LightRAG
pip install -e .
```

Specific instructions are provided for working with Ollama models.

We have provided example files for that shown previously in case you wish to test this method yourself.

The basic file structure is as follows:
```
./AIRA_LightRAG/examples/lightrag_ollama_PDF01.py
./AIRA_LightRAG/examples/lightrag_ollama_PDF02.py
./AIRA_LightRAG/examples/lightrag_ollama_PDF19.py
./AIRA_LightRAG/examples/lightrag_ollama_PDF20.py
./AIRA_LightRAG/examples/graph_PDF01_with_html.py
./AIRA_LightRAG/examples/graph_PDF02_with_html.py
./AIRA_LightRAG/examples/graph_PDF19_with_html.py
./AIRA_LightRAG/examples/graph_PDF20_with_html.py
./AIRA_LightRAG/PDF01
./AIRA_LightRAG/PDF02
./AIRA_LightRAG/PDF19
./AIRA_LightRAG/PDF20
./AIRA_LightRAG/README.md_
./AIRA_LightRAG/requirements.txt
```

The final out visualization uses networkx to view; simply select the resulting html file.
