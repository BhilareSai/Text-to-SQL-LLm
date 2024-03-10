from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
 
    model=genai.GenerativeModel(model_name="gemini-pro")
    response=model.generate_content([prompt[0],question])
    if len(response.parts) != 1 or "text" not in response.parts:
     print(response.parts[0].text)   
     return response.parts[0].text
    

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION  ,MARKS \nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    i Just Want SQL Query

    """]




## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    query=get_gemini_response(question,prompt)

    response=read_sql_query(query,"student.db")
    st.subheader("The Response is for ",query )
    for row in response:
        print(row)
        st.header(row)    
        
   