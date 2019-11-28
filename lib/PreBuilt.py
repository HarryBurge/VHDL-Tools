class AND():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = self.I1 and self.I2

    def getOutputs(self):
        return {'O1':self.O1}


class OR():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = self.I1 or self.I2

    def getOutputs(self):
        return {'O1':self.O1}


class NOT():

    O1 = False

    def __init__(self, I1):
        self.I1 = I1

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.compute()

    def compute(self):
        self.O1 = not self.I1

    def getOutputs(self):
        return {'O1':self.O1}


class XOR():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = self.I1 ^ self.I2

    def getOutputs(self):
        return {'O1':self.O1}


class NAND():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = not(self.I1 and self.I2)

    def getOutputs(self):
        return {'O1':self.O1}


class NOR():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = not(self.I1 or self.I2)

    def getOutputs(self):
        return {'O1':self.O1}


class XNOR():

    O1 = False

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.O1 = not(self.I1 ^ self.I2)

    def getOutputs(self):
        return {'O1':self.O1}


class Half_Adder():

    O1 = False
    COut = False
    XORs = {}
    ANDs = {}

    def __init__(self, I1, I2):
        self.I1 = I1
        self.I2 = I2

        self.XORs['1'] = XOR(False, False)
        self.ANDs['1'] = AND(False, False)

    def setInputs(self, Inputs):
        self.I1 = Inputs.get('I1')
        self.I2 = Inputs.get('I2')
        self.compute()

    def compute(self):
        self.XORs.get('1').setInputs({'I1':self.I1, 'I2':self.I2})
        self.O1 = self.XORs.get('1').getOutputs().get('O1')

        self.ANDs.get('1').setInputs({'I1':self.I1, 'I2':self.I2})
        self.COut = self.ANDs.get('1').getOutputs().get('O1')

    def getOutputs(self):
        return {'O1':self.O1, 'COut':self.COut}
