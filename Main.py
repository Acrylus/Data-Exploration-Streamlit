import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Load the dataset
    df = pd.read_csv('views/dataset/spotify-2023.csv', encoding='ISO-8859-1')

    df = df.drop_duplicates()

    df.columns = df.columns.str.replace('_', ' ')

    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df['in deezer playlists'] = pd.to_numeric(df['in deezer playlists'], errors='coerce')
    df['in shazam charts'] = pd.to_numeric(df['in shazam charts'], errors='coerce')


    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    df[numeric_cols ] = df[numeric_cols].fillna(0)

    df[numeric_cols] = df[numeric_cols].astype(int)

    df['key'] = df['key'].astype('category')
    df['mode'] = df['mode'].astype('category')

    return df

df = load_data()

pages = {
    "About Dataset": [
        st.Page("views/pages/Introduction.py", title="Introduction", icon=":material/person:"),
        st.Page("views/pages/Conclusion.py", title="Conclusion", icon=":material/dataset:"),
        st.Page("views/pages/Statistics.py", title="Statistics", icon=":material/legend_toggle:"),
    ],
    "Visualization": [
        st.Page("views/pages/visualization/Area.py", title="Area", icon=":material/ssid_chart:"),
        st.Page("views/pages/visualization/Histogram.py", title="Histogram", icon=":material/analytics:"),
        st.Page("views/pages/visualization/Bar.py", title="Bar", icon=":material/bar_chart:"),
        #st.Page("views/pages/visualization/Table.py", title="Table", icon=":material/table_chart:"),
        st.Page("views/pages/visualization/Scatter.py", title="Scatter", icon=":material/scatter_plot:"),
    ],
}

st.logo(
    "views/icons/Spotify.png",
    icon_image="views/icons/Spotify.png",
)

pg = st.navigation(pages)
pg.run()