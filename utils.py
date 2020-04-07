import plotly.graph_objects as go

def imc_chart(imc):
    if imc<16 or imc>30:
        color="red"
    elif (imc>16 and imc<18.5) or (imc>25 and imc<30):
        color="orange"
    elif imc>18.5 and imc<25:
        color="green"
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = imc,
    mode = "gauge+number",
    title = {'text': "IMC"},
    gauge = {'axis': {'range': [None, 50]},
             'bar': {'color': color},
             'steps' : [
                 {'range': [0, 16], 'color': "white"},
                 {'range': [16, 18.5], 'color': "white"},
                 {'range': [18.5, 25], 'color': "white"},
                 {'range': [25, 30], 'color': "white"},
                 {'range': [30, 50], 'color': "white"}],
             'threshold' : {'line': {'color': color, 'width': 8}, 'thickness': 0.75, 'value': imc}}))

    
    return fig

def calories_chart(bmr, ded, tded):
    colors = ["grey", "orange", "green"]

    fig = go.Figure(data=[go.Bar(
        x=['Basal Metabolic Ratio', 'Daily Energy Deprivation', 'Target Daily Energy Deprivation'],
        y=[bmr, ded, tded],
        #marker={"colorbar":{"tickangle":-30}},
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_layout(title_text='Calories consumption')
    return fig