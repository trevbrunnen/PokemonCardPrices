from shiny import App, render, ui, reactive
import pandas as pd
import os
import pathlib

dir = pathlib.Path(__file__).parent

#@reactive.file_reader(dir / 'PokemonGroups.csv')
def read_groups():
    return pd.read_csv(dir / "PokemonGroups.csv")


groups = read_groups()

app_ui = ui.page_fluid(
            ui.layout_sidebar(
                ui.panel_sidebar(
                    #ui.input_selectize('sets','Select Sets',groups['name'],multiple=True),
                    ui.input_switch("fullwidth", "Take full width", True),
                    ui.input_switch("fixedheight", "Fixed height", True)
                ),
                ui.panel_main(
                    ui.output_data_frame("grid")
                )
            )
        )


def server(input, output, session):

    @output
    @render.data_frame
    def grid():
        height = 350 if input.fixedheight() else None
        width = "100%" if input.fullwidth() else "fit-content"
        return render.DataGrid(
                groups,
                row_selection_mode='multiple',
                height=height,
                width=width,
                filters=True,
        )

app = App(app_ui, server)
