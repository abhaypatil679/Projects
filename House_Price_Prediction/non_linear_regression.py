from numpy import polyfit, linspace, polyval
from plotly.graph_objs import Figure


def poly_regression(df, col, target, equations_dict, degree=2, round_off=2):

    coeffs = polyfit(x=df[col].values, y=df[target].values, deg=degree).round(round_off)

    # for readability formatting coeffients in equations form.
    eq_str = ''
    curr_indx = degree

    for coef in coeffs:
        eq_str += f'+{coef}*(x**{curr_indx})'
        curr_indx -= 1

    # adding the equation to result dictionary.
    res = eq_str
    equations_dict[col] = res
    x_pred = linspace(start=df[col].min(), stop=df[col].max(), num=100)
    y_pred = polyval(coeffs, x_pred)

    # plotting figure with the fit line.
    fig = Figure()
    fig.add_scatter(x=df[col], y=df[target], mode='markers', name=f'{col}')
    fig.add_scatter(x=x_pred, y=y_pred, mode='lines', name=f'prediction<br>degree = {degree}')
    fig.layout.template = 'gridon'
    fig.layout.title.text = f'{col} vs {target}'
    fig.layout.xaxis.title.text = col
    fig.layout.xaxis.rangemode = 'tozero'
    fig.layout.yaxis.title.text = target
    fig.layout.font.size = 13

    # plotting graph in notebook
    print(res)
    fig.show()
    return equations_dict
