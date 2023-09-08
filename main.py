
import streamlit as st

# modules imports
from utils import DECADES, GENRES
from utils import (
    load_image,
    estimate_decade_and_genres, 
    estimate_title_and_actors, 
    generate_image
)

# functions
def estimate_button_clicked():
    st.session_state.do_estimate = True
    
def generate_button_clicked():
    st.session_state.do_generate = True
    
# session state
if 'do_estimate' not in st.session_state:
    st.session_state.do_estimate = False
    
if 'do_generate' not in st.session_state:
    st.session_state.do_generate = False

if 'generation_ready' not in st.session_state:
    st.session_state.generation_ready = False
    
# 0. Header
st.set_page_config('Filmy', layout='wide')

st.markdown("<h2 style='text-align: center; color: white;'>RePost</h2>",
            unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white;'>start by uploading your prefered poster</p>",
            unsafe_allow_html=True)
st.subheader("", divider='rainbow')

uploaded_file = st.file_uploader("", type=["jpg", "png"])
image_path = uploaded_file.name if uploaded_file is not None else None

if image_path is not None:
    # work
    image = load_image(image_path)
    
    # show
    

    info_columns = st.columns(2)
    with info_columns[0]:
        st.subheader("Extracted poster data", divider='rainbow')
        
        st.button("Estimate", on_click=estimate_button_clicked)
        if st.session_state.do_estimate:
            with st.spinner("estimating relevant text"):
                title, actors = estimate_title_and_actors(image_path)
                st.markdown(f"""
                - Title: **{title}**
                - Actors: **{", ".join(actors)}**
                """)
            with st.spinner("estimating style"):
                decade, genre = estimate_decade_and_genres(image_path)
                st.markdown(f"""
                    - Decade: **{decade}**
                    - Genre: **{genre}**
                """)
            st.session_state.generation_ready = True
            
    with info_columns[1]:
        
        if st.session_state.do_estimate and st.session_state.generation_ready:
            
            st.subheader("Generate your own", divider='rainbow')
            with st.form('generate_form'):
                style_columns = st.columns(2)
                with style_columns[0]:
                    if (key := 'decade_selection') not in st.session_state:
                        st.session_state[key] = f"{decade}s"
                    selected_decade = st.selectbox("Decade", DECADES, key='decade_selection')
                with style_columns[1]:
                    if (key := 'genre_selection') not in st.session_state:
                        st.session_state[key] = genre
                    selected_genre = st.selectbox("Genre", GENRES, key='genre_selection')
                
                if (key := 'prompt_selection') not in st.session_state:
                    st.session_state[key] = ''
                selected_genre = st.text_input("Prompt", key='prompt_selection')
                
                st.form_submit_button("Generate", on_click=generate_button_clicked)
        
    images_columns = st.columns(2)   
    with images_columns[0]:
        # show image perhaps with some text
        st.image(image, width=None, caption="Uploaded Movie Poster")
        
    with images_columns[1]:
        if st.session_state.do_generate:
            with st.spinner("generating your poster"):
                new_poster = generate_image(image_path)
            
                st.image(new_poster, width=None, caption=f"{decade}s {title}")


st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")

st.markdown("<h3 style='text-align: center; color: white;'>gallery</h3>",
            unsafe_allow_html=True)
st.subheader("", divider='rainbow')

footer_columns = st.columns(3)
with footer_columns[0]:
    st.image("tt12986254.jpg")
with footer_columns[1]:
    st.image("tt14074150.jpg")
with footer_columns[2]:
    st.image("tt14308636.jpg")
