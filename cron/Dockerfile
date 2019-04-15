FROM ubuntu:latest
LABEL MAINTAINER=trim21<trim21me@gmail.com>

RUN apt-get update && apt-get -y install cron

# Add crontab file in the cron directory
ADD crontabfile /etc/cron.d/bgmi-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/bgmi-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

RUN crontab /etc/cron.d/bgmi-cron

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log