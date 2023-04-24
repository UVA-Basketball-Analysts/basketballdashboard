import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import re
from dash import Dash, dash_table
from datetime import datetime

class VisualsTool():
    def __init__(self):
        temp = pd.read_csv("syntheticdata/synthetic_data.csv").sort_values(by="meta__session__session_datetime", ascending=True)
        temp['meta__session__session_datetime'] = [datetime.strptime(time, '%Y.%m.%d %H:%M:%S') for time in temp['meta__session__session_datetime']]
        self.column_names = {
                                'summary__bilateral_squat__mobility__depth__unit': 'unit__depth__bilateral_squat',
                                'summary__bilateral_squat__mobility__hip__left': 'left__hip__bilateral_squat',
                                'summary__bilateral_squat__mobility__hip__right': 'right__hip__bilateral_squat',
                                'summary__bilateral_squat__mobility__hip__delta': 'delta__hip__bilateral_squat',
                                'summary__bilateral_squat__mobility__knee__left': 'left__knee__bilateral_squat',
                                'summary__bilateral_squat__mobility__knee__right': 'right__knee__bilateral_squat',
                                'summary__bilateral_squat__mobility__knee__delta': 'delta__knee__bilateral_squat',
                                'summary__bilateral_squat__mobility__ankle__left': 'left__ankle__bilateral_squat',
                                'summary__bilateral_squat__mobility__ankle__right': 'right__ankle__bilateral_squat',
                                'summary__bilateral_squat__mobility__ankle__delta': 'delta__ankle__bilateral_squat',
                                'summary__bilateral_squat__alignment__max_weight_shift__left': 'left__max_weight_shift__bilateral_squat',
                                'summary__bilateral_squat__alignment__max_weight_shift__right': 'right__max_weight_shift__bilateral_squat',
                                'summary__bilateral_squat__alignment__max_weight_shift__delta': 'delta__max_weight_shift__bilateral_squat',
                                'summary__bilateral_squat__alignment__dyn_valgus__left': 'left__dyn_valgus__bilateral_squat',
                                'summary__bilateral_squat__alignment__dyn_valgus__right': 'right__dyn_valgus__bilateral_squat',
                                'summary__bilateral_squat__alignment__dyn_valgus__delta': 'delta__dyn_valgus__bilateral_squat',
                                'summary__bilateral_squat__loading_strategy__bilateral': 'bilateral__loading_strategy__bilateral_squat',
                                'summary__unilateral_squat__mobility__depth__left': 'left__depth__unilateral_squat',
                                'summary__unilateral_squat__mobility__depth__right': 'right__depth__unilateral_squat',
                                'summary__unilateral_squat__mobility__depth__delta': 'delta__depth__unilateral_squat',
                                'summary__unilateral_squat__mobility__hip__left': 'left__hip__unilateral_squat',
                                'summary__unilateral_squat__mobility__hip__right': 'right__hip__unilateral_squat',
                                'summary__unilateral_squat__mobility__hip__delta': 'delta__hip__unilateral_squat',
                                'summary__unilateral_squat__mobility__knee__left': 'left__knee__unilateral_squat',
                                'summary__unilateral_squat__mobility__knee__right': 'right__knee__unilateral_squat',
                                'summary__unilateral_squat__mobility__knee__delta': 'delta__knee__unilateral_squat',
                                'summary__unilateral_squat__mobility__ankle__left': 'left__ankle__unilateral_squat',
                                'summary__unilateral_squat__mobility__ankle__right': 'right__ankle__unilateral_squat',
                                'summary__unilateral_squat__mobility__ankle__delta': 'delta__ankle__unilateral_squat',
                                'summary__unilateral_squat__alignment__pelvic_obliquity__left': 'left__pelvic_obliquity__unilateral_squat',
                                'summary__unilateral_squat__alignment__pelvic_obliquity__right': 'right__pelvic_obliquity__unilateral_squat',
                                'summary__unilateral_squat__alignment__pelvic_obliquity__delta': 'delta__pelvic_obliquity__unilateral_squat',
                                'summary__unilateral_squat__alignment__dyn_valgus__left': 'left__dyn_valgus__unilateral_squat',
                                'summary__unilateral_squat__alignment__dyn_valgus__right': 'right__dyn_valgus__unilateral_squat',
                                'summary__unilateral_squat__alignment__dyn_valgus__delta': 'delta__dyn_valgus__unilateral_squat',
                                'summary__unilateral_squat__loading_strategy__left_leg': 'left_leg__loading_strategy__unilateral_squat',
                                'summary__unilateral_squat__loading_strategy__right_leg': 'right_leg__loading_strategy__unilateral_squat',
                                'summary__vertical_jump__mobility__loading__hip_flex__right': 'right__hip_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__hip_flex__delta': 'delta__hip_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__knee_flex__left': 'left__knee_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__knee_flex__right': 'right__knee_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__knee_flex__delta': 'delta__knee_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__ankle_flex__left': 'left__ankle_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__ankle_flex__right': 'right__ankle_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__loading__ankle_flex__delta': 'delta__ankle_flex__vertical_jump__loading',
                                'summary__vertical_jump__mobility__landing__hip_flex__left': 'left__hip_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__hip_flex__right': 'right__hip_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__hip_flex__delta': 'delta__hip_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__knee_flex__left': 'left__knee_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__knee_flex__right': 'right__knee_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__knee_flex__delta': 'delta__knee_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__ankle_flex__left': 'left__ankle_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__ankle_flex__right': 'right__ankle_flex__vertical_jump__landing',
                                'summary__vertical_jump__mobility__landing__ankle_flex__delta': 'delta__ankle_flex__vertical_jump__landing',
                                'summary__vertical_jump__alignment__loading__dyn_val__left': 'left__dyn_val__vertical_jump__loading',
                                'summary__vertical_jump__alignment__loading__dyn_val__right': 'right__dyn_val__vertical_jump__loading',
                                'summary__vertical_jump__alignment__loading__dyn_val__delta': 'delta__dyn_val__vertical_jump__loading',
                                'summary__vertical_jump__alignment__landing__dyn_val__left': 'left__dyn_val__vertical_jump__landing',
                                'summary__vertical_jump__alignment__landing__dyn_val__right': 'right__dyn_val__vertical_jump__landing',
                                'summary__vertical_jump__alignment__landing__dyn_val__delta': 'delta__dyn_val__vertical_jump__landing',
                                'summary__vertical_jump__performance__grf_takeoff__left': 'left__grf_takeoff__vertical_jump__performance',
                                'summary__vertical_jump__performance__grf_takeoff__right': 'right__grf_takeoff__vertical_jump__performance',
                                'summary__vertical_jump__performance__grf_takeoff__delta': 'delta__grf_takeoff__vertical_jump__performance',
                                'summary__vertical_jump__performance__peak_grf__bilateral': 'bilateral__peak_grf__vertical_jump__performance',
                                'summary__vertical_jump__landing_strategy__bilateral': 'bilateral__landing_strategy__vertical_jump',
                                'summary__concentric_jump__mobility__loading__hip_flex__left': 'left__hip_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__hip_flex__right': 'right__hip_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__hip_flex__delta': 'delta__hip_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__knee_flex__left': 'left__knee_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__knee_flex__right': 'right__knee_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__knee_flex__delta': 'delta__knee_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__ankle_flex__left': 'left__ankle_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__ankle_flex__right': 'right__ankle_flex__concentric_jump__loading',
                                'summary__concentric_jump__mobility__loading__ankle_flex__delta': 'delta__ankle_flex__concentric_jump__loading',
                                'summary__concentric_jump__alignment__loading__dyn_val__left': 'left__dyn_val__concentric_jump__loading',
                                'summary__concentric_jump__alignment__loading__dyn_val__right': 'right__dyn_val__concentric_jump__loading',
                                'summary__concentric_jump__alignment__loading__dyn_val__delta': 'delta__dyn_val__concentric_jump__loading',
                                'summary__concentric_jump__performance__jump_height__bilateral': 'bilateral__jump_height__concentric_jump__performance',
                                'summary__concentric_jump__performance__grf_takeoff__left': 'left__grf_takeoff__concentric_jump__performance',
                                'summary__concentric_jump__performance__grf_takeoff__right': 'right__grf_takeoff__concentric_jump__performance',
                                'summary__concentric_jump__performance__grf_takeoff__delta': 'delta__grf_takeoff__concentric_jump__performance',
                                'summary__concentric_jump__landing_strategy__bilateral': 'bilateral__landing_strategy__concentric_jump'
                            }
        self.df = temp.rename(self.column_names, axis=1)


    def bilateral(self, playerid):
        bilateral_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "meta__session__session_datetime",
            "left__hip__bilateral_squat",
            "right__hip__bilateral_squat",
            "delta__hip__bilateral_squat",
            "left__knee__bilateral_squat",
            "right__knee__bilateral_squat",
            "delta__knee__bilateral_squat",
            "left__ankle__bilateral_squat",
            "right__ankle__bilateral_squat",
            "delta__ankle__bilateral_squat",
            "left__max_weight_shift__bilateral_squat",
            "right__max_weight_shift__bilateral_squat",
            "delta__max_weight_shift__bilateral_squat",
            "left__dyn_valgus__bilateral_squat",
            "right__dyn_valgus__bilateral_squat",
            "delta__dyn_valgus__bilateral_squat",
            # "bilateral__loading_strategy__bilateral_squat"
        ]
        
        bilateral_df = self.df[bilateral_columns]
        
        if playerid != 'all':
            player_df = bilateral_df[bilateral_df['meta__person__unique_id'].str.contains(playerid)]
        else:
            player_df = bilateral_df
            
        lines = []
        # fig = go.Figure()
        for column in player_df.columns[3:]:
            trace = go.Bar(
                x=player_df['meta__session__session_datetime'],
                y=player_df[column],
                # mode='lines+markers',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Bilateral',
            xaxis=dict(title='meta__session__session_datetime'),
            yaxis=dict(title='Value'),
            xaxis_range=[
                            self.df['meta__session__session_datetime'],
                            self.df['meta__session__session_datetime'][len(self.df) - 1]
                        ]
        )
        fig = go.Figure(data=lines, layout=layout)
        fig.update_traces(visible="legendonly")
        return fig
    
    def unilateral(self, playerid):
        unilateral_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "meta__session__session_datetime",
            "left__depth__unilateral_squat",
            "right__depth__unilateral_squat",
            "delta__depth__unilateral_squat",
            "left__hip__unilateral_squat",
            "right__hip__unilateral_squat",
            "delta__hip__unilateral_squat",
            "left__knee__unilateral_squat",
            "right__knee__unilateral_squat",
            "delta__knee__unilateral_squat",
            "left__ankle__unilateral_squat",
            "right__ankle__unilateral_squat",
            "delta__ankle__unilateral_squat",
            "left__pelvic_obliquity__unilateral_squat",
            "right__pelvic_obliquity__unilateral_squat",
            "delta__pelvic_obliquity__unilateral_squat",
            "left__dyn_valgus__unilateral_squat",
            "right__dyn_valgus__unilateral_squat",
            "delta__dyn_valgus__unilateral_squat",
            "left_leg__loading_strategy__unilateral_squat",
            "right_leg__loading_strategy__unilateral_squat"
        ]
        unilateral_df = self.df[unilateral_columns]
        
        if playerid != 'all':
            player_df = unilateral_df[unilateral_df['meta__person__unique_id'].str.contains(playerid)]
        else:
            player_df = unilateral_df
            
        lines = []
        for column in player_df.columns[3:]:
            trace = go.Bar(
                x=player_df['meta__session__session_datetime'],
                y=player_df[column],
                #mode='lines+markers',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Unilateral',
            xaxis=dict(title='meta__session__session_datetime'),
            yaxis=dict(title='Value'),
            xaxis_range=[
                            self.df['meta__session__session_datetime'],
                            self.df['meta__session__session_datetime'][len(self.df) - 1]
                        ]
        )
        fig = go.Figure(data=lines, layout=layout)
        fig.update_traces(visible="legendonly")
        return fig
    
    def bivsuni(self, playerid):
        matching_columns = [
            "meta__person__unique_id",
            "meta__session__session_guid",
            "meta__session__session_datetime",
            "left__hip__unilateral_squat",
            "right__hip__unilateral_squat",
            "delta__hip__unilateral_squat",
            "left__knee__unilateral_squat",
            "right__knee__unilateral_squat",
            "delta__knee__unilateral_squat",
            "left__ankle__unilateral_squat",
            "right__ankle__unilateral_squat",
            "delta__ankle__unilateral_squat",
            "left__hip__bilateral_squat",
            "right__hip__bilateral_squat",
            "delta__hip__bilateral_squat",
            "left__knee__bilateral_squat",
            "right__knee__bilateral_squat",
            "delta__knee__bilateral_squat",
            "left__ankle__bilateral_squat",
            "right__ankle__bilateral_squat",
            "delta__ankle__bilateral_squat",
            "left__dyn_valgus__unilateral_squat",
            "right__dyn_valgus__unilateral_squat",
            "delta__dyn_valgus__unilateral_squat",
            "left__dyn_valgus__bilateral_squat",
            "right__dyn_valgus__bilateral_squat",
            "delta__dyn_valgus__bilateral_squat",
        ]
        drop_columns = [
            ["left__hip__unilateral_squat","left__hip__bilateral_squat"],
            ["right__hip__unilateral_squat","right__hip__bilateral_squat"],
            ["delta__hip__unilateral_squat","delta__hip__bilateral_squat"],
            ["left__knee__unilateral_squat","left__knee__bilateral_squat"],
            ["right__knee__unilateral_squat","right__knee__bilateral_squat"],
            ["delta__knee__unilateral_squat","delta__knee__bilateral_squat"],
            ["left__ankle__unilateral_squat","left__ankle__bilateral_squat"],
            ["right__ankle__unilateral_squat","right__ankle__bilateral_squat"],
            ["delta__ankle__unilateral_squat","delta__ankle__bilateral_squat"],
            ["left__dyn_valgus__unilateral_squat","left__dyn_valgus__bilateral_squat"],
            ["right__dyn_valgus__unilateral_squat","right__dyn_valgus__bilateral_squat"],
            ["delta__dyn_valgus__unilateral_squat","delta__dyn_valgus__bilateral_squat"],
        ]
        matching_df = self.df[matching_columns]
        calculations = [[matching_df[col[0]] - matching_df[col[1]], col[0].replace('unilateral', 'difference')] for col in drop_columns]
        for series, cols in calculations:
            matching_df[cols] = series
        flaten = [item for items in drop_columns for item in items]
        matching_df = matching_df.drop(flaten, axis=1)
        
        if playerid != 'all':
            player_df = matching_df[matching_df['meta__person__unique_id'].str.contains(playerid)]
        else:
            player_df = matching_df
            
        lines = []
        for column in player_df.columns[3:]:
            trace = go.Bar(
                x=player_df['meta__session__session_datetime'],
                y=player_df[column],
                #mode='lines+markers',
                name=column
            )
            lines.append(trace)

        layout = go.Layout(
            title='Clinician Difference',
            xaxis=dict(title='meta__session__session_datetime'),
            yaxis=dict(title='Value'),
            xaxis_range=[
                            self.df['meta__session__session_datetime'],
                            self.df['meta__session__session_datetime'][len(self.df) - 1]
                        ]
        )
        fig = go.Figure(data=lines, layout=layout)
        fig.update_traces(visible="legendonly")
        return fig
    
    def loading_strategy(self,playerid):
        if playerid != 'all':
            one_athlete = self.df[self.df['meta__person__unique_id'].str.contains(playerid)]
        else:
            one_athlete = self.df
        df_strat = one_athlete.filter(regex = re.compile(r'meta__session__session_datetime|bilateral__loading_strategy__bilateral_squat|left_leg__loading_strategy__unilateral_squat|right_leg__loading_strategy__unilateral_squat|summary__lateral_lunge__loading_strategy__left_leg|summary__lateral_lunge__loading_strategy__right_leg'))

        lines = []
        for column in df_strat.columns[2:7]:
            trace = go.Scatter(x=df_strat['meta__session__session_datetime'],
                               y=df_strat[column],
                               name = column)
            lines.append(trace)
        layout = go.Layout(
            title='Loading Strategies',
            xaxis=dict(title='meta__session__session_datetime'),
            yaxis=dict(title='Strategy'),
            xaxis_range=[
                            self.df['meta__session__session_datetime'],
                            self.df['meta__session__session_datetime'][len(self.df) - 1]
                        ]
            # legend=dict(orientation="h")
        )

        fig = go.Figure(data=lines, layout=layout)
        return fig
    
    def loading_strategy_table(self, playerid):

        if playerid != 'all':
            one_athlete = self.df[self.df['meta__person__unique_id'].str.contains(playerid)]
        else:
            one_athlete = self.df
                                    
        df_strat = one_athlete.filter(regex = re.compile(r'meta__session__session_datetime|bilateral__loading_strategy__bilateral_squat|left_leg__loading_strategy__unilateral_squat|right_leg__loading_strategy__unilateral_squat|summary__lateral_lunge__loading_strategy__left_leg|summary__lateral_lunge__loading_strategy__right_leg'))

        #df_strat = df_strat.drop('meta__session__session_datetime', axis=1)

        df_strat['meta__session__session_datetime'] = [str(time) for time in df_strat['meta__session__session_datetime']]
        df_strat.set_index('meta__session__session_datetime', inplace=True)


        df_transposed = df_strat.transpose()

        df_transposed = df_transposed.reset_index()
        df_transposed['strategies'] = df_transposed['index']

        df_transposed = df_transposed.drop('index', axis=1)

        strategies_col = df_transposed.pop('strategies')
        df_transposed.insert(0, 'strategies', strategies_col)


        df_transposed['strategies'] = df_transposed['strategies'].str.replace('_', ' ')

        return df_transposed 
    
    def jumps_figure(self, playerid, variables):
        if playerid != 'all':
            user_df = self.df.query("meta__person__unique_id == @playerid")
        else:
            user_df = self.df
        if variables == None:
            variables = []
        melted_df = pd.melt(user_df, id_vars=['meta__session__session_datetime'], value_vars=variables)

        fig1 = px.scatter(melted_df,
                       x="meta__session__session_datetime",
                       y="value",
                       color = "variable")
        fig1.update_layout(xaxis_range=[
                            self.df['meta__session__session_datetime'],
                            self.df['meta__session__session_datetime'][len(self.df) - 1]
                        ])

        # fig1.update_layout(width=1750, height=800, autosize=False)

        return fig1