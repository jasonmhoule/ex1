FROM rocker/rstudio:3.6.3

# RUN apt-get update && apt-get install -y \
#     curl \
#     gnupg

# # Install gcsfuse: https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md
# # RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
# # RUN echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list
# RUN echo "deb http://packages.cloud.google.com/apt gcsfuse-`lsb_release -c -s` main" | tee /etc/apt/sources.list.d/gcsfuse.list
# # RUN echo "deb http://packages.cloud.google.com/apt gcsfuse-stretch main" | tee /etc/apt/sources.list.d/gcsfuse.list
# # RUN cat /etc/apt/sources.list.d/gcsfuse.list
# RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
# RUN apt-get update && apt-get install -y gcsfuse

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    apt-transport-https \
    ca-certificates \
    ssh-client
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN sudo apt-get update && sudo apt-get install -y google-cloud-sdk


COPY files/gs_loader.R /home/script.R
