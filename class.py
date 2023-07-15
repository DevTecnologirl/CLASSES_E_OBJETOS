class Casa():
    rua = "Blue Street"
    bairro = "Good Neighborhood"
    CEP = "123654"
        
    def enderecoCompleto(self):
        return "Endereço Completo: "+self.rua+ ", "+ self.bairro+ " - CEP: "+ self.CEP
    
casa1 = Casa()
print(type(casa1))