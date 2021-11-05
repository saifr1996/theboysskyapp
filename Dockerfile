# Use Python 3.6 or later as a base image
FROM python:3.7
# Copy contents into image
COPY  . .
# Install pip dependencies from requirements
RUN pip install flask
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "app.py"]
