# create s3 bucket for terraform state
resource "aws_s3_bucket" "s3_for_severe_weather" {
  bucket = "chizoba-weather-severe-file"

  tags = {
    Name        = "weather_severe_file"
    Environment = "local_prod"
  }
}


# create s3 bucket for weather API
resource "aws_s3_bucket" "severe_weather_bucket" {
  bucket = "chizoba-severe-weather-data"

  tags = {
    Name        = "severe_weather_bucket"
    Environment = "local_Dev"
  }
}