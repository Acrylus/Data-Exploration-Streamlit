import streamlit as st
import pandas as pd

# Load the dataset
from Main import load_data
df = load_data()

# Set page title
st.title('JolliBini: Dataset Introduction')

# Display the full dataset
st.write("### Full Dataset:")
st.dataframe(df, height=500)

# Dictionary with column names and their descriptions
column_descriptions = {
    "track name": "Name of the song.",
    "artist(s) name": "Name of the artist(s) of the song.",
    "artist count": "Number of artists contributing to the song.",
    "released year": "Year when the song was released.",
    "released month": "Month when the song was released.",
    "released day": "Day of the month when the song was released.",
    "in spotify playlists": "Number of Spotify playlists the song is included in.",
    "in spotify charts": "Presence and rank of the song on Spotify charts.",
    "streams": "Total number of streams on Spotify.",
    "in apple playlists": "Number of Apple Music playlists the song is included in.",
    "in apple charts": "Presence and rank of the song on Apple Music charts.",
    "in deezer playlists": "Number of Deezer playlists the song is included in.",
    "in deezer charts": "Presence and rank of the song on Deezer charts.",
    "in shazam charts": "Presence and rank of the song on Shazam charts.",
    "bpm": "Beats per minute, a measure of song tempo.",
    "key": "Key of the song.",
    "mode": "Mode of the song (major or minor).",
    "danceability %": "Percentage indicating how suitable the song is for dancing.",
    "valence %": "Positivity of the song's musical content.",
    "energy %": "Perceived energy level of the song.",
    "acousticness %": "Amount of acoustic sound in the song.",
    "instrumentalness %": "Amount of instrumental content in the song.",
    "liveness %": "Presence of live performance elements.",
    "speechiness %": "Amount of spoken words in the song."
}

# Create a mapping of display names (without _) to original column names
column_display_names = {col.replace('_', ' ').title(): col for col in column_descriptions.keys()}

# Dropdown to select a column (with _ replaced by spaces)
st.write("### Select a Column to View its Description:")
selected_display_column = st.selectbox("Select a column:", list(column_display_names.keys()))

# Get the original column name based on the selected display name
selected_column = column_display_names[selected_display_column]

# Display the description of the selected column
if selected_column:
    st.write(f"**{selected_display_column}:** {column_descriptions[selected_column]}")

# Display the data types of the columns
st.write("### Data Types of the Columns:")
st.write(df.dtypes)


