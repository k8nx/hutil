from BeautifulSoup import BeautifulSoup as BS

import yaml

class Configuration:
  def __init__(self):
    self.props = dict()

  def __getitem__(self, name):
    return self.props.get(name)

  def __setitem__(self, name, value):
    self.props[name] = value

  def loadYAML(self, filename, chroot = None):
    if chroot is None and filename.find("#") > 0:
      chroot = filename[filename.find("#")+1:]
      filename = filename[:filename.find("#")]
    else:
      filename = filename

    try:
      body = open(filename).read()
      root = yaml.load(body) if chroot is None else yaml.load(body)[chroot]
    except:
      root = dict()

    for name in root:
      self.props[name] = root[name]

  def loadXML(self, filename):
    try:
      xml = open(filename).read()
      soup = BS(xml)
      for p in soup.findAll("property"):
        name = p.find("name").text
        value = p.find("value").text
        self.props[str(name)] = str(value)
    except:
      pass

  def generateAsYAMLFile(self, output, extra=None):
    value = self.generateAsYAML(extra)
    try:
      f = file(output, "w")
      f.write(value)
      f.flush()
      f.close()
    except:
      pass

  def generateAsXMLFile(self, output, extra=None, indent=2):
    value = self.generateAsXML(extra=extra, indent=indent)
    try:
      f = file(output, "w")
      f.write(value)
      f.flush()
      f.close()
    except:
      pass

  def copy(self, extra=None):
    ps = {}
    for name in self.props:
      ps[name] = self.props[name]

    if extra is not None:
      for name in extra:
        ps[name] = extra[name]
    
    return ps

  def generateAsYAML(self, extra = None):
    return yaml.dump(self.copy(extra))

  def generateAsXML(self, extra=None, indent=2):
    try:
      indent = abs(int(indent))
    except:
      indent = 2
    (level1, level2) = (" " * indent, " " * indent * 2)
    ps = self.copy(extra)

    xml = """<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
"""
    for name in ps:
      if type(ps[name]) == bool:
        ps[name] = 'true' if ps[name] else 'false'
      if type(ps[name]) == list:
        ps[name] = ','.join([str(value) for value in ps[name]])
      xml += """
%s<property>
%s<name>%s</name>
%s<value>%s</value>
%s</property>
"""%(level1, level2, name, level2, ps[name], level1)
    xml += """
</configuration>
"""
    return xml
