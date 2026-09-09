import matplotlib.pyplot as plt


def generate_score_chart(scores, output_path):

    labels = list(scores.keys())

    values = list(scores.values())

    plt.figure(figsize=(8, 4))

    plt.plot(
        labels,
        values,
        marker="o",
        linewidth=2
    )

    plt.grid(True)

    plt.title(
        "Evolution du Score Quantitatif"
    )

    plt.ylabel("Score")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    return output_path
``
