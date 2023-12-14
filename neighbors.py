# ref: https://learn.microsoft.com/en-us/azure/ai-services/openai/tutorials/embeddings?tabs=python-new%2Ccommand-line&pivots=programming-language-python
import pandas as pd
import numpy as np
from openai import OpenAI
import numpy as np
from ast import literal_eval

# if using openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key="")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding
# search through the medical fact for a given medical query
def search_medical_fact(df, medical_query, n=3, pprint=True):
    print("Query: ", {medical_query})
    df["ada_embedding"] = df.ada_embedding.apply(literal_eval).apply(np.array)
    product_embedding = get_embedding(
        medical_query,
        model="text-embedding-ada-002"
    )
    df["similarity"] = df.ada_embedding.apply(lambda x: cosine_similarity(x, product_embedding))
    df.sort_values("similarity", ascending=False)
    return df

# Find the closest match with the medical query
def find_closest_match(df, medical_query, n=1):
    import re
    results = search_medical_fact(df, medical_query, n=n)
    context =  " ".join(results['abstract'].values.tolist())
    cleaned_text = re.sub(r'<[^>]+>', '', context)
    return cleaned_text


"""
df = pd.read_csv("embedded_general_medical.csv")
print(find_closest_match(df, medical_query="I have cough but I think I have fever too. What should I do?", n=1))
"""

