import io
import base64
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


def gen_temp_plot(temperature, maximums, minimums, timestamps):
    img = io.BytesIO()

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(DateFormatter('%d.%m %H:%M'))
    fig.autofmt_xdate(rotation=40)
    fig.tight_layout()

    ax.plot(timestamps, temperature, 'ko')
    ax.plot(timestamps, maximums, 'r')
    ax.plot(timestamps, minimums, 'b')

    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url
