import streamlit as st 

st.title('Where Life leads You After Gradution?')

st.write("""
As a fresh graduate, feeling lost is part of the journey. Your mind is likely filled with questions like, 
"Is there even a chance for fresh graduates in the Saudi market?" I will answer this question based on real datasets, 
and hopefully, we can find some hope.
""")

# Job Opportunities Section
st.header("Job Opportunities in Saudi Arabia")
st.image("./Q1.JPG", caption="Job Opportunities in Saudi Arabia")

st.header("Is There a Gender Preference in the Saudi Market?")
st.image('./Q2.JPG')
st.write("In the Saudi job market, gender distribution job positions shows a balanced preference, with 39 % of opportunities available to both genders, 32 % specifically for males, and 27 % for female.")

st.header("Salary Range for Fresh Graduates")
st.image('./Q3.JPG')
st.write('The salary range for fresh graduates in Saudi Arabia is predominantly around 4,000 SAR.')

st.header("The Truth Behind Fresh graduates Opportunities")
st.image('./Q4.JPG')
st.write('The data suggests growing opportunities for fresh graduates')