import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from Main import load_data

# Load data
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

# Convert streams column to numeric and drop rows with NaN values in streams
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
df = df.dropna(subset=['streams'])

# Get the top 10 tracks based on stream counts
top_tracks = df.nlargest(10, 'streams')

# Create a DataFrame for chart data, excluding 0 from rankings
chart_data = pd.DataFrame({
    'Track Name': top_tracks['track name'],
    'Spotify': top_tracks['in spotify charts'].replace(0, pd.NA),
    'Apple': top_tracks['in apple charts'].replace(0, pd.NA),
    'Deezer': top_tracks['in deezer charts'].replace(0, pd.NA),
    'Shazam': top_tracks['in shazam charts'].replace(0, pd.NA)
})

# Set 'Track Name' as the index
chart_data.set_index('Track Name', inplace=True)

# Create the plot
fig = go.Figure()

# Loop through each track and add its data as a trace in the plot
for track in chart_data.index:
    fig.add_trace(go.Scatter(
        x=chart_data.columns,
        y=chart_data.loc[track],
        mode='lines+markers',
        name=track,
        hoverinfo='x+y',
    ))

# Reverse y-axis to show higher rankings at the top
fig.update_layout(
    title="Ranking Across Platforms",
    xaxis_title="Platform",
    yaxis_title="Ranking",
    yaxis=dict(autorange='reversed'),
)

# Display the chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)
