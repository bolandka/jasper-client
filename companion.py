#!/usr/bin/env python2
# -*- coding: utf-8-*-

import os
import sys
import shutil
import logging

import yaml
import argparse

from client import tts
from client import stt
from client import jasperpath
from client import diagnose
from client.conversation import Conversation
import simon
import daniel
import nostalgie

# Add jasperpath.LIB_PATH to sys.path
sys.path.append(jasperpath.LIB_PATH)

parser = argparse.ArgumentParser(description='Pocket Companion Control Center')
parser.add_argument('--local', action='store_true',
                    help='Use text input instead of a real microphone')
parser.add_argument('--no-network-check', action='store_true',
                    help='Disable the network connection check')
parser.add_argument('--diagnose', action='store_true',
                    help='Run diagnose and exit')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
parser.add_argument('--transcribe', action='store_true', help='Show transcriptions')
parser.add_argument('--rank', action='store_true', help='Rank speaker according to his wilkoishness')
parser.add_argument('--zeljko', action='store_true', help='Imitate Zeljkos behaviour')
parser.add_argument('--simon', action='store_true', help='Get the good old WTS-Wiki Jokes of the Day')
parser.add_argument('--kataUndBen', action='store_true', help='Notify the Stammtisch organizers that you are thirsty')
parser.add_argument('--matt', action='store_true', help='Get some sound advice by git master Matt')
parser.add_argument('--daniel', action='store_true', help='Activate the Daniel ambient engine')
parser.add_argument('--nostalgie', action='store_true', help='Nostalgia: in rememberance of the great WTS choir')
args = parser.parse_args()

if args.local:
    from client.local_mic import Mic
else:
    from client.mic import Mic


class Companion(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

        # Create config dir if it does not exist yet
        if not os.path.exists(jasperpath.CONFIG_PATH):
            try:
                os.makedirs(jasperpath.CONFIG_PATH)
            except OSError:
                self._logger.error("Could not create config dir: '%s'",
                                   jasperpath.CONFIG_PATH, exc_info=True)
                raise

        # Check if config dir is writable
        if not os.access(jasperpath.CONFIG_PATH, os.W_OK):
            self._logger.critical("Config dir %s is not writable. Pocket companion " +
                                  "won't work correctly.",
                                  jasperpath.CONFIG_PATH)

        new_configfile = jasperpath.config('profile.yml')

        # Read config
        self._logger.debug("Trying to read config file: '%s'", new_configfile)
        try:
            with open(new_configfile, "r") as f:
                self.config = yaml.safe_load(f)
        except OSError:
            self._logger.error("Can't open config file: '%s'", new_configfile)
            raise

        try:
            stt_engine_slug = self.config['stt_engine']
        except KeyError:
            stt_engine_slug = 'sphinx'
            logger.warning("stt_engine not specified in profile, defaulting " +
                           "to '%s'", stt_engine_slug)
        stt_engine_class = stt.get_engine_by_slug(stt_engine_slug)

        try:
            slug = self.config['stt_passive_engine']
            stt_passive_engine_class = stt.get_engine_by_slug(slug)
        except KeyError:
            stt_passive_engine_class = stt_engine_class

        try:
            tts_engine_slug = self.config['tts_engine']
        except KeyError:
            tts_engine_slug = tts.get_default_engine_slug()
            logger.warning("tts_engine not specified in profile, defaulting " +
                           "to '%s'", tts_engine_slug)
        tts_engine_class = tts.get_engine_by_slug(tts_engine_slug)

        # Initialize Mic
        self.mic = Mic(tts_engine_class.get_instance(),
                       None,
                       stt_engine_class.get_active_instance())

    def run(self):
    
        if args.simon:
            return simon.run(self.mic)
        
        if args.daniel:
            return daniel.run(self.mic)
    
        if args.nostalgie:
            return nostalgie.run()

        if 'first_name' in self.config:
            salutation = ("How can I be of service, %s?"
                          % self.config["first_name"])
        else:
            salutation = "How can I be of service?"
        self.mic.say(salutation)

        conversation = Conversation("COMPANION", self.mic, self.config)
        conversation.handleForever(args.rank, args.zeljko, args.kataUndBen, args.matt)

if __name__ == "__main__":

    print("*******************************************************")
    print("*               WILKO'S POCKET COMPANION              *")
    print("*                         <3                          *")
    print("*******************************************************")

    logging.basicConfig()
    logger = logging.getLogger()
    
    if args.transcribe:
        logger.getChild("client.stt").setLevel(logging.INFO)

    if args.debug:
        logger.setLevel(logging.DEBUG)


    if not args.no_network_check and not diagnose.check_network_connection():
        logger.warning("Network not connected. This may prevent the pocket companion from " +
                       "running properly.")

    if args.diagnose:
        failed_checks = diagnose.run()
        sys.exit(0 if not failed_checks else 1)

    try:
        app = Companion()
    except Exception:
        logger.error("Error occured!", exc_info=True)
        sys.exit(1)

    app.run()
