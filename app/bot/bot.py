from mastodon import Mastodon
import os
import random

from textgenrnn import textgenrnn

# from app.settings import MASTODON_API_URL

mastodon = Mastodon(
    # access_token=os.getenv("MASTODON_ACCESS_KEY"),
    access_token="0efddcc59647b1713e405e2460c48f402ed0423e0eea1068863465716d0f78b7",
    api_base_url="https://botsin.space"
)

heroes_names = textgenrnn(weights_path="weights/heroes_textgen.hdf5", config_path="weights/textgenrnn_config.json",
                          vocab_path="weights/textgenrnn_vocab.json")


def lambda_handler(event, context):
    with open("../outputs/generated_names.txt", "r") as f:
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
    # LOAD THE TRAINED MODEL
    # heroes_names = textgenrnn(weights_path="..weights/heroes_textgen.hdf5",
    #                           config_path="..weights/textgenrnn_config.json",
    #                           vocab_path="..weights/textgenrnn_vocab.json")
    #
    # GENERATE THE NAMES
    # heroes_names.generate_to_file("../outputs/generated_names.txt", n=10000, temperature=1)
