from .controller import Controller
from . import resources as r

app = Controller('api', __name__)
app.add_resource('/', r.IndexResource)
app.add_resource('/auth', r.AuthIndexResource)
app.add_resource('/builds', r.BuildIndexResource)
app.add_resource('/repos', r.RepositoryIndexResource)
app.add_resource('/repos/<repository_id>/builds', r.RepositoryBuildsResource)
