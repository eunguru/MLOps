from sacred import Experiment

ex = Experiment()

@ex.automain
def my_main():
    print("hello world")