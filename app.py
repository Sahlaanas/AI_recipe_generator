
import os
import streamlit as st
from langchain_community.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import json
from langchain_google_genai import GoogleGenerativeAI
from PIL import Image
image = Image.open("C:/Users/user/Downloads/img.png")
load_dotenv()
API_KEY = os.getenv("API_KEY")

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=API_KEY)





class Recipe(BaseModel):
    cooking_time: str = Field(description="Estimated cooking time")
    ingredients: str = Field(description="List of ingredients")
    instructions: str = Field(description="Step-by-step instructions")
    
    


prompt = PromptTemplate(
    template="Tell me the recipe for {dish_name}.\n"
             "Please include the following details:\n"
             "- Estimated cooking time\n"
             "- List of ingredients\n"
             "- Step-by-step instructions\n",
    input_variables=["dish_name"],
)



chain = prompt | llm 




st.image(image)
st.title("Recipe Generator")
user_input = st.text_input("Search your dish")
submit = st.button("Generate")



if submit:
    output = chain.invoke({"dish_name": user_input})
    st.write(output)
    
