FROM ghcr.io/prefix-dev/pixi:0.72.0-bullseye-slim AS build

# Use bash as shell
SHELL ["/bin/bash", "-c"]

WORKDIR /app

ENV PATH=$PATH:/opt/conda/bin:/opt/conda/condabin

#RUN pixi global install pixi-install-to-prefix pixi-inject

COPY src /app
COPY pixi.lock pyproject.toml README.md /app/

RUN pixi reinstall --locked -e default && \
    pixi publish --target-dir .pixi/publish --path pyproject.toml && \
    pixi exec rattler inject-into-prefix -p $CONDA_PREFIX .pixi/publish/{{cookiecutter.import_name}}-*.conda

FROM condaforge/mambaforge:24.9.2-0 AS production

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY --from=build /opt/conda /opt/conda

EXPOSE 8000

ENTRYPOINT [ "{{cookiecutter.import_name}}" ]