import streamlit as st
name=st.text_input("Enter you name:")
fname=st.text_input("Enter you Father name:")
add=st.text_area("Enter your Address:")
classdata=st.selectbox("Enter your class: ",(1,2,3,4,5,6))

button=st.button("Done")



if button:
    st.markdown(f""" Name: {name}, Father Name: {fname} , Class: {classdata},Address: {add} 
                """)