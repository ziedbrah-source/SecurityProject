# PROTON++ the best Python-Secure-Chatroom application!
THIS PROJECT IS MADE BY Soulaima Kahla && Mohamed Zied Brahmi.


LIBRARIES USED: (the important ones)
TKINTER,OPENLDAP,OPENSSL,RABBITMQ AMPQ

Special thanks to : 
Mr Yousffi Souhaieb for LDAP/ASYMMETRIC,ASYMMETRIC encryption course,
Mr Sofiane ouni for distributed systems and rabbitMQ course.


> ***Architecture:***
> * a rabbitmq server to link between senders and receivers ( we will send encrypted messages over it)
> * an authority server to sign certificates and give them to users
> * an ldap server that holds the tree structure of our app
> * the main application server : 
> > * It will generate keys and send the request to the autority server to give back the certificate
> > * It will encrypt and decrypt messages and put them into the interface 
> > * It will handle event received from rabbitmq server.
> > * It will send event through rabbitmq server.
         


