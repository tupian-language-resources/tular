from pathlib import Path

from clld.web.assets import environment

import tular


environment.append_path(
    Path(tular.__file__).parent.joinpath('static').as_posix(),
    url='/tular:static/')
environment.load_path = list(reversed(environment.load_path))
