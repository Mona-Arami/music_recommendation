import streamlit as st
st.set_page_config(page_title="Music Mastermind", layout="wide")

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import streamlit.components.v1 as components

@st.cache_data
def load_data():
    df = pd.read_csv("data/filtered_track_df.csv")
    df['genres'] = df.genres.apply(lambda x: [i[1:-1] for i in str(x)[1:-1].split(", ")])
    exploded_track_df = df.explode("genres")
    return exploded_track_df

genre_names = ['Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']
audio_feats = ["acousticness", "danceability", "energy", "instrumentalness", "valence", "tempo"]

exploded_track_df = load_data()

def n_neighbors_uri_audio(genre, start_year, end_year, test_feat):
    genre = genre.lower()
    genre_data = exploded_track_df[(exploded_track_df["genres"]==genre) & (exploded_track_df["release_year"]>=start_year) & (exploded_track_df["release_year"]<=end_year)]
    genre_data = genre_data.sort_values(by='popularity', ascending=False)[:500]

    neigh = NearestNeighbors()
    neigh.fit(genre_data[audio_feats].to_numpy())

    n_neighbors = neigh.kneighbors([test_feat], n_neighbors=len(genre_data), return_distance=False)[0]

    uris = genre_data.iloc[n_neighbors]["uri"].tolist()
    audios = genre_data.iloc[n_neighbors][audio_feats].to_numpy()
    return uris, audios
    



def web_page():
    # set layout
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: #273b62;
            color:#ffffff;
            font-size:50px;
            gap: 0rem;

        }}
        .st-ci{{
        color:#736bae;
        }}
        .css-81oif8{{
        color:#736bae;
        min-height: 0rem;
        }}
        .css-ue6h4q {{
        color:#736bae;
        }}
        .css-1n543e5 {{
        color:#736bae; !important
        }}
        .css-1n543e5 {{
        color:#736bae; !important
        }}
        .st-cg{{
        color:#ffffff;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    def title(title):
        st.markdown(f'<h1 style="color:#ffffff" >{title}</h1>', unsafe_allow_html=True)
    def header(header):
        st.markdown(f'<h2 style="color:#736bae">{header}</h2>', unsafe_allow_html=True)
    def ppp(p_text):
        st.markdown(f'<p style="color:#736bae">{p_text}</p>', unsafe_allow_html=True)
    def new_line():
        st.markdown(f'</br>', unsafe_allow_html=True)
    
    title('Music Mastermind')
    header('Find music to listen to')
    new_line()
    # st.write("Welcome aboard! This is the platform where you can customize your listening experience using a machine learning model.")
    # st.write("Explore various genres and fine-tune audio features to discover music recommendations curated just for you!")
        
    with st.container():
        col1, col2, col3 = st.columns((1.5,0.5,5))
        with col1:
            "***Choose genre:***"
            genre = st.selectbox(
                "",
                genre_names, index=genre_names.index("Pop"))
            # with col2:
            "***Choose features:***"
            start_year, end_year = st.slider(
                'Select the year range',
                1990, 2019, (2015, 2019)
            )
            acousticness = st.slider(
                'Acousticness',
                0.0, 1.0, 0.5)
            danceability = st.slider(
                'Danceability',
                0.0, 1.0, 0.5)
            energy = st.slider(
                'Energy',
                0.0, 1.0, 0.5)
            instrumentalness = st.slider(
                'Instrumentalness',
                0.0, 1.0, 0.0)
            valence = st.slider(
                'Valence',
                0.0, 1.0, 0.45)
            tempo = st.slider(
                'Tempo',
                0.0, 244.0, 118.0)
        with col3:
            tracks_per_page = 6
            test_feat = [acousticness, danceability, energy, instrumentalness, valence, tempo]
            uris, audios = n_neighbors_uri_audio(genre, start_year, end_year, test_feat)

            tracks = []
            for uri in uris:
                track = """<iframe src="https://open.spotify.com/embed/track/{}" width="350" height="200" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(uri)
                tracks.append(track)

            if 'previous_inputs' not in st.session_state:
                st.session_state['previous_inputs'] = [genre, start_year, end_year] + test_feat
            
            current_inputs = [genre, start_year, end_year] + test_feat
            if current_inputs != st.session_state['previous_inputs']:
                if 'start_track_i' in st.session_state:
                    st.session_state['start_track_i'] = 0
                st.session_state['previous_inputs'] = current_inputs

            if 'start_track_i' not in st.session_state:
                st.session_state['start_track_i'] = 0
            
            with st.container():
                col1, col2, col3 = st.columns([3,0.5,3])
                if st.button("Recommend More Songs"):
                    if st.session_state['start_track_i'] < len(tracks):
                        st.session_state['start_track_i'] += tracks_per_page

                current_tracks = tracks[st.session_state['start_track_i']: st.session_state['start_track_i'] + tracks_per_page]
                current_audios = audios[st.session_state['start_track_i']: st.session_state['start_track_i'] + tracks_per_page]
                if st.session_state['start_track_i'] < len(tracks):
                    for i, (track, audio) in enumerate(zip(current_tracks, current_audios)):
                        if i%2==0:
                            with col1:
                                components.html(
                                    track,
                                    height=200,
                                )
                                # with st.expander("See more details"):
                                #     df = pd.DataFrame(dict(
                                #     r=audio[:5],
                                #     theta=audio_feats[:5]))
                                #     fig = px.line_polar(df, r='r', theta='theta', line_close=True)
                                #     fig.update_layout(height=400, width=340)
                                #     st.plotly_chart(fig)
                    
                        else:
                            with col3:
                                components.html(
                                    track,
                                    height=200,
                                )
                                # with st.expander("See more details"):
                                #     df = pd.DataFrame(dict(
                                #         r=audio[:5],
                                #         theta=audio_feats[:5]))
                                #     fig = px.line_polar(df, r='r', theta='theta', line_close=True)
                                #     fig.update_layout(height=400, width=340)
                                #     st.plotly_chart(fig)

                else:
                    st.write("No songs left to recommend")
web_page()
