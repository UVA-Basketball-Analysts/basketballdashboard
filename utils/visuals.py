import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import re

class VisualsTool():
    def __init__(self):
        self.df = pd.read_csv("data/ClinicianReport.csv")
        
    def bilateral(self, playerid):
        bilateral_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "timestamp",
            "summary__bilateral_squat__mobility__depth__unit",
            "summary__bilateral_squat__mobility__hip__left",
            "summary__bilateral_squat__mobility__hip__right",
            "summary__bilateral_squat__mobility__hip__delta",
            "summary__bilateral_squat__mobility__knee__left",
            "summary__bilateral_squat__mobility__knee__right",
            "summary__bilateral_squat__mobility__knee__delta",
            "summary__bilateral_squat__mobility__ankle__left",
            "summary__bilateral_squat__mobility__ankle__right",
            "summary__bilateral_squat__mobility__ankle__delta",
            "summary__bilateral_squat__alignment__max_weight_shift__left",
            "summary__bilateral_squat__alignment__max_weight_shift__right",
            "summary__bilateral_squat__alignment__max_weight_shift__delta",
            "summary__bilateral_squat__alignment__dyn_valgus__left",
            "summary__bilateral_squat__alignment__dyn_valgus__right",
            "summary__bilateral_squat__alignment__dyn_valgus__delta",
            "summary__bilateral_squat__loading_strategy__bilateral"
        ]
        
        bilateral_df = self.df[bilateral_columns]
        player_df = bilateral_df[bilateral_df['meta__person__unique_id'].str.contains(playerid)]
        lines = []
        for column in player_df.columns:
            trace = go.Scatter(
                x=player_df['timestamp'],
                y=player_df[column],
                mode='lines',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Bilateral',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Value')
        )
        fig = go.Figure(data=lines, layout=layout)
        # fig.update_traces(visible="legendonly")
        return fig
    
    def unilateral(self, playerid):
        unilateral_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "timestamp",
            "summary__unilateral_squat__mobility__depth__left",
            "summary__unilateral_squat__mobility__depth__right",
            "summary__unilateral_squat__mobility__depth__delta",
            "summary__unilateral_squat__mobility__hip__left",
            "summary__unilateral_squat__mobility__hip__right",
            "summary__unilateral_squat__mobility__hip__delta",
            "summary__unilateral_squat__mobility__knee__left",
            "summary__unilateral_squat__mobility__knee__right",
            "summary__unilateral_squat__mobility__knee__delta",
            "summary__unilateral_squat__mobility__ankle__left",
            "summary__unilateral_squat__mobility__ankle__right",
            "summary__unilateral_squat__mobility__ankle__delta",
            "summary__unilateral_squat__alignment__pelvic_obliquity__left",
            "summary__unilateral_squat__alignment__pelvic_obliquity__right",
            "summary__unilateral_squat__alignment__pelvic_obliquity__delta",
            "summary__unilateral_squat__alignment__dyn_valgus__left",
            "summary__unilateral_squat__alignment__dyn_valgus__right",
            "summary__unilateral_squat__alignment__dyn_valgus__delta",
            "summary__unilateral_squat__loading_strategy__left_leg",
            "summary__unilateral_squat__loading_strategy__right_leg"
        ]
        unilateral_df = self.df[unilateral_columns]
        player_df = unilateral_df[unilateral_df['meta__person__unique_id'].str.contains(playerid)]
        lines = []
        for column in player_df.columns:
            trace = go.Scatter(
                x=player_df['timestamp'],
                y=player_df[column],
                mode='lines',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Bilateral',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Value')
        )
        fig = go.Figure(data=lines, layout=layout)
        # fig.update_traces(visible="legendonly")
        return fig
    
    def bivsuni(self, playerid):
        matching_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "timestamp",
            "summary__unilateral_squat__mobility__hip__left",
            "summary__unilateral_squat__mobility__hip__right",
            "summary__unilateral_squat__mobility__hip__delta",
            "summary__unilateral_squat__mobility__knee__left",
            "summary__unilateral_squat__mobility__knee__right",
            "summary__unilateral_squat__mobility__knee__delta",
            "summary__unilateral_squat__mobility__ankle__left",
            "summary__unilateral_squat__mobility__ankle__right",
            "summary__unilateral_squat__mobility__ankle__delta",
            "summary__bilateral_squat__mobility__hip__left",
            "summary__bilateral_squat__mobility__hip__right",
            "summary__bilateral_squat__mobility__hip__delta",
            "summary__bilateral_squat__mobility__knee__left",
            "summary__bilateral_squat__mobility__knee__right",
            "summary__bilateral_squat__mobility__knee__delta",
            "summary__bilateral_squat__mobility__ankle__left",
            "summary__bilateral_squat__mobility__ankle__right",
            "summary__bilateral_squat__mobility__ankle__delta",
            "summary__unilateral_squat__alignment__dyn_valgus__left",
            "summary__unilateral_squat__alignment__dyn_valgus__right",
            "summary__unilateral_squat__alignment__dyn_valgus__delta",
            "summary__bilateral_squat__alignment__dyn_valgus__left",
            "summary__bilateral_squat__alignment__dyn_valgus__right",
            "summary__bilateral_squat__alignment__dyn_valgus__delta",
        ]
        drop_columns = [
            ["summary__unilateral_squat__mobility__hip__left","summary__bilateral_squat__mobility__hip__left"],
            ["summary__unilateral_squat__mobility__hip__right","summary__bilateral_squat__mobility__hip__right"],
            ["summary__unilateral_squat__mobility__hip__delta","summary__bilateral_squat__mobility__hip__delta"],
            ["summary__unilateral_squat__mobility__knee__left","summary__bilateral_squat__mobility__knee__left"],
            ["summary__unilateral_squat__mobility__knee__right","summary__bilateral_squat__mobility__knee__right"],
            ["summary__unilateral_squat__mobility__knee__delta","summary__bilateral_squat__mobility__knee__delta"],
            ["summary__unilateral_squat__mobility__ankle__left","summary__bilateral_squat__mobility__ankle__left"],
            ["summary__unilateral_squat__mobility__ankle__right","summary__bilateral_squat__mobility__ankle__right"],
            ["summary__unilateral_squat__mobility__ankle__delta","summary__bilateral_squat__mobility__ankle__delta"],
            ["summary__unilateral_squat__alignment__dyn_valgus__left","summary__bilateral_squat__alignment__dyn_valgus__left"],
            ["summary__unilateral_squat__alignment__dyn_valgus__right","summary__bilateral_squat__alignment__dyn_valgus__right"],
            ["summary__unilateral_squat__alignment__dyn_valgus__delta","summary__bilateral_squat__alignment__dyn_valgus__delta"],
        ]
        matching_df = self.df[matching_columns]
        calculations = [[matching_df[col[0]] - matching_df[col[1]], col[0].replace('unilateral', 'difference')] for col in drop_columns]
        for series, cols in calculations:
            matching_df[cols] = series
        flaten = [item for items in drop_columns for item in items]
        matching_df = matching_df.drop(flaten, axis=1)
        player_df = matching_df[matching_df['meta__person__unique_id'].str.contains(playerid)]
        lines = []
        for column in player_df.columns:
            trace = go.Scatter(
                x=player_df['timestamp'],
                y=player_df[column],
                mode='lines',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Bilateral',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Value')
        )
        fig = go.Figure(data=lines, layout=layout)
        # fig.update_traces(visible="legendonly")
        return fig