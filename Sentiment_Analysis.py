import streamlit as st
from textblob import TextBlob
import os

def main():
    st.title("Setimental Analysis WebApp")
    st.write("Buildwith Streamlit and Python")
    activities = ["Sentiment_Analysis"]
    # choice = st.sidebar.selectbox("Select activities", activities)

    # choice == "Sentiment_Analysis":
    from_sent=st.text_input("Enter a sentence: ")
    if st.button("Analysis"):
        br=TextBlob(from_sent)
        result=br.sentiment.polarity
        if result==0:
            st.success("This is a Neutral Message")
        elif result>0:
            st.success("This is a Positive Message")
        else:
            st.success("This is a Negative Message")

if __name__=="__main__":
    main()