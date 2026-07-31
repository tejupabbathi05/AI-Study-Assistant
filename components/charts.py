import plotly.express as px
import pandas as pd


def quiz_score_chart(attempts):

    if not attempts:
        return None

    data = []

    for i, attempt in enumerate(reversed(attempts), start=1):

        data.append(
            {
                "Attempt": i,
                "Score": attempt.percentage
            }
        )

    df = pd.DataFrame(data)

    fig = px.line(
        df,
        x="Attempt",
        y="Score",
        markers=True,
        title="Quiz Performance"
    )

    fig.update_layout(
        xaxis_title="Quiz Attempt",
        yaxis_title="Percentage",
        height=400
    )

    return fig