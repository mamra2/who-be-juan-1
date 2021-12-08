import random


class Responses:
    def __init__(self, message):

        self.responses_enri = ["https://c.tenor.com/lVLSSglhk1cAAAAC/monkey-cymbals.gif",
                               "https://c.tenor.com/7Glf51FDQZQAAAAM/monkey-annoying.gif"]
        self.responses = ["who be juan kanobi"]

        self.responses_olek = [f"Olha {message.author.name} sobes ao {random.randint(0, 1000)}º andar e saltas.",
                               "Isso dá muito trabalho...",
                               "@rogue#0001 faz tu!",
                               "https://media1.tenor.com/images/5ad50b6db3dc7ed4ca10dd65d4ea84c2/tenor.gif?itemid=11811769",
                               "levas com a garrafa"]


    def get_response(self, number):
        return self.responses[number]

    def get_responses_olek(self, number):
        return self.responses_olek[number]

    def get_responses_enri(self, number):
        return self.responses_enri[number]