# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#  Copyright 2020 yafra.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------
#
# YAPKI certificate control
import logging
from sqlalchemy.orm import Session
from model import db, schemas

logger = logging.getLogger(__name__)


def get_certificates(dbs: Session):
    certs = dbs.query(db.DbCertificate).order_by(db.DbCertificate.common_name).all()
    if certs:
        logger.debug("yapki CLI - list all certificates stored in the database")
        for c in certs:
            logger.debug(c.serial)
        return certs
    else:
        return 0
