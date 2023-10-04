import streamlit as st
import openai

openai.api_key=st.secrets["openai_key"]
st.title("Generative AI")

#input text box

prompt=st.text_area("Enter a Prompt:")
def generate_text(prompt):
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1200
    )
    return response.choices[0].text
    #button to generate text

 
    if st.button("Generate"):
        if prompt:
            generate_text=generate_text(prompt)
            st.write("Generated Text")
            st.write(generate_text)
        else:
            st.warning("please enter a prompt")
    