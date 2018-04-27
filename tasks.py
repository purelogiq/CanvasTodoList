from invoke import task, call


@task
def start(ctx):
    """Start all services in the background.

    Only starts or restarts services if they are not already running with latest changes.
    """
    ctx.run("docker-compose up -d", pty=True)


@task
def stop(ctx):
    """Stop all running services."""
    ctx.run("docker-compose down")


@task(
    help={
        "service": "The docker-compose service to show output for. If none, output from "
                   "all services will be interleaved together.",
        "tail": "Amount of past output to include. Use 'all' to show all past output.",
        "nofollow": "Exit immediately and do not show new output automatically.",
    }
)
def show(ctx, service=None, tail=80, nofollow=False):
    """Show the output of a service."""
    cmd = (
        f"docker-compose logs --tail={tail}{' ' if nofollow else ' -f '}{service or ''}"
    )
    ctx.run(cmd, pty=True)


@task(
    help={
        "service": "The docker-compose service to show output for.",
    },
    pre=[call(start)]
)
def shell(ctx, service):
    """Attach to a service container to run commands in a shell."""
    result = ctx.run(
        f"docker-compose ps | grep -o '.*canvastodolist_{service}_.'", hide=True
    )
    container = result.stdout.strip()
    ctx.run(f"docker exec -it {container} /bin/bash", pty=True)


@task()
def rebuild(ctx):
    """Forces a clean rebuild of all service images and containers."""
    ctx.run("docker-compose down")
    ctx.run("docker-compose build --no-cache")
    ctx.run("docker-compose up --force-recreate -d")


@task()
def buildjs(ctx):
    """Build all frontend files using webpack."""
    ctx.run("docker-compose run webpack npm run build", pty=True)
