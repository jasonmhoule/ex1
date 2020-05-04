proj_name <- ""

# Connect
system("gcloud init --account=652580964228-compute@developer.gserviceaccount.com --project=ml-learning-199501", intern = TRUE)

# Load config files and change RSA file permissions
system("gsutil cp -r gs://jmh_config/jmh_config/* . && chmod 600 ~/.ssh/id_rsa && chmod 600 ~/.ssh/id_rsa.pub")

# Download all project files from GCS
system(paste0("gsutil -m cp -r gs://jmh/", proj_name, " ."), intern = TRUE)

# Upload all project files to GCS
system(paste0("gsutil -m cp -r . gs://jmh/", proj_name), intern = TRUE)

# Once loaded and logged into project, one-time setup to change repo origin to use SSH
system(paste0("git remote set-url origin git@github.com:jasonmhoule/", proj_name, ".git"), intern = TRUE)
