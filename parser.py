import json
import matplotlib.pyplot as plt

def plot_chart(json_data):
    guesses = [item["Guesses"] for item in json_data["Guessing"]]
    id = [item["ID"] for item in json_data["Guessing"]]

    plt.bar(guesses, id)
    plt.xlabel("Guesses")
    plt.ylabel("ID")
    plt.title("Bar Chart from JSON Data")
    plt.show()

if __name__ == "__main__":
    with open("log.json", "r") as file:
        json_data = json.load(file)

    plot_chart(json_data)