bucketname <- ""
system(paste0("gcsfuse -o nonempty ", bucketname, " ."), intern = TRUE)
