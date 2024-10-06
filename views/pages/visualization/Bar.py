import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from Main import load_data

df = load_data()

st.title("Bar")
st.subheader("Top 10 streamed music - bpm")

st.write(
    """
    This visualization displays the top 10 streamed music tracks based on their stream counts. 
    Each bar represents the BPM (beats per minute) of a track, allowing you to understanding the 
    energy and pace of music that influence listener engagement and preference.
    """
)

df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df.dropna(subset=['streams'])

top_tracks = df.nlargest(10, 'streams')

fig = go.Figure()

for i in range(len(top_tracks)):
    fig.add_trace(go.Bar(
        x=[top_tracks['track name'].iloc[i]],
        y=[top_tracks['bpm'].iloc[i]],
        name=top_tracks['track name'].iloc[i],
        text=[f'{top_tracks["bpm"].iloc[i]:.1f}'],
        textposition='auto'
    ))

fig.update_layout(
    title="BPM of Top 10 Streamed tracks",
    xaxis_title="Track Name",
    yaxis_title="BPM",
    yaxis=dict(tickformat='.1f'),
    xaxis={'categoryorder': 'total ascending'},
)

st.plotly_chart(fig, use_container_width=True)
