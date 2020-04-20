# importation des libs requises
import smtplib
import logging
from kalliope.core.NeuronModule import NeuronModule
# config de logging
logging.basicConfig()
logger = logging.getLogger("kalliope")
# création de la class
class mailsend(NeuronModule):
    def __init__(self, **kwargs):
        super(mailsend, self).__init__(**kwargs)
        # fix des variables
        self.Fromadd = kwargs.get('Fromadd', None) # adresse expediteur
        self.MDP = kwargs.get('MDP', None) # mots de passe
        self.Toadd = kwargs.get('Toadd', None) # adresse destinataire
        self.message = kwargs.get('message', None) # message du mail
        
        serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en précisant son nom et son port)
        serveur.starttls()    ## Spécification de la sécurisation
        serveur.login(self.Fromadd, self.MDP)    ## Authentification
        message = self.message    ## Message à envoyer
        serveur.sendmail(self.Fromadd, self.Toadd, message)    ## Envoie du message
        serveur.quit()    ## Déconnexion du serveur