# import the libs requises
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from kalliope.core.NeuronModule import NeuronModule
# config
#  logging

logging.basicConfig()
logger = logging.getLogger("kalliope")

# création de la class

class Mailsend(NeuronModule):
    def __init__(self, **kwargs):
        super(Mailsend, self).__init__(**kwargs)
        # fix des variables
        self.Fromadd = kwargs.get('Fromadd', None) # adresse expediteur
        self.MDP = kwargs.get('MDP', None) # mots de passe
        self.Toadd = kwargs.get('Toadd', None) # adresse destinataire
        self.message = kwargs.get('message', None) # message du mail
        self.subject = kwargs.get('subject', None)
        
        Fromadd = self.Fromadd
        Toadd = self.Toadd    ##  Spécification des destinataires
        Subject= self.subject
        message = MIMEMultipart()    ## Création de l'objet "message"
        message['From'] = Fromadd    ## Spécification de l'expéditeur
        message['To'] = Toadd    ## Attache du destinataire à l'objet "message"
        message['Subject'] = Subject    ## Spécification de l'objet de votre mail
        msg = self.message ## Message à envoyer
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8

        serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en précisant son nom et son port)
        serveur.starttls()    ## Spécification de la sécurisation
        serveur.login(Fromadd, self.MDP)    ## Authentification
        texte= message.as_string().encode('utf-8')    ## Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
        serveur.sendmail(Fromadd, Toadd, texte)    ## Envoi du mail
        serveur.quit()    ## Déconnexion du serveur