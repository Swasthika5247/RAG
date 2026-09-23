from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from model import model
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()



document_loader = TextLoader("books/AI.txt ", encoding="utf8")
#docs=document_loader.load()
docs=document_loader.lazy_load()
doc=next(docs)
#print(type(docs))
#print(docs[0].page_content)
#print(docs[0].metadata)

prompt = PromptTemplate.from_template(
    #input_variables=["question", "context"],   (use when using just prompt template without from_template)
    template="You are a helpful assistant. Answer the following question: {question} \n\n context: {context}"
)

chain = prompt | model | parser

response = chain.invoke({
    "question": "What is the main topic of the text?",
    "context": doc.page_content
})

print(response)