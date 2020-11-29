import io
import base64
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


def gen_temp_plot(temperature, maximums, minimums, timestamps):
    # create figure with one axes
    fig, ax = plt.subplots()

    # prettify
    ax.xaxis.set_major_formatter(DateFormatter('%d.%m %H:%M'))
    fig.autofmt_xdate(rotation=40)
    fig.tight_layout()

    # plot all the data at one axes
    ax.plot(timestamps, temperature, 'ko')
    ax.plot(timestamps, maximums, 'r')
    ax.plot(timestamps, minimums, 'b')

    # create a bytes stream
    img = io.BytesIO()
    # save figure to stream
    plt.savefig(img, format='png')
    img.seek(0)

    # encode bytes-like object using base64, than decode binary data
    plot_url = base64.b64encode(img.getvalue()).decode()
    # close bytes stream
    img.close()

    return plot_url
