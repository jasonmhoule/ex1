proj_name <- ""

# Connect
system("gcloud init --account=652580964228-compute@developer.gserviceaccount.com --project=ml-learning-199501", intern = TRUE)

# Load config files
system("gsutil cp -r gs://jmh_config/jmh_config/* .")

# Download
system(paste0("gsutil cp -r gs://jmh/", proj_name, " ."), intern = TRUE)

# Upload
system(paste0("gsutil cp -r . gs://jmh/", proj_name), intern = TRUE)
