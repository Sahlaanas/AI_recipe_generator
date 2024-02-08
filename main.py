API_KEY = "AIzaSyDN8S3Q8N_6hyK4pXMG9Cn-8wsRpI9SlP8"
import google.generativeai as genai
import streamlit as st
import json

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-pro')



def get_gimini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text



input_prompt = """
Act like a skilled and professional chef who knows every cuisine and dishes.
I will give you the sambar , generate the recipe of that sambar along with 
time for cooking, ingredients for sambar and steps of cooking that.

I want the response having the structure
{{"Time":"","Ingredients":[],"Steps":[]}}

"""

dish_name = "sambar"
response = get_gimini_response(input_prompt)
print(type(response))
response = response.replace('{{','')
response = response.replace('}}','')

response_dict ={}
for item in response.split(','):
    if ":" in item:
        key, value = item.split(":", 1)
        print(value)
        # ... process key and value
    
    
print(response_dict.keys())


# st.title("Recipe Generator")
# dish_name = st.text_input("Search your dish")

# submit = st.button("Submit")


# if submit:
#     response = get_gimini_response(input_prompt)
#     recipe_dict = {}
#     for item in response.split(";"):
#         key, value = item.split(":", 1)
#         if key in ["Ingredients", "Steps"]:
#             value = value.split(",")  # Split into a list for these keys
#         recipe_dict[key] = value
        
#     print(recipe_dict.keys(),"=============")
    
    

        
