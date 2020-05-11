proj_name <- ""

# Initialize and clone repo (using SSH)
system(paste0("gcloud init --account=652580964228-compute@developer.gserviceaccount.com --project=ml-learning-199501 && ",
              "gsutil cp -r gs://jmh_config/jmh_config/* . && ",
              "chmod 600 ~/.ssh/id_rsa && ",
              "chmod 600 ~/.ssh/id_rsa.pub && ",
              "git clone git@github.com:jasonmhoule/", proj_name, ".git"))

# From outside project, to download & overwrite files from bucket (assumes existing folder)
system(paste0("gsutil -m cp -r gs://jmh/", proj_name, " ."))

# From within project, resync files to bucket (creates folder if needed; ignores .git)
system(paste0("gsutil -m rsync -rd -x .git . gs://jmh/", proj_name))
