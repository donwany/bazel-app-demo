# Use a Python base image
FROM python:3.11.3-slim-bullseye

# Install Bazel
RUN apt-get update && apt-get install -y apt-transport-https curl gnupg
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor -o /usr/share/keyrings/bazel-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
RUN apt-get update && apt-get install -y bazel

# Set the working directory
WORKDIR /usr/app

# Copy your Bazel project into the container
COPY . /usr/app

# COPY ./requirements.txt /usr/app
RUN pip install --no-cache-dir -r /usr/app/requirements.txt

# Build the project
# RUN bazel build //:hello

# Set environment variables
#ENV name=elbowai
#ENV age=45
#ENV job=running
#ENV num_a=99
#ENV num_b=100

# Set the entry point for your application
#CMD ["bazel",
#    "run",
#    "main:hello",
#    "--", \
#    "--name=$name", \
#    "--age=$age", \
#    "--job=$job", \
#    "--num_a=$num_a", \
#    "--num_b=$num_b"
#    ]

CMD ["sh", "-c", "bazel run main:hello -- --name=$name --age=$age --job=$job --num_a=$num_a --num_b=$num_b"]


