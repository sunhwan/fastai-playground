FROM continuumio/miniconda

# Remove (large file sizes) MKL optimizations.
RUN conda install nomkl

# Install dependencies
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
RUN echo "source activate fastai" > ~/.bashrc
ENV PATH /opt/conda/envs/fastai/bin:$PATH

# Add our code
ADD . / /opt/webapp/
WORKDIR /opt/webapp

# Run the image as a non-root user
RUN adduser --disabled-password myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 

