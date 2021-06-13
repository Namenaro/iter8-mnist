from descriptorA import DescriptorA

class DescriptorUB:
    def __init__(self, descrB, ux, uy):
        self.ux = ux
        self.uy = uy
        self.descriptorB = descrB


    def get_all_hypotheses_in_point(self, pic, coordx, coordy):
        pic2 = self.descriptorB.get_reaction_on_pic(pic)
        centerx= coordx+self.ux
        centery= coordy+self.uy

