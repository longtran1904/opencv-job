### If you want to run docker manually (without using docker compose)
### run this script
docker build -t opencvjob .
create docker volume {your_volume_name}
docker run --mount source={your_volume_name},target=/usr/src/app opencvjob