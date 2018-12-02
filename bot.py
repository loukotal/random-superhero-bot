from mastodon import Mastodon
import os
import random
# from textgenrnn import textgenrnn

mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_KEY"),
    api_base_url="https://botsin.space"
)


def lambda_handler(event, context):
    with open("generated_names.txt","r") as f:
        lines = f.readlines()
        heroes_list = [random.choice(lines) for _ in range(6)]

    # heroes_names = textgenrnn(weights_path="heroes_textgen.hdf5", config_path="textgenrnn_config.json",
    #                           vocab_path="textgenrnn_vocab.json")
    # heroes_list = heroes_names.generate(5, return_as_list=True)
    heroes = "\n".join(heroes_list)
    mastodon.status_post("New superheroes on the block!\n\n{}".format(heroes))
    return {
        "statusCode": 200,
        "body": "{}".format(heroes)
    }


if __name__ == "__main__":
    pass
    # heroes_names = textgenrnn(weights_path="heroes_textgen.hdf5", config_path="textgenrnn_config.json",
    #                           vocab_path="textgenrnn_vocab.json")
    # heroes_names.generate_to_file("generated_names.txt", n=10000, temperature=1)
