# -*- coding: utf-8-*-
import logging
from brain import Brain
import time
import wpm

class Conversation(object):

    def __init__(self, persona, mic, profile):
        self._logger = logging.getLogger(__name__)
        self.persona = persona
        self.mic = mic
        self.profile = profile
        self.brain = Brain(mic, profile)

    def handleForever(self):
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
                end = time.clock()
                wpm.run(start, end, input, self.mic)
