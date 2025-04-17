import pickle
import streamlit as st
import numpy as np
import sklearn

st.header("Book Recommender System using Machine Learning")
st.subheader("Find Your Favourite Book")
model=pickle.load(open("artifacts/model.pkl","rb"))
book_names=pickle.load(open("artifacts/book_names.pkl","rb"))
books_pivot=pickle.load(open("artifacts/book_pivot.pkl","rb"))
final_rating=pickle.load(open("artifacts/final_rating.pkl","rb"))

selected_books=st.selectbox(
    "Type or select a book ",book_names
)
def fetch_poster(suggestions):
    poster_url=[]
    books_name=[]
    ids_index=[]
    
    for book_id in suggestions:
        books_name.append(books_pivot.index[book_id])
    for name in books_name[0]:
        ids=np.where(final_rating["title"]==name)[0][0]
        ids_index.append(ids)
        
    for i in ids_index:
        poster_url.append(final_rating.iloc[i]["image_url"])
        
    return poster_url
    
   

def recommend_books(book_name):
    book_list=[]
    book_id=np.where(books_pivot.index==book_name)[0][0]
    distances,suggestions=model.kneighbors(books_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    
    poster_url=fetch_poster(suggestions)
    
    for i in range(len(suggestions)):
        books=books_pivot.index[suggestions[i]]
        for j in books:
            book_list.append(j)
    return book_list,poster_url

if st.button("Show Books"):
    recommend_books,poster_url=recommend_books(selected_books)  
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(recommend_books[0])
        st.image(poster_url[0])
        
    with col2:
        st.text(recommend_books[1])
        st.image(poster_url[1])
        
    with col3:
        st.text(recommend_books[2])
        st.image(poster_url[2])
        
    with col4:
        st.text(recommend_books[3])
        st.image(poster_url[3])
        
    with col5:
        st.text(recommend_books[4])
        st.image(poster_url[4])
    
    with col6:
        st.text(recommend_books[5])
        st.image(poster_url[5])
        