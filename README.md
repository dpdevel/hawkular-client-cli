# hawkular-client-cli

This repository includes a Python client script to access Hawkular metrics remotely.

## Introduction

Utility script for accessing Hawkular metrics server remotely, the script can query
a list of metric definitions and tags, update metrics tags, read and write metric data.
The script is using the python [hawkular-client](https://github.com/hawkular/hawkular-client-python) module.

## License and copyright

```
   Copyright 2016 Red Hat, Inc. and/or its affiliates
   and other contributors.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## Installation

To install, run ``python setup.py install`` if you installed from source code, or ``pip install hawkular-client-cli`` if using pip.

## Usage

The `-h` flag will print out a help text, that list the command line arguments.

```bash
hawkular-client-cli -h

usage: command_line.py [-h] [-n [URL]] [-i] [-t NAME] [-c [CONFIG_FILE]]
                       [-p [PASSWORD]] [-u [USERNAME]]
                       [-a [TAG=VALUE [TAG=VALUE ...]]] [-k [KEY [KEY ...]]]
                       [-l] [-r] [-v]
                       [KEY=VALUE [KEY=VALUE ...]]

Read/Write data to and from a Hawkular metric server.

positional arguments:
  KEY=VALUE             key value pairs to send

optional arguments:
  -h, --help            show this help message and exit
  -n [URL], --url [URL]
                        Hawkualr server url
  -i, --insecure        allow insecure ssl connection
  -t NAME, --tenant NAME
                        Hawkualr tenenat name
  -c [CONFIG_FILE], --config [CONFIG_FILE]
                        Configurations file path
  -p [PASSWORD], --password [PASSWORD]
                        Hawkualr server password
  -u [USERNAME], --username [USERNAME]
                        Hawkualr server username
  -a [TAG=VALUE [TAG=VALUE ...]], --tags [TAG=VALUE [TAG=VALUE ...]]
                        a list of tags [ when used with a list of keys, will
                        update tags for this keys ]
  -k [KEY [KEY ...]], --keys [KEY [KEY ...]]
                        a list of keys [ when used with a list of tags, will
                        update tags for this keys ]
  -l, --list            list all registered keys, can be used with --tags
                        argument for filtering
  -r, --read            read data for keys or tag list [requires the --keys or
                        --tags arguments]
  -v, --version         print versionusage: command_line.py [-h] [-n [URL]] [-i] [-t NAME] [-c [CONFIG_FILE]]
                       [-p [PASSWORD]] [-u [USERNAME]]
                       [-a [TAG=VALUE [TAG=VALUE ...]]] [-k [KEY [KEY ...]]]
                       [-l] [-r] [-v]
                       [KEY=VALUE [KEY=VALUE ...]]

```
### Querying metric definitions [ -l ]
Metric definitions list can also be filtered using tags.

```bash
hawkular-client-cli -l
hawkular-client-cli -l -a issue=42
```
### Querying metric data [ -r KEY ]
Query for metrics data can be done using a list of keys [ using the -k argument ]
or using a list of tag,value pairs [ using the -a argument ]

```bash
hawkular-client-cli -r -k machine/example.com/memory.usage
hawkular-client-cli -r -a issue=42
```
### Pushing new values [ KEY=VALUE ]
When pushing new data, we also update the tag values of the keys we push data to,
If not explicit tags are defined ( e.g. using the -a argument ) tags are set using
rules in the config file.

```bash
hawkular-client-cli machine/example.com/memory.usage=300
```
### Modifying metric definition tags [ -k KEY -a TAG=VALUE ]
If a key match an auto-tagging rule from a config file, the tag value defined
in the config file will be updated. Explicit tag values defined using the command line
argument [ -a or --tags ] will override tag values defined by rules in the config file.

```bash
hawkular-client-cli -k machine/example.com/memory.usage -a units=bytes
```

### Config file
If present, a yaml config file, can be used to store credentials information, and
tagging rules. Command line arguments will override credentials and tags defined in
the config file.

Default path for the config file is `/etc/hawkular-client-cli/conifg.yaml`

The hawkuklar part of the yaml file can store information about the hawklar server,
for example, username and password.

The auto-tagging rules match the rules regex with pre-defined tags, for example, the rules
in this example will add the tag `units` with value `bytes` to any key that match the regex pattern `.*memory.*`.

```yaml
hawkular:
  url: https:/hawkular-metrics.com:443
  username: hawkular
  password: secret
  tenant: _ops
rules:
  - regex: .*
    tags:
      type: node
      hostname: example.com
  - regex: .*memory.*
    tags:
      units: byte
  - regex: .*cpu.*
    tags:
      units: cpu
```
