# ref: https://cookbook.openai.com/
from openai import OpenAI
import pandas as pd
# if using openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key="")

df = pd.read_csv("df_diet_practice_pubmed_summaries.txt.csv")
def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# Create embeddings for search and in context learning
df['ada_embedding'] = df.abstract.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
df.to_csv('embedded_diet_practice.csv', index=False)
