from invoke import task, call

@task
def start(ctx, detached=False):
    cmd = "docker-compose up"
    cmd = cmd + " -d" if detached else cmd
    ctx.run(cmd, pty=True)


@task
def stop(ctx):
    ctx.run("docker-compose down")


@task(pre=[call(start, detached=True)])
def shell(ctx):
    result = ctx.run("docker-compose ps | grep -o 'todomvctypedpixi_python_.'", hide=True)
    container = result.stdout.strip()
    ctx.run(f"docker exec -it {container} /bin/bash", pty=True)
