import streamlit as st
import pandas as pd
import plotly.express as px
from Main import load_data

df = load_data()

st.title("Scatter")
st.subheader("Top 10 streamed music - Playlist")

st.write(
    """
    This scatter plot visualizes the top 10 streamed music tracks based on their appearances 
    in playlists across different platforms, including Spotify, Apple Music, and Deezer. 
    """
)

df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df.dropna(subset=['streams'])

top_tracks = df.nlargest(10, 'streams')

scatter_data = top_tracks.melt(id_vars=['track name'], 
                                value_vars=['in spotify playlists', 'in apple playlists', 'in deezer playlists'],
                                var_name='Playlist', 
                                value_name='Streams')

fig = px.scatter(scatter_data, 
                 x='track name',
                 y='Streams',
                 color='Playlist',
                 title='Number of Streams per Playlist Platform',
                 labels={'track name': 'Track Name', 'Streams': 'Streams'},
                 hover_data=['Playlist', 'Streams'])


fig.update_traces(marker=dict(size=10))

fig.update_layout(yaxis_title='Number of Playlist',
                  xaxis_title='Track Name',
                  legend_title='Playlist')

st.plotly_chart(fig, use_container_width=True)
