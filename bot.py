from mastodon import Mastodon
import os
from textgenrnn import textgenrnn

mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_KEY"),
    api_base_url="https://botsin.space"
)


def lambda_handler(event, context):
    #
    heroes_names = textgenrnn(weights_path="heroes_textgen.hdf5", config_path="textgenrnn_config.json",
                              vocab_path="textgenrnn_vocab.json")
    heroes_list = heroes_names.generate(5, return_as_list=True)
    heroes = "\n".join(heroes_list)
    mastodon.status_post("{}".format(heroes))
    return {
        "statusCode": 200,
        "body": "{}".format(heroes)
    }


if __name__ == "__main__":
    heroes_names = textgenrnn(weights_path="heroes_textgen.hdf5", config_path="textgenrnn_config.json",
                              vocab_path="textgenrnn_vocab.json")
    heroes_names.generate()
