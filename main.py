import os
import json

from decouple import config

from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0,
)

schema = {
    'properties': {
        'posicao': {'type': 'integer'},
        'time': {'type': 'string'},
        'jogos': {'type': 'integer'},
        'vitorias': {'type': 'integer'},
        'empates': {'type': 'integer'},
        'derrotas': {'type': 'integer'},
        'gols_pro': {'type': 'integer'},
        'gols_contra': {'type': 'integer'},
        'saldo_gols': {'type': 'integer'},
        'pontos': {'type': 'integer'},
    }
}

def extract(content, schema):
    return create_extraction_chain(
        schema=schema,
        llm=llm,
    ).invoke(content).get('text')

def scrap_with_playwright(urls, schema):
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformed = BeautifulSoupTransformer()
    docs_transformed = bs_transformed.transform_documents(
        documents=docs,
        tags_to_extract=['table'], #Extrair tags HTML (h1, h2, h3, span, a, table, etc...)
    )
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=2000,
        chunk_overlap=0,
    )
    splits = splitter.split_documents(
        documents=docs_transformed,
    )
    extracted_content = []

    for split in splits:
        extracted_content.extend(
            extract(
                schema=schema,
                content=split.page_content,
            )
        )
    return extracted_content

if __name__ == '__main__':
    urls = ['https://ge.globo.com/futebol/brasileirao-serie-a/']
    extracted_content = scrap_with_playwright(
        urls=urls,
        schema=schema,
    )

    with open('dados.json', 'w') as fp:
        json.dump(
            obj=extracted_content,
            fp=fp,
            ensure_ascii=False,
            indent=4,
        )
