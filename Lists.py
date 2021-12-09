import random


class Responses:
    responses_negro = ["Qual foi a última coisa que passou pela cabeça da princesa Diana?\nO rádio",
                       "Porque é que não existem medicamentos na Etiópia?\nPorque não podem ser tomados em jejum.",
                       "O sujeito vai ao médico:\n– Doutor, tenho tendências suicidas. O que faço?\n– Em primeiro lugar, pague a consulta.",
                       "Qual a diferença entre um padre e um tenista?\nAs bolas com que o tenista brinca têm pelinhos.",
                       "Qual é a parte mais dura de um vegetal?\nA cadeira de rodas.",
                       "O que faz um leproso no banho?\nNestum",
                       "Porque é que a Anne Frank não acabou o diário?\nProblemas de concentração.",
                       "Porque é que o Hitler se suicidou?\nPorque viu a conta do gás.",
                       "O que se chama a dois sem-abrigos a atirar pedras um ao outro?\nUma luta de almofadas.",
                       "Sabias que sem árabes não tinha acontecido o 11/9?\nTinha acontecido o XI/IX.",
                       "Hitler estava a caminhar num campo de concentração quando ouve “sniff, sniff…”.\nVira-se e vê uma menina a chorar enquanto mexia num cinzeiro com o dedo. Hitler aproxima-se, mete-lhe a mão por cima do ombro e pergunta:\n– Era alguém conhecido?",
                       "Qual é a diferença entre uma pizza e um judeu?\nA pizza quando vai ao forno não grita."
                       ]

    def __init__(self, message):
        self.responses_enri = ["https://c.tenor.com/lVLSSglhk1cAAAAC/monkey-cymbals.gif",
                               "https://c.tenor.com/7Glf51FDQZQAAAAM/monkey-annoying.gif"]
        self.responses = ["who be juan kanobi"]

        self.responses_olek = [f"Olha {message.author.mention} sobes ao {random.randint(0, 1000)}º andar e saltas.",
                               "Isso dá muito trabalho...",
                               "@rogue#0001 faz tu!",
                               "https://media1.tenor.com/images/5ad50b6db3dc7ed4ca10dd65d4ea84c2/tenor.gif?itemid=11811769",
                               "levas com a garrafa"]
