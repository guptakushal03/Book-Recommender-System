import streamlit as st
import pickle
import pandas as pd

with open('book_dict.pkl', 'rb') as file:
    book_dict = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

books = pd.DataFrame(book_dict)

def recommend(selected_book_name):
    book_index = books[books['Name'] == selected_book_name].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_books = []
    for i in books_list:
        recommended_books.append(books.iloc[i[0]].Name)
    return recommended_books

st.title('Books Recommender System')
st.write('Note! This is just a prototype and works on limited datasets.')
selected_book_name = st.selectbox(
    'Type Name of the Book',
    books['Name'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_book_name)
    for i in recommendations:
        st.write(i)