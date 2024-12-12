import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('./jadarat_processed.csv')

st.title('Where Life leads You After Gradution?')

st.write("""
Stepping into the professional world as a fresh graduate can be intimidating. The uncertainty of the job market, especially in a dynamic economy like Saudi Arabia's, can leave many feeling lost and anxious. This analysis aims to provide valuable insights into the current job landscape, empowering you on your career journey.
""")

# Job Opportunities Section
st.header("Where Are The Jobs")
region_counts = data['region'].value_counts().reset_index()
fig = px.pie(
    region_counts.head(8),
    values='count',
    names='region',
    title="Proportion of Job Postings by Region in KSA",
    hole=0.4,  
    color_discrete_sequence=px.colors.sequential.dense
)

fig.update_traces(
    textinfo='percent+label',
    textposition='outside',
    #textfont_size=12,  
)



st.plotly_chart(fig, use_container_width=True)
st.write("Without a doubt, Riyadh holds the largest share of job postings, followed by Makkah and the Eastern Province, while other regions contribute a smaller proportion.")
st.write("Now that we have a sense of job opportunities across KSA, let's find out if there is any gender preference.")
st.header("Gender Diversity in the Job Market")
gender = data['gender'].value_counts()
fig = go.Figure(data=[go.Pie(
                       labels=['Both', 'Males', 'Females'], 
                       values=gender.values, 
                       hole=0.3,  #
                       marker=dict(colors=px.colors.sequential.dense)  # Apply the first 3 colors
                    )])


st.plotly_chart(fig, use_container_width=True)
st.write('The majority of job postings are open to both males and females, indicating a positive trend towards gender equality in the workplace.')

st.header("Salary Expectations for Fresh Graduates")
fresh_grads = data[data['exper'] == 0]
fig = px.histogram(x=fresh_grads['Salary'], color_discrete_sequence=px.colors.sequential.dense[2:], labels={'x':'Salary'})
st.plotly_chart(fig, use_container_width=True)

st.write('The salary range for fresh graduates in Saudi Arabia is predominantly around 4,000 SAR.')

st.header("Myth vs. Reality: Opportunities for Fresh Graduates")

with_experience = data[data['exper'] > 0]
job_counts = [len(fresh_grads), len(with_experience)]
categories = ['Fresh Graduates', 'With Experience']

# Plot bar chart
fig = go.Figure(
    data=[
        go.Bar(
            x=categories,
            y=job_counts,
            marker=dict(color=px.colors.sequential.dense[3:]),
            text=job_counts,  
            textposition='auto'
        )
    ]
)

fig.update_layout(
    title='Fresh Graduates vs. Experienced',
    xaxis_title='Candidate Category',
    yaxis_title='Number of Job Opportunities',
    template='plotly_white'
)
st.plotly_chart(fig, use_container_width=True)

st.write("A significant number of job postings are specifically tailored to fresh graduates, demonstrating that with the right skills and a proactive approach, you can secure a fulfilling caree.")

st.write('Take a step forward; it will get easier!')



