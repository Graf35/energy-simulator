import logging

#Создаём класс демона логирования
class Deman_log(object):
    def __init__(self):
        self.logfile = open('log.txt', "w")
        self.logfile.close()
        logging.basicConfig(format = u'%(filename)s %(funcName)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level = logging.INFO, filename="log.txt")
        logging.info("Деман лога призван!")


