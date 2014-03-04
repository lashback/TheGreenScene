from greenscene.settings import common as settings

def debug(context):
  return { 'DEBUG': settings.DEBUG }