# -*- coding: utf-8-*-
import logging
import time
import wpm
import wilkoscore
import zeljko
import kataUndBen

class Conversation(object):

    def __init__(self, persona, mic, profile):
        self._logger = logging.getLogger(__name__)
        self.persona = persona
        self.mic = mic
        self.profile = profile
    
    def handleForever(self, rankWilkoishness=False, imitateZeljko=False, contactKataAndBen=False):
        """
        Delegates user input to the handling function.
        """

        while True:              
            threshold = None

            start = time.clock()
    
            input = self.mic.activeListenToAllOptions(threshold)
            self._logger.debug("Stopped to listen actively with threshold: %r",
                               threshold)

            if input:
                if input[0]:
                    end = time.clock()
                    if rankWilkoishness:
                        wilkoscore.run(wpm.computeWpm(start, end, input, self.mic))
                    if imitateZeljko:
                        zeljko.run(self.mic)
                    if contactKataAndBen:
                        return kataUndBen.run(input[0], self.mic)
                    else:
                        wpm.run(start, end, input, self.mic)
