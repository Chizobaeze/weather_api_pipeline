resource "aws_iam_user" "severe_weather_user" {
  name = "severe_weather_user"
}

resource "aws_iam_access_key" "severe_weather_access_key" {
  user = aws_iam_user.severe_weather_user.name
}

resource "aws_iam_user_policy" "lb_ro" {
  name = "severe_policy"
  user = aws_iam_user.severe_weather_user.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["s3:ListAllBuckets"],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": ["s3:PutObject"],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::chizoba-weather-severe-api/*"
    }
  ]
}
EOF
}


#ssm parameters using random
resource "aws_ssm_parameter" "severe_user_ssm_access" {
  name  = "chizoba-severe-access-key"
  type  = "String"
  value = aws_iam_access_key.severe_weather_access_key.id
  overwrite = true
}

resource "random_password" "app_password" {
  length  = 20
  special = true
}

resource "aws_ssm_parameter" "secure_app_password" {
  name        = "/severe-weather-api/app-password"
  description = "Random password for Severe Weather API app"
  type        = "SecureString"
  value       = random_password.app_password.result
}