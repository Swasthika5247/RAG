from model import model
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser   

loader = PyPDFLoader("books/Attention.pdf")
docs = loader.load()
#doc = next(docs)
if __name__ == "__main__":
    print(type(docs))
    print(docs[0].page_content)
    print(docs[0].metadata)
    print(len(docs))
    prompt = PromptTemplate.from_template(
        template="you are a helpful assistant. Answer the following question: {question} \n\n context: {context}"
    )

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({
    "question": "What is the main topic of the text?",
    "context": docs[0].page_content
})
print(response)

