import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from Main import load_data

df = load_data()

st.title("Line")
st.subheader("Top 10 streamed music - Ranking of each platform")

st.write(
    """
    This chart displays the positions of the top 10 streamed music tracks across various platforms, 
    including Spotify, Apple Music, Deezer, and Shazam. Each line represents a track, and the markers 
    indicate its respective position on each platform's chart. A lower position number signifies a 
    higher ranking on the charts.
    """
)

df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df.dropna(subset=['streams'])

top_tracks = df.nlargest(10, 'streams')

chart_data = pd.DataFrame({
    'Track Name': top_tracks['track name'],
    'Spotify': top_tracks['in spotify charts'].dropna().values,
    'Apple': top_tracks['in apple charts'].dropna().values,
    'Deezer': top_tracks['in deezer charts'].dropna().values,
    'Shazam': top_tracks['in shazam charts'].dropna().values
})

chart_data.set_index('Track Name', inplace=True)

fig = go.Figure()

for track in chart_data.index:
    fig.add_trace(go.Scatter(
        x=chart_data.columns,
        y=chart_data.loc[track],
        mode='lines+markers',
        name=track,
        hoverinfo='x+y',
    ))

fig.update_layout(
    title="Ranking Across Platforms",
    xaxis_title="Platform",
    yaxis_title="Ranking",
    yaxis=dict(autorange='reversed'),
)

st.plotly_chart(fig, use_container_width=True)
