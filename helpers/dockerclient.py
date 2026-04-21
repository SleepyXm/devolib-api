import docker
import os

docker_client = docker.DockerClient(
    base_url=os.getenv("DOCKER_HOST", f"unix://{os.path.expanduser('~')}/.docker/run/docker.sock")
)