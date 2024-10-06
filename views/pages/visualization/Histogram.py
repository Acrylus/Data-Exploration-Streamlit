import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from Main import load_data

df = load_data()

st.title("Histogram")
st.subheader("Top 10 streamed music - Percentages")

st.write(
    """
    This bar chart displays various audio attributes of the top 10 streamed music tracks, 
    including Danceability, Valence, Energy, Acousticness, Instrumentalness, Liveness, 
    and Speechiness. Each attribute is represented as a separate bar for each track, 
    allowing for easy comparison of these musical characteristics.
    """
)


df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df.dropna(subset=['streams'])

top_tracks = df.nlargest(10, 'streams')

attributes = ['Danceability %', 'Valence %', 'Energy %', 'Acousticness %', 'Instrumentalness %', 'Liveness %', 'Speechiness %']

fig = go.Figure()

for attribute in attributes:
    fig.add_trace(go.Bar(
        x=top_tracks[attribute.lower()],
        y=top_tracks['track name'],
        name=attribute,
        orientation='h',
        text=[f'{p:.1f}%' for p in top_tracks[attribute.lower()]],
        textposition='auto',
    ))

fig.update_layout(
    title="Top 10 Tracks' Attributes",
    xaxis_title="Percentage",
    yaxis_title="Track Name",
    barmode='group',
    xaxis=dict(tickformat='.1f'),
    yaxis={'categoryorder': 'total ascending'},
)

st.subheader("Top 10 Tracks' Attributes (Grouped by Track Name)")
st.plotly_chart(fig, use_container_width=True)