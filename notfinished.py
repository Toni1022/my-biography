import streamlit as st

#----Page Configuration----
st.set_page_config(page_title="BIOGRAPHY")

#----HEADER SECTION----
st.title("Toni's Biography") #large font size

#----Image for Profile Picture----
# two-column layout and place the image in the top-right column
col1, col2 = st.columns([4, 2])  # Adjust the ratio to make the right column narrow
with col2:
    st.image("IMG_20241022_115232.jpg", width=320) 

#----Personal Information----
st.subheader("Personal Information") #medium font size 

gettoknowme= st.text_area("Get to know Me", """Hey, I'm Toni Faye S. Hibaya. A first year computer engineering student and this
is my biography. Hope you will learn something new about me.""")

#Name Input
Name= st.text_input("Name","Toni Faye S. Hibaya")
#Birthday Input
Birthday= st.text_input("Birthday", "October 22,2006")
#Age Input
age= st.text_input("Age", "18")
#Gender Input
gender= st.radio("Gender", "Female")

#----Likes and Dislikes----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Likes and Dislikes") 
        st.write("##")
        st.write(
            """ 
            Likes:
            - Reading manhwa's, manhua's, and manga's.
            - Listening to rnb, krnb/khiphop, kpop, and ppop.
            - Playing basketball.
            
            Dislikes:
            - Durian
            - Messy people.
            - Getting sick.
            """
         
        )

#----Family----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Family")
        st.write("##")
        st.write(
            """
            Mother's Name: Filma S. Hibaya
           
            Birthday: June 25, 1968

            Father's Name: Tony J. Hibaya
            
            Birthday: December 17, 1976
            
            Sister's Name: Phoebe Anne Tonette S. Hibaya

            Birthday: September 22,2009
            """
        )    


#Educational Attainment
st.subheader("Educational Attainment")
#Elementary
elem= st.text_input("Elementary", "Emerico Borja Elementary School")
#Junior High
junior= st.text_input("Junior High", "Cabrera Altres National High School")
#Senior High
senior= st.text_input("Senior", "Surigao Del Norte National High School")
#College
college= st.text_input("College", "Surigao Del Norte State University")