import logging
import os

BASE_DIR = '/app'

BACKEND = 'Mattermost'
BOT_EXTRA_BACKEND_DIR = '/app/plugins/errbot-mattermost-backend'

login = os.getenv('login')
password = os.getenv('password')

BOT_IDENTITY = {
        # Required
        'login': login,
        'password': password,
        'team': 'Geeked Out',
        'server': 'chat.mycroft.ai',
        # Optional
        'insecure': False, # Default = False. Set to true for self signed certificates
        'scheme': 'https', # Default = https
        'port': 8065, # Default = 8065
        'timeout': 30 # Default = 30. If the webserver disconnects idle connections later/earlier change this value
}

# The location where all of Err's data should be stored. Make sure to set
# this to a directory that is writable by the user running the bot.
BOT_DATA_DIR = '/tmp'

### Repos and plugins config.

# Set this to change from where errbot gets its installable plugin list.
# By default it gets the index from errbot.io which is a file generated by tools/plugin-gen.py.
# BOT_PLUGIN_INDEXES = 'http://version.errbot.io/repos.json'
#
# You can also specify a local file:
# BOT_PLUGIN_INDEXES = 'tools/repos.json'
#
# Or a list. note: if some plugins exists in 2 lists, only the first hit will be taken into account.
# BOT_PLUGIN_INDEXES = ('/data/repos.json', 'https://my.private.tld/errbot/myrepos.json')

# Set this to a directory on your system where you want to load extra
# plugins from, which is useful mostly if you want to develop a plugin
# locally before publishing it. Note that you can specify only a single
# directory, however you are free to create subdirectories with multiple
# plugins inside this directory.
BOT_EXTRA_PLUGIN_DIR = "/app/plugins"
print(BOT_EXTRA_PLUGIN_DIR)

# The location of the log file. If you set this to None, then logging will
# happen to console only.
BOT_LOG_FILE = None

# The verbosity level of logging that is done to the above logfile, and to
# the console. This takes the standard Python logging levels, DEBUG, INFO,
# WARN, ERROR. For more info, see http://docs.python.org/library/logging.html
#
# If you encounter any issues with Err, please set your log level to
# logging.DEBUG and attach a log with your bug report to aid the developers
# in debugging the issue.
BOT_LOG_LEVEL = logging.INFO


##########################################################################
# Account and chatroom (MUC) configuration                               #
##########################################################################


# Set the admins of your bot. Only these users will have access
# to the admin-only commands.
#
# Unix-style glob patterns are supported, so 'gbin@localhost'
# would be considered an admin if setting '*@localhost'.
BOT_ADMINS = ('@btotharye',)
