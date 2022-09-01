#!/usr/bin/python3
# -*- coding: utf-8 -*-
# gera_log.py ------------------------------------------------------- #
# ------------------------------------------------------------------- #
# Author: Daniel Noronha da Silva C012743                             #
#  Phone: +5585987680611                                              #
# ------------------------------------------------------------------- #
# Programa criado para ser uma forma simples de gerar logs das        #
# aplicações criadas em python.                                       #
# ------------------------------------------------------------------- #
# Changelog: -------------------------------------------------------- #
#   v0.1 - 01/09/2022 - Daniel Noronha                                #
#     - Criação da classe GeraLog                                     #
# ------------------------------------------------------------------- #

# IMPORTS ----------------------------------------------------------- #
import logging
# ------------------------------------------------------------------- #

# VARIÁVEIS --------------------------------------------------------- #
# ------------------------------------------------------------------- #

# CLASSE ------------------------------------------------------------ #

class GeraLog:
  def __init__(self, name_log):
    self.log_file = name_log
    self.filemode = "a"

  def grava_info(self, mensagem):
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
      filename=self.log_file,
      filemode=self.filemode,
      format=log_format,
      level=logging.INFO
    )

    logger = logging.getLogger()
    logger.info(mensagem)

  def grava_warning(self, mensagem):
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
      filename=self.log_file,
      filemode=self.filemode,
      format=log_format,
      level=logging.WARNING
    )

    logger = logging.getLogger()
    logger.warning(mensagem)

  def grava_error(self, mensagem):
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
      filename=self.log_file,
      filemode=self.filemode,
      format=log_format,
      level=logging.ERROR
    )

    logger = logging.getLogger()
    logger.error(mensagem)

  def grava_critical(self, mensagem):
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
      filename=self.log_file,
      filemode=self.filemode,
      format=log_format,
      level=logging.CRITICAL
    )

    logger = logging.getLogger()
    logger.critical(mensagem)

# ------------------------------------------------------------------- #
