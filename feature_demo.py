"""Small feature-branch example for the Git Basics lab."""


def make_feature_summary(year: int, continents: list[str]) -> str:
    """Build a short label for a selected dashboard view."""
    region_text = ", ".join(continents) if continents else "no continents selected"
    return f"Feature preview for {year}: {region_text}"


if __name__ == "__main__":
    print(make_feature_summary(2007, ["Asia", "Europe"]))
