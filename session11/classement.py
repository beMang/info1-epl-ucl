from orderedlinkedlist import OrderedLinkedList

class Classement:
    """
    Une implémentation primitive de classement, non ordonnée et de capacité fixe.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__resultats = OrderedLinkedList([])

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__resultats.size()

    def result(self):
        return self.__resultats

    def add(self,r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Le résultat est simplement ajouté à la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des éléments.
        """
        self.__resultats.add(r)

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        node = self.__resultats.first()
        while node is not None:
            if node.value().coureur() == c:
                return (node.value())
            node = node.next()

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Etant donné que la dictionnaire de résultats ne connaît pas de position,
                    pour le moment cette méthode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaînée ordonnée
                    comme structure de données, plutôt qu'une simple dictionnaire.
        """
        node = self.__resultats.first()
        i = 1
        while node is not None:
            if node.value().coureur() == c:
                return i
            i += 1
            node = node.next()
        return -1

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        node = self.__resultats.first()
        previous = node
        while node is not None:
            if node.value().coureur() == c:
                if node == self.__resultats.first():
                    self.__resultats.remove_first()
                    return c
                else:
                    previous.set_next(node.next())
                    self.__resultats.dec_size()
                    return c
            previous = node
            node = node.next()
        return False

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        d = self.__resultats.get_as_array()
        for c in d:
            s += "  " + str(self.get_position(c.coureur())) + " > " + str(c.coureur()) + "\n"
        return s
