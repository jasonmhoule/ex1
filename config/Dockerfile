FROM rocker/rstudio:3.6.3

RUN apt-get update && apt-get install -y \
    curl \
    gnupg

# Install gcsfuse: https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md
RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
RUN echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get install -y gcsfuse
