# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates a Container VM with the provided Container manifest."""


COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GlobalComputeUrl(project, collection, name):
  return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                  '/global/', collection, '/', name])


def ZonalComputeUrl(project, zone, collection, name):
  return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                  '/zones/', zone, '/', collection, '/', name])


def GenerateConfig(context):
  """Generate configuration."""

  res = []
  base_name = (context.env['deployment'] + '-vm1')
  
  MANIFEST = """
  apiVersion: v1
  kind: Pod
  metadata:
    name: simple-echo
  spec:
    containers:
    - name: simple-echo
      image: gcr.io/google-samples/hello-app:2.0
      imagePullPolicy: Always
      ports:
      - containerPort: 8080
        hostPort: 8080
  """
  
  MANIFEST2 = """
  apiVersion: v1
  kind: Pod
  metadata:
    name: rocker
  spec:
    containers:
    - name: rocker
      image: docker.io/rocker/rstudio
      imagePullPolicy: Always
      env:
      - name: PASSWORD
        value: swordfish
      stdin: true
      tty: true
      restartPolicy: Always
      ports:
      - containerPort: 8787
        hostPort: 8787
  """
  

  # Properties for the container-based instance.
  instance = {
      'zone': context.properties['zone'],
      'machineType': ZonalComputeUrl(context.env['project'],
                                     context.properties['zone'],
                                     'machineTypes',
                                     'n1-standard-1'),
      'metadata': {
          'items': [{
              'key': 'gce-container-declaration',
              'value': MANIFEST2
              },{
              'key': 'google-logging-enabled',
              'value': 'true'
          }]
      },
      'tags': {
          'items': ['http-server',
                    'https-server']
      },
      'disks': [{
          'deviceName': 'boot',
          'type': 'PERSISTENT',
          'autoDelete': True,
          'boot': True,
          'initializeParams': {
              'diskName': base_name + '-disk',
              'sourceImage': GlobalComputeUrl('cos-cloud',
                                              'images',
                                              'family/cos-stable')
              },
      }],
      'networkInterfaces': [{
          'accessConfigs': [{
              'name': 'external-nat',
              'type': 'ONE_TO_ONE_NAT'
              }],
          'network': GlobalComputeUrl(context.env['project'],
                                      'networks',
                                      'default')
      }],
      'serviceAccounts': [{
          'email': 'default',
          'scopes': [
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring.write"
          ]
      }]
  }
  res.append({
      'name': base_name,
      'type': 'compute.v1.instance',
      'properties': instance
  })
  # Resources to return.
  resources = {
      'resources': res,
  }

  return resources
