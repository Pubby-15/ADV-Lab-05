import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Global Development Dashboard",
    page_icon="🌍",
    layout="wide",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load Plotly's bundled Gapminder sample dataset."""
    return px.data.gapminder()


def filter_data(
    data: pd.DataFrame, selected_year: int, selected_continents: list[str]
) -> pd.DataFrame:
    """Return records matching the chosen year and continents."""
    return data.loc[
        (data["year"] == selected_year)
        & (data["continent"].isin(selected_continents))
    ].copy()


df = load_data()

st.title("🌍 Global Development Dashboard")
st.write(
    "Explore the relationship between income, population, and life expectancy "
    "across countries using the Gapminder sample dataset."
)

st.sidebar.header("Dashboard Filters")
years = sorted(int(year) for year in df["year"].unique())
selected_year = st.sidebar.select_slider(
    "Select year",
    options=years,
    value=years[-1],
)
continents = sorted(str(value) for value in df["continent"].unique())
selected_continents = st.sidebar.multiselect(
    "Select continent(s)",
    options=continents,
    default=continents,
)

filtered = filter_data(df, selected_year, selected_continents)

st.subheader(f"Key indicators — {selected_year}")
if filtered.empty:
    st.warning("No records match the selected filters. Select at least one continent.")
else:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Countries", f"{filtered['country'].nunique():,}")
    col2.metric("Median life expectancy", f"{filtered['lifeExp'].median():.1f} years")
    col3.metric("Total population", f"{filtered['pop'].sum() / 1_000_000_000:.2f} B")
    col4.metric("Median GDP per capita", f"${filtered['gdpPercap'].median():,.0f}")

    st.subheader("GDP per capita vs. life expectancy")
    scatter = px.scatter(
        filtered,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=48,
        labels={
            "gdpPercap": "GDP per capita (US dollars)",
            "lifeExp": "Life expectancy (years)",
            "pop": "Population",
            "continent": "Continent",
        },
        title=f"Country comparison in {selected_year}",
    )
    scatter.update_layout(height=560, legend_title_text="Continent")
    st.plotly_chart(scatter, use_container_width=True)

    st.subheader("Average life expectancy by continent")
    life_summary = (
        filtered.groupby("continent", as_index=False)["lifeExp"]
        .mean()
        .sort_values("lifeExp", ascending=False)
    )
    bar = px.bar(
        life_summary,
        x="continent",
        y="lifeExp",
        color="continent",
        labels={"continent": "Continent", "lifeExp": "Average life expectancy (years)"},
        title="Average life expectancy",
    )
    bar.update_layout(showlegend=False, height=400)
    st.plotly_chart(bar, use_container_width=True)

    with st.expander("View filtered country records"):
        st.dataframe(
            filtered[["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]]
            .sort_values("gdpPercap", ascending=False),
            use_container_width=True,
            hide_index=True,
        )

st.caption(
    "Lab 4 — Git Basics for a Python Project | Data source: Plotly Gapminder sample data"
)
