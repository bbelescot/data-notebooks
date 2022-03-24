import pandas as pd


def jugement_majoritaire_computations(vote_input: dict) -> pd.DataFrame():

    vote_results_percent = pd.DataFrame(vote_input).T.apply(
        lambda row: row / row.sum(), axis=1
    )

    vote_results_percent["JUGEMENT MAJORITAIRE"] = [
        row[1][row[1] >= 0.5].head(1).index[0].upper()
        for row in (vote_results_percent.cumsum(axis=1)).iterrows()
    ]

    vote_results_percent = vote_results_percent[vote_results_percent.columns[::-1]]

    return vote_results_percent
