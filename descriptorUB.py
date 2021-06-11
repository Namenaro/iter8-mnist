from descriptorA import DescriptorA

class DescriptorUB:
    def __init__(self, descrB, ux, uy):
        self.ux = ux
        self.uy = uy
        self.descriptorB = descrB

    def count_statistics(self, pics_for_stat, n_bins):
        pass

    def apply(self, pic, coordx, coordy):
        # we find all local mimimas of popravca of descrB in all the pic