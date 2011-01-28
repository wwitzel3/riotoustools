from minimock import Mock

from riotoustools import models
models.DBSession = Mock('DBSession')
