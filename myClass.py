import pandas as pd

class myObject:
    
    #url='C:/Users/Greta/Desktop/formation IA/Class/data.csv'
    url=None
    df=None
    
    def test(self):
        print('test', self.url)
    
    def __str__(self):#si str(nouveau objet)
        return 'mon objet'
    
    def stat(self):
        print("description:", self.df.describe())
        
    

    def __init__(self, url_fichier): #nouveau objet = myObjet(url_fichier)
        self.url = url_fichier
        self.df = pd.read_csv(self.url)
        print('Création, url:', self.url, 'et taille frame:', self.df.shape)
        
#if __name__ == "__main__":
