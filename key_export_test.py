import json
from os import path

import tempfile
import logbook

from nio import EncryptionError
from nio.crypto import Olm
from nio.crypto.key_export import decrypt, decrypt_and_read, encrypt, encrypt_and_save
from nio.store import DefaultStore

from nio.log import logger_group

TEST_ROOM = "!test:example.org"


def test_invalid_json_schema(tempdir):
    file = path.join(tempdir, "keys_file")

    payload = {"sessions": [{"algorithm": "test"}]}
    encrypt_and_save(json.dumps(payload).encode(), file, "pass", count=10)

    imported = Olm.import_keys_static(file, "pass")

    assert len(imported) == 0

if __name__ == "__main__":
    logger_group.level = logbook.DEBUG
    log_handler = logbook.StderrHandler(level=logbook.DEBUG)
    with log_handler.applicationbound():
        with tempfile.TemporaryDirectory() as tempdir:
            test_invalid_json_schema(tempdir)
