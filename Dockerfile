FROM python:3.8

# Set work directory
WORKDIR /app

RUN pip3 install virtualenv
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH=$VIRTUAL_ENV


COPY ./app $WORKDIR
# Install dependencies
CMD . venv/bin/activated
RUN pip install -r requirements.txt
CMD ['python', 'runner.py', 'db', 'upgrade']
EXPOSE 5000