import plotly.offline as py
import webview
import plotly.graph_objects as go

labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]

py.offline.plot(figure_or_data=[go.Pie(labels=labels, values=values)], filename='file.html', auto_open=False)

webview.create_window("Selected Image's Location", 'file.html', min_size=(1100, 300))
webview.start()
