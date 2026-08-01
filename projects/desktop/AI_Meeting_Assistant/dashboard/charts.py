import matplotlib.pyplot as plt


def draw_speaker_chart(
        stats):

    names = list(
        stats.keys()
    )

    values = list(
        stats.values()
    )

    plt.figure(
        figsize=(6, 6)
    )

    plt.pie(
        values,
        labels=names,
        autopct="%1.1f%%"
    )

    plt.title(
        "Speaker Ratio"
    )

    plt.savefig(
        "reports/speaker.png"
    )

    plt.close()